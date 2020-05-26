# [ManimOnline](http://manim.online)

You can experience it on [manim.online](http://manim.online).(or the backup on [manim.ml](http://manim.ml) | [manim.cf](http://manim.cf))

[Manim](https://github.com/3b1b/manim) is a Mathematical ANIMation engine programed by Grant(the author of `3Blue1Brown` channel).

I make some small tools so that you can experience manim online. Btw, I'm a high school student, the server is in my home and the website isn't very stable.

---
不用在意上面的乱七八糟的东西（除了网站链接

先推一波我的[bilibili](https://space.bilibili.com/27482524)(=・ω・=)

再鸣谢一下manim交流群(862671480)里的大佬们。

* 易学易用的在线 manim
* 好看的界面
* 一键生成视频和GIF
* 带有全套 manim **代码补全**、自动缩进、代码高亮的在线IDE
* ~~性能低下的服务器~~

这个网站可以让你不用麻麻烦烦的配置系统运行环境就能体验到`manim`的美妙，也可以帮助你非常方便地测试小效果并导出视频以及GIF动图。界面自以为还挺直白的，直接进入网站体验即可。

**请注意**，不要在网站上运行计算量过大的项目，如果你认为自己真的对`manim`感兴趣，那在自己电脑上安装`manim`是十分有必要的。可以加入上面提到的qq群一起交流。

---

什么？你还不会manim？好吧，因为个人能力有限，我的manim使得也不大好，但是我可以给你推荐一些教程。

b站是个好地方，有众多manim玩的贼amazing的up如:[鹤翔万里](https://space.bilibili.com/171431343/)、[cigar666](https://space.bilibili.com/66806831/)、[有一种悲伤叫颓废](https://space.bilibili.com/387821788/)、[pdcxs](https://space.bilibili.com/10707223/video)……可以看看他们的视频以及专栏教程。也可以结合着看看他们的github视频源码:[鹤翔万里](https://github.com/Tony031218/manim-projects)、[cigar666](https://github.com/cigar666/my_manim_projects)、[有一种悲伤叫颓废](https://github.com/136108Haumea/my-manim)、[pdcxs](https://github.com/pdcxs/ManimProjects)……

另外是[中文文档](https://github.com/cai-hust/manim-tutorial-CN)，基本的东西都包含了。当然，更上一层楼还得靠读源码。

---

## 关于这个网站
我是一个高中生，根据我国相关法律规定，未成年无法获得域名备案，且`1C2G`的学生云服务器跑`manim`实在有些捉襟见肘，倒不如废物利用。于是就用了家里的旧电脑。
```
CPU: Pentium(R) Dual-Core E5300@2.60GHz (2C2T)
内存: 4G
系统: Ubuntu 18.04 LTS 64bit
软件环境: Python3.6.9 | Manim | Nginx | PHP | TeX Live 2017 Full Version
```
电脑使用[Sakura Frp](https://www.natfrp.com/)进行内网穿透，从日本东京的节点走一遭。域名是免费域名，可以直接注册(我已经把manim的全部免费域名都抢注了哈哈哈)，然后挂到阿里云DNS解析。所以并不能保证网站稳定...

项目中的[manim](https://github.com/flwfdd/ManimOnline/tree/master/manim)文件夹就是网站的根目录，另外[tool](https://github.com/flwfdd/ManimOnline/tree/master/tool)中是生成一些东西的脚本，关于他们的具体介绍你可以进入这两个文件夹查看。能力有限，代码很丑，还请谅解。

## 开发历程
ManimOnline出现了！多线程写的并不完全，现在还是只能单线程运行。@2020-2-22 2:51

增加了多线程@2020-2-22 13:14

修复了后台孙子进程杀不干净的bug，配置了manim.ml域名。@2020-3-2 18:02

添加了转gif的功能，发现内网穿透非80端口会很卡，就改成了`nginx`反向代理。把项目上传到了github。@20200304 21:02

搞了个manim.online的域名 @20200310 21:21

改为了`POST`，可以支持长代码的提交。@20200526
