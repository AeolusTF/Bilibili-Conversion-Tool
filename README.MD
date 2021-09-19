# Bilibili-Conversion-Tool

## 简介
作为B站资深用户，某一天突然发现一个问题，手机上从B站App缓存下来的视频只能在B站App上看，但考虑到手机上下载比较方便，于是干脆从手机上批量下载，再搬到电脑上处理，于是写了这个程序。

## 环境

```
Windows10 + python3 + ffmpeg
```
***

## 使用

此处已Android为例，B站的缓存文件一般存放在 \Android\data\tv.danmaku.bili\download 这样的路径下，照着这个路径应该就能找到，然后连跟数据线，直接把download里面所有文件搬到电脑上。

![image](/images/20210920041247.png)

每一个文件夹下面是相应种类视频的分p：

![image](/images/20210920042336.png)

现有的缓存文件看起来有些混乱，得整理一下：
里面文件存放的方式居然有两种，一种是比较新的：

![image](/images/20210920042447.png)

还有一种比较老的：

![image](/images/20210920041826.png)

新的把音视频分开了，最里面的video.m4s 和 audio.m4s两个文件就是我要的 ，看样子要把两个文件混流才行，而老的却是把视频分段了，直接拼起来就行了。

最简单粗暴的操作，考虑到格式工厂之类的音视频编辑软件，但是后缀名不对还识别不了，而且那么多的文件，一个个去操作实在愚蠢，于是考虑写个程序，让它自动去跑。

这里使用的环境为windows10+python3.8，要实现这样的功能，python有一个现成的轮子，叫moviepy，不过这个库有许多问题，而且在拼接的时候速度极为缓慢，于是干脆直接用ffmpeg

没有ffmpeg的，直接去官网下载，或者打开 powershell，输入以下命令安装：

```
choco install ffmpeg
```

提示没有choco命令的，打开 powershell 复制以下命令安装choco，再安装ffmpeg：

```
Set-ExecutionPolicy Bypass -Scope Process -Force; [System.Net.ServicePointManager]::SecurityProtocol = [System.Net.ServicePointManager]::SecurityProtocol -bor 3072; iex ((New-Object System.Net.WebClient).DownloadString('https://chocolatey.org/install.ps1'))
```

### 根据上述新、老识别方法，老的使用：

```
python3 Bilibili-Conversion-Old.py
```
![image](/images/20210920041623.png)

![image](/images/20210920042025.png)

### 新的使用：
```
python3 Bilibili-Conversion-New.py
```
![image](/images/20210920050131.png)

![image](/images/20210920052647.png)

### 重点：在使用前，无论新、老，请修改源码中的路径！！！

![image](/images/20210920045026.png)


***
## *PS：*
*老视频只是拼接一下，速度会非常的快，而新的视频需要音视频混流，所以速度比较慢，视电脑配置而定，要加快速度的话，可以考虑使用多线程。*
