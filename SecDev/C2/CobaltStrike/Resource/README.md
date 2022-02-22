# Cobalt Strike魔改记录

## references

1. [wbglil cobalt-strike](https://wbglil.gitbook.io/cobalt-strike/)
2. [pediy](https://bbs.pediy.com/user-718877.htm)
3. [zer0yu/Awesome-CobaltStrike](https://github.com/zer0yu/Awesome-CobaltStrike)

## 环境准备

[CobaltStrike二开环境初探](https://www.ol4three.com/2021/11/09/%E5%86%85%E7%BD%91%E6%B8%97%E9%80%8F/CobaltStrike/CobaltStrike%E4%BA%8C%E5%BC%80%E7%8E%AF%E5%A2%83%E5%88%9D%E6%8E%A2/)

[lengjibo](https://lengjibo.github.io/CobaltStrikeCode/)

[CobaltStrike二次开发环境初探](https://blog.51cto.com/u_15274949/2931535)

## 协议解析

[CS 登陆通信流程分析](https://mp.weixin.qq.com/s?__biz=MzkxMTMxMjI2OQ==&mid=2247483923&idx=1&sn=ad34e81ac5b7313a83764c2ebfc0aac5&chksm=c11f56f1f668dfe7c4b5bc64f039b3b3dc2c8efcf4c01febd371c6be99137fea695e66bdfc9a&scene=178&cur_album_id=2174670809724747778#rd)
[[原创]魔改CobaltStrike：协议全剖析](https://bbs.pediy.com/thread-267208.htm)

## run code

### TeamServer

TeamServer 要跑起来, 需要

1. 先生成一个ssl证书

```
keytool -keystore ./cobaltstrike.store -storepass keypassword -keypass keypassword  -genkey -keyalg RSA -alias cobaltstrike -dname "CN=H@ck3r.live.com, OU=H@ck3r Corporation, O=H@ck3r Corporati    on, L=Sm1thhat, S=NewAlien, C=UK"
```

VM option 参数加上 

```
-Djavax.net.ssl.keyStore=./cobaltstrike.store
-Djavax.net.ssl.keyStorePassword=keypassword
server.TeamServer
```

2. 生成一个默认的 TeamServer.prop

```bash
#Cobalt Strike Team Server Properties
#Fri May 07 12:00:00 CDT 2021
# ------------------------------------------------
# Validation for screenshot messages from beacons
# ------------------------------------------------
# limits.screenshot_validated=true
# limits.screenshot_data_maxlen=4194304
# limits.screenshot_user_maxlen=1024
# limits.screenshot_title_maxlen=1024
# Stop writing screenshot data when Disk Usage reaches XX%
# Example: Off
#          "limits.screenshot_diskused_percent=0"
# Example: Stop writing screenshot data when Disk Usage reaches 95%
#          "limits.screenshot_diskused_percent=95"
# Default:
# limits.screenshot_diskused_percent=95
# ------------------------------------------------
# Validation for keystroke messages from beacons
# ------------------------------------------------
# limits.keystrokes_validated=true
# limits.keystrokes_data_maxlen=8192
# limits.keystrokes_user_maxlen=1024
# limits.keystrokes_title_maxlen=1024
# Stop writing keystroke data when Disk Usage reaches XX%
# Example: Off
#          "limits.keystrokes_diskused_percent=0"
# Example: Stop writing keystroke data when Disk Usage reaches 95%
#          "limits.keystrokes_diskused_percent=95"
# Default:
# limits.keystrokes_diskused_percent=95
```

3. 抄一下teamserver的启动脚本中的参数, 复制到 VM Options

```bash
-XX:ParallelGCThreads=4
-XX:+AggressiveHeap
-XX:+UseParallelGC
```