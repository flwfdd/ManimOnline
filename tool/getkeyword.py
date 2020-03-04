import os
import re
import json

files=[]

for root,d,f in os.walk("./manimlib"):
    files+=[os.path.join(root,i) for i in f if i[-3:]==".py"]


defs=set() #变量们
classs=set() #类们
for file in files:
    with open(file,"r") as f:
        s=f.read()
        l=re.findall("\n[ ]*def .+\(",s)
        for i in l:
            if i[i.find("def")+4]!='_':
                defs.add(i[i.find("def")+4:-1])
        l=re.findall("\n[ ]*class .+\(",s)
        for i in l:
            if i[i.find("class")+6]!='_':
                classs.add(i[i.find("class")+6:-1])

# value : 输入值
# caption: 匹配值
# meta: 提示值
# score : 权重

with open("keyword.js","w") as f:
    s=json.dumps(list(defs))
    f.write("defs="+s+"\n")
    s=json.dumps(list(classs))
    f.write("classs="+s)
