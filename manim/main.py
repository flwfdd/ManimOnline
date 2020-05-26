import subprocess
import time
import threading
import socket
import urllib.parse
import os
import signal
import psutil
import config
import json

flag={} # 刺杀令
p={} # 存储进程
run_ct=0 # 当前运行数量
runlist=[] # 当前运行用户名

def readstd(name):
    while True:
        s=str(p[name].stdout.readline(),encoding='utf-8')
        if(p[name].poll()!=None): return
        if p[name].poll() == None or s!='':
            with open("./data/"+name+"/out.html",'a') as f:
                f.write(s)
        else: break

def readerr(name):
    while True:
        s=str(p[name].stderr.readline(),encoding='utf-8')
        if(p[name].poll()!=None): return
        if p[name].poll() == None or s!='':
            with open("./data/"+name+"/out.html",'a') as f:
                f.write(s)
        else: break

def creatsub(cmd,name):
    global run_ct
    flag[name]=0
    run_ct+=1
    runlist.append(name)
    p[name]=subprocess.Popen(cmd,shell=True,stdout=subprocess.PIPE,stderr=subprocess.PIPE)
    with open("./data/"+name+"/out.html",'w') as f:
        f.write("Start at "+time.strftime("%Y--%m--%d %H:%M:%S",time.localtime())+"\n")

    threading.Thread(target=readstd,args=(name,)).start()
    threading.Thread(target=readerr,args=(name,)).start()
    while(p[name].poll()==None):
        time.sleep(1)
        if flag[name]==1: # 处理上一层下发的刺杀令
            try: psutil.Process(p[name].pid).children()[0].kill()
            except: pass
    with open("./data/"+name+"/out.html",'a') as f:
        f.write("Finish at "+time.strftime("%Y--%m--%d %H:%M:%S",time.localtime()))
    run_ct-=1
    flag[name]=1
    runlist.remove(name)


def start_conn(conn,addr): # 处理一个连接请求
    s=""
    while True:
        r=conn.recv(1024)
        s+=str(r,encoding="utf-8")
        if len(r)!=1024: break
        
    try:
        '''
        s=s.split("\r\n")[0].split(" ")[1]
        if s.find("?")==-1:
            conn.close()
            return
        s=s[s.find("?")+1:]
        '''
        s=s.split("\r\n\r\n")[1]
        dic=urllib.parse.parse_qs(s)
        
    except: conn.close()

    #print("GET ",s,dic)
    
    try:
        if dic['cmd'][0]=="run_ct": # 正在运行的数量
            res="HTTP/1.1 200 OK\r\n\r\n"+str(run_ct)
            if "name" in dic:
                if dic['name'][0] in flag: res+="/"+str(1^flag[dic['name'][0]])
                else: res+="/0"
            conn.send(res.encode('utf-8'))
            conn.close()
            return
        if dic["cmd"][0]=="run": # 运行
            if dic['name'][0] in runlist:
                res="HTTP/1.1 200 OK\r\n\r\nerror"
                conn.send(res.encode('utf-8'))
                conn.close()
                return
            if os.path.exists("./data/"+dic['name'][0])==False: os.mkdir("./data/"+dic['name'][0])
            with open("./data/"+dic['name'][0]+"/"+dic['name'][0]+".py","w") as f:
                f.write(dic['code'][0])
            cmd=config.manimcmd+" "+os.getcwd()+"/data/"+dic['name'][0]+"/"+dic['name'][0]+".py"+" test --leave_progress_bars --video_output_dir "+os.getcwd()+"/data/"+dic['name'][0]+"/ "
            threading.Thread(target=creatsub,args=(cmd+dic["opt"][0],dic['name'][0])).start()
            res="HTTP/1.1 200 OK\r\n\r\nok"
            conn.send(res.encode('utf-8'))
            conn.close()
            return
        if dic["cmd"][0]=="close": # 停止运行
            flag[dic['name'][0]]=1
            res="HTTP/1.1 200 OK\r\n\r\nok"
            conn.send(res.encode('utf-8'))
            conn.close()
            return
        if dic["cmd"][0]=="run_list": # 运行列表
            res="HTTP/1.1 200 OK\r\n\r\n"+json.dumps(runlist)
            conn.send(res.encode('utf-8'))
            conn.close()
            return
        if dic["cmd"][0]=="gif": # 转换gif
            if dic['name'][0] in runlist or os.path.exists("./data/"+dic['name'][0]+"/test.mp4")==False:
                res="HTTP/1.1 200 OK\r\n\r\nerror"
                conn.send(res.encode('utf-8'))
                conn.close()
                return
            cmd="ffmpeg -i "+os.getcwd()+"/data/"+dic['name'][0]+"/test.mp4 -s 480*270 -r 15 -y "+os.getcwd()+"/data/"+dic['name'][0]+"/test.gif"
            threading.Thread(target=creatsub,args=(cmd,dic['name'][0])).start()
            res="HTTP/1.1 200 OK\r\n\r\nok"
            conn.send(res.encode('utf-8'))
            conn.close()
            return
    except: conn.close()

def start_tcp():
    so=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    so.bind(("",config.port))
    so.listen(5)

    print("Server Started\n")
    while True:
        conn,addr=so.accept()
        threading.Thread(target=start_conn,args=(conn,addr)).start()

start_tcp()
