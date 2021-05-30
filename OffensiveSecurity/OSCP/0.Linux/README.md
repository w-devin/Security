# Linux

虽然平时用linux比较多, 大概翻了一下第二章, 还是有些收获的. 毕竟之前linux学的比较潦草. 这里只记录一点之前疏忽的地方

## Linux Filesystem

- /bin - basic programs (ls, cd, cat, etc.) 
- /sbin - system programs (fdisk, mkfs, sysctl, etc) 
- /etc - configuration files 
- /tmp - temporary files (typically deleted on boot) 
- /usr/bin - applications (apt, ncat, nmap, etc.) 
- /usr/share - application support and data files


之前对于这几个bin目录没有很明确的区分


## Basic Linux Commands

### man

1. 粗略搜索

```
(base) root@kali:/etc# man -k passwd
chgpasswd (8)        - update group passwords in batch mode
chpasswd (8)         - update passwords in batch mode
gpasswd (1)          - administer /etc/group and /etc/gshadow
htpasswd (1)         - Manage user files for basic authentication
asswd (1)           - change user password
passwd (1ssl)        - compute password hashes
passwd (5)           - the password file
...
```

2. 正则搜索

```
(base) root@kali:/etc# man -k '^passwd$'
passwd (1)           - change user password
passwd (1ssl)        - compute password hashes
passwd (5)           - the password file
```

3. 若搜索结果不唯一, 添加搜索结果括号中的内容来区分

```
(base) root@kali:/etc# man 5 passwd
```

### apropos

等价于 `man -k`

### ss

> ss is used to dump socket statistics. It allows showing information similar to netstat.  It can display more TCP and state information than other tools.


## Finding Files in Linux

### which

搜索 `$PATH` 中的目录

### locate

1. 搜索自维护的数据库 `locate.db` 而不是磁盘文件搜索, 所以系统上的新文件可能搜索不到
2. 数据库会定时自动更新, 若要手动更新, 执行 `updatedb`

### find

> The main advantage of find over locate is that it can search for files and directories by more than just the name. With find, we can search by file age, size, owner, file type, timestamp, permissions, and more.

- `name` find file by name
- `atime` access time
- `mtime` modify time
- `ctime` change time

```bash
# find php files modified in 24 hours
find ./ -name '*.php' -mtime 0

# find php files modified in 24~48 hours
find ./ -name '*.php' -mtime 1

# find php files modified in 7 days
find ./ -name '*.php' -mtime -7

# find php files modified out 7 days
find ./ -name '*.php' -mtime +7

# time +- n, may not correct
```


## Managing Linux Services

### apt/apt-get

1. `apt search` vs `apt show`

- apt-cache: search looks for the requested keyword in the package’s description rather than the package name itself.
- apt show: the resource-agents package description really contains the “pure-ftpd” keyword,

### dpkg

dpkg is the core tool used to install a package, either directly or indirectly through APT

1. use

```bash
dpkg -i xxxxxx.deb
```

## Command Line Fun

### Bash Environment

1. $PATH
2. $USER
3. $PWD
4. $HOME
5. $$: the process ID of the current shell

> export: makes the variable accessible to any subprocesses
> use `env` to view environment variables defined by system

### piping `|` and redirection `<` `>`

1. STDIN 0, STDOUT 1, STDERR 2

### Text Searching and Manipulation

1. grep

- `r` recursive searching
- `i` ignore text case
- `n` line number
- `s` no error messages
- `v` invert match

2. sed

https://www.gnu.org/software/sed/manual/sed.html

```bash
sed 's/hard/harder/'  # replace
```

3. cut

cut can only accept a single character as field delimiter

- `b` select only these bytes

```bash
(base) [root@jarvis ~]# echo 'this is my password, bro.' | cut -b 3
i

(base) [root@jarvis ~]# echo 'this is my password, bro.' | cut -b 3-5,10
is y

(base) [root@jarvis ~]# echo 'this is my password, bro.' | cut -b -3
thi
(base) [root@jarvis ~]# echo 'this is my password, bro.' | cut -b 10-
y password, bro.

```

- `n` with `-b` do not split multibyte character

```bash
(base) [root@jarvis ~]# echo '你好, 你也要日卫星嘛?' | cut -b 5
¥
(base) [root@jarvis ~]# echo '你好, 你也要日卫星嘛?' | cut -nb 5
你
```


- `c` select only these characters

```bash
(base) [root@jarvis ~]# echo 'this is my password, bro.' | cut -c 3
i
(base) [root@jarvis ~]# echo 'this is my password, bro.' | cut -c 3-5,10
is y
(base) [root@jarvis ~]# echo 'this is my password, bro.' | cut -c -3
thi
(base) [root@jarvis ~]# echo 'this is my password, bro.' | cut -c 10-
y password, bro.
```

