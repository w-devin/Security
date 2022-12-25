# 域控安全

虽然目录定名是域渗透, 准确来说应该是windows内网渗透, 涉及的东西比较多, 列个list慢慢更吧

## 内网基础

### 工作组, 域概念

### windows hash

1. NT Hash
    - MD4(UTF-16-LE(password))
2. LM Hash
    - 用户密码转为大写16进制字符串, 不足14字节, 用0填充
    - "KGS!@#$%" 作为key, 进行des加密
    - 密码最长14字符
    - 不区分大小写
    - 如果密码长度小于7, 则第二分组加密后的值一定是 "aad3b435b51404ee"
    - 分组加密, 导致密码被破解的难度降低
    - des密码强度不高
3. NTLM Hash
   - 本地认证: winlogin.exe -> 接收用户输入 -> lsass.exe -> 本地认证
   - 远程认证: 
     - c -> s, NTLM Hash1, version, account
     - s -> c, challenge, 16 random integer
     - c: response: ntlm(challenge)
     - s -> dc: account,challenge, response
     - dc: response2: encrypt(challenge, ntlm hash (sam(account)))
     - dc: cmp: response1, response2
4. kerberos
   - 在互不信任的网络中, 提供了可靠的中心化认证协议
   - 密码不在网络中传输, 不会存储在客户端机器上, 使用完立即删除, 明文不会存储在认证服务器(KDC)的数据库里
   - 实现单点登录
   - 角色：
     - 客户端 client
     - 服务端 server
     - 密钥分发中心 KDC, key distribution center
       - AS, Authentication server, 认证服务器
       - TGS, Ticket Granting Ticket, 票据授予服务器

## 信息收集

### 工作组信息收集


### 域信息收集

```cmd
1. 当前域名称
net view /domain

2. 查询域内所有主机
net view /domain:<域名>

3. 查询域内所有用户组
net group /domain

4. 查看域密码信息
net accounts /domain

5. 获取域信任信息
nltest /domain_trusts

6. 查询所有域成员主机全称
net group "domain computers" /domain

7. 查看域控制器组
net group "domain controllers" /domain

8. 查看域管理员用户
net group "domain admins" /domain
 
9. 查询管理员用户组
net group "enterprise admins" /domain

10. 查询域用户
net group "domain users" /domain

11. 查询用户
wmic useraccount get /all

12. 查看当前域信息
net time /domain
nslookup <domain>
ping <domain>

13. 其他工具
dsquery (only dc), user|computer|subnet|quota...
```

### 定位域管理员

1. 定位工具
    - Psloggedon
    - PVEFindADUser
    - NetView
    - Netsess: 补充 `net session` 没有权限执行的情况
    - Hunter: empire module: powershell/situational_awareness/network/powerview/user_hunter
    - PowerView, [PowerSploit](https://github.com/PowerShellMafia/PowerSploit)
    - [GDA](https://github.com/nullbind/Other-Projects/blob/master/GDA/README.txt)
    - bloodhound-


### 查找域管理进程

查找到域管理员运行的进程后, 可以把某个进程的内存 dump 出来, 搞到域管理员的hash。用于模拟域管的操作

#### 本地查询

```cmd
net group "domain admins" /domain
tasklist /v
```

#### 远程查找

```cmd
net session

# 交叉引用域管理员列表与活动会话列表
net group "domain Controllers" /domain > dcs.txt
net group "domain admins" /domain > admins.txt

for /f %i in (dcs.txt) do 
    @echo [+] Querying DC %i
    && @netsess -h %i 2 > null > sessions.txt
    && for /f %a in (admins.txt) do
        @type sessions.txt | @findstr /i %a
        
工具: GDA, nbtscan
```

## reference

1. [ms](https://docs.microsoft.com/en-us/windows-server/identity/ad-ds/active-directory-domain-services)
2. [adsecurity.org](https://adsecurity.org/)
3. [红蓝对抗之Windows内网渗透](https://security.tencent.com/index.php/blog/msg/154)
4. [WHOAMI-FreeBuf](https://www.freebuf.com/author/MrAnonymous)
5. [NTLM 基础 介绍](https://daiker.gitbook.io/windows-protocol/ntlm-pian/4)
6. [LM, NTLM, Net-NTLMv2, oh my!](https://medium.com/@petergombos/lm-ntlm-net-ntlmv2-oh-my-a9b235c58ed4)
7. [基于AD Event日志监测域内信息探测行为](https://mp.weixin.qq.com/s/IWpNZoV6-4G2kXMoMD079A)
