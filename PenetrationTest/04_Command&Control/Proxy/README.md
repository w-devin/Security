# 代理/端口转发

## 工具

### HTran

应该是由 cnhonker 的一伙人开发的, 最初是用C写的 Windows 版本, 后来内部做了 linux 适配版, [项目地址](https://github.com/HiwinCN/HTran)

后来由 [bGn4](https://github.com/bGN4) 做了多平台适配版, [项目地址](https://github.com/bGN4/HTran)

#### usage

```cmd
(base) PS D:\Projects\socket_client\Debug> .\socket_client.exe
======================== HUC Packet Transmit Tool V1.00 =======================
=========== Code by lion & bkbll, Welcome to http://www.cnhonker.com ==========

[Usage of Packet Transmit:]
 D:\Projects\socket_client\Debug\socket_client.exe -<listen|tran|slave> <option> [-log logfile]

[option:]
 -listen <ConnectPort> <TransmitPort>
 -tran   <ConnectPort> <TransmitHost> <TransmitPort>
 -slave <ConnectHost> <ConnectPort> <TransmitHost> <TransmitPort>
```

支持三种转发方式, 分别是 端口转端口(listen), 端口转连接(tran), 连接转连接(slave)

核心转发代码在 transmitdata 方法, 在 slave 模式下, 由 bkbll 做了连接方式的改进, 在接收端接收到数据后, 再向目标发起连接

简单干净的GO版本, [项目地址](https://github.com/cw1997/NATBypass)

### LCX

这个工具很奇怪, 感觉像是 HTran 的初始版本, 瑕疵, 代码结构都不是很好, 即使是它的[优化版](https://github.com/UndefinedIdentifier/LCX)

emmmmm, 代码看的一言难尽

使用可参考: [红队技能：Hash读取与端口转发](https://mp.weixin.qq.com/s/tXRGfiinPkOOVpQ1n7z1-g)

### netcat

### socat
3
1. [Socat 入门教程](https://www.hi-linux.com/posts/61543.html)

### [powercat](https://github.com/besimorhino/powercat)


1. [工具之powercat使用教程](https://blog.csdn.net/qq_32393893/article/details/108904697)

## TODO

1. [内网渗透-代理篇](https://mp.weixin.qq.com/s/mjie7AnPvnW0jRaEnkdddQ)
2. [内网穿透姿势汇总](https://mp.weixin.qq.com/s/Syf0vQfElk5JERnoycKSsw)
3. [MSF配合Ngrock穿透内网](https://mp.weixin.qq.com/s/g0iuHpiuuUN2AOQAkMcJ2Q)
4. [内网隧道工具SPP尝鲜](https://mp.weixin.qq.com/s/zY9T-t86Dpw07SecABPuug)
5. [利用 ssh 隧道反弹 shell](https://paper.seebug.org/1022/)