- `f` select only these fields
- `d` use DELM instead of TAB for field delimiter

```bash
(base) [root@jarvis ~]# echo 'this is my password, bro.' | cut -d ' ' -f 1
this
(base) [root@jarvis ~]# echo 'this is my password, bro.' | cut -d ' ' -f 2-4
is my password,
(base) [root@jarvis ~]# echo 'this is my password, bro.' | cut -d ' ' -f -3
this is my
(base) [root@jarvis ~]# echo 'this is my password, bro.' | cut -d ' ' -f 3-
my password, bro.
```

4. awk

sample use:

```bash
(base) [root@jarvis ~]# echo 'hello, world. this is my password, bro.' | awk '{print $1, $3}'
hello, this
(base) [root@jarvis ~]# echo 'hello, world. this is my password, bro.' | awk -F ' ' '{print $1, $3}'
hello, this
(base) [root@jarvis ~]# echo 'hello, world. this is my password, bro.' | awk -F ',' '{print $1, $3}'
hello  bro.
```

5. parctical

```bash
(base) [root@jarvis OSCP]# head secure -n 200 | grep "Failed password" | grep "invalid user" | awk -F ' ' '{print $13, $11}' | sort -n
39.96.137.159 git
39.96.137.159 hadoop
39.96.137.159 oracle
39.96.137.159 oracle
39.96.137.159 postgres
117.132.2.75 basic
117.132.2.75 centos
117.132.2.75 db2inst3
117.132.2.75 invite
117.132.2.75 java
117.132.2.75 logan
117.132.2.75 matthew
117.132.2.75 research
117.132.2.75 tech
117.132.2.75 tyler
117.132.2.75 tyler
```

6. exercises

```bash
cat /etc/passwd |sed 's/Gnome Display Manager/GDM/'| awk -F ':' '$6 !~ "/bin/false" {printf "The user %s home directory is %s\n",$1,$6}'
```

### Editing Files from the Command Line

1. nano
2. vim

### Comparing Files

1. comm

```bash

# 比较两个文件, 显示有三列, 第一个文件独有的, 第二个文件独有的, 两个文件共有的
comm scan-a.txt scan-b.txt

# 比较两个文件, -n 不显示某一列, 取值 [1, 2, 3]
comm scan-a.txt scan-b.txt -12
```

2. diff

- `c` context format
- `u` unified format

```bash
(base) [root@jarvis OSCP]# diff -c scan-a.txt scan-b.txt 
*** scan-a.txt	2021-05-31 01:30:16.469692438 +0800
--- scan-b.txt	2021-05-31 01:30:26.798074746 +0800
***************
*** 1,5 ****
  192.168.1.1 
- 192.168.1.2
  192.168.1.3 
! 192.168.1.4
  192.168.1.5
--- 1,5 ----
  192.168.1.1 
  192.168.1.3 
! 192.168.1.4 
  192.168.1.5
+ 192.168.1.6
(base) [root@jarvis OSCP]# diff -u scan-a.txt scan-b.txt 
--- scan-a.txt	2021-05-31 01:30:16.469692438 +0800
+++ scan-b.txt	2021-05-31 01:30:26.798074746 +0800
@@ -1,5 +1,5 @@
 192.168.1.1 
-192.168.1.2
 192.168.1.3 
-192.168.1.4
+192.168.1.4 
 192.168.1.5
+192.168.1.6
```

'-' show that the line appears in the first file, but not in the second
'+' shows that the line appears in the second file, but not in the first
'!' unknow

3. vimdiff

- `do` get changes from the other window into the current one
- `dp` put the changes from the current window into the other one
- `]c` jumps to the next change
- `[c` jumps to the previous change
- `Ctrl-W` switches to the other split window

### Managing Processes

1. Backgrounding Processes(bg)

- background a process

```bash
command &

Ctrl-c # cancel
Ctrl-z # suspend job

bg     # resume process in the background
```

2. jobs control: jobs and fg

```bash
(base) [root@jarvis OSCP]# jobs
[1]+  Stopped                 vim scan-b.txt
(base) [root@jarvis OSCP]# fg %1
vim scan-b.txt

```

about fg:

- `%Number` refers to a job number
- `%string` refers to the beginning of the suspended command's name
- `%+ or %%` refers to the current job
- `%-` refers to the previous job

3. Process Control: ps and kill

```bash
ps aux

# same as 
ps -ef

# select by command name

ps -fC bash

# select by command name and kill them by PID
ps -fC leafpad | awk '$2 ~ "^[0-9]+$" {print $2}' | xargs kill -9
```

### File and Command Monitoring

1. tail

# TODO: continue


























