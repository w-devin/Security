# linux 提权

## 必要信息收集

### 常用命令

```bash
# 1. 查看内核版本
uname -a

# 2. 查看系统发行版本
cat /etc/issue
cat /etc/*-release

# 3. 查看进程信息
ps -aux
netstat

# 4. 查看安装的软件
dpkg -l
rpm -qa

# 5. 其他
磁盘, 杀软 等
```

### 信息收集工具

1. linux exploit suggester

## 提权

### 漏洞提权

1. CVE-2018-18955
2. 脏牛

### suid 提权

执行者对文件有执行权限, 执行者有文件所属者的权限

常见文件: nmap, vim, find, bash, more, less

```bash
# 搜索有suid的文件
find / -perm -u=s -type f 2>/dev/null
```

### sudo 提权

影响范围: 1.8.28 之前的 sudo 版本

可以使用 `sudo -u#-1` 使用root用户执行命令


## reference

1. [gtfobins](https://gtfobins.github.io)
