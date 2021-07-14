# Active Information Gathering

## DNS Enumeration

[OneForAll](https://github.com/shmilylty/OneForAll)


## Port Scanning

### Netcat

1. TCP Scanning

- `w` connection timeout in seconds
- `z` zero-I/O mode, send no data, used for scanning

tips:

> netcat 默认不显示连接状态, 所以需要 -v 参数, 但是连接信息是通过`标准错误输出`打印的, 所以如果仅想看开放的端口信息, 需要做下重定向

```bash
nc -nvv -w 1 -z ip port-range 2>&1 | grep open
```

2. UDP Scanning

- `u` udp mode

```bash
nc -nvv -w 1 -u -z ip port-range 2>&1 | grep open
```

但是实际使用下来, 端口开启与否的判定有问题, 抓包也并没有发现 `ICMP port unreachable` 的包

nmap扫描同样没有 `ICMP port unreachable`, 但是可以准确判定, // TODO: 挖坑

### Nmap

1. Stealth / SYN Scanning

the default scan technique

SYN scanning is a TCP port scanning method that involves sending SYN packets to various ports
on a target machine without completing a TCP handshake

```bash
sudo nmap -sS target_ip
```

tips:

> Please note that term “stealth” refers to the fact that, in the past, primitive
firewalls would fail to log incomplete TCP connections. This is no longer the case
with modern firewalls and even if the stealth moniker has stuck around, it could
be misleading.

2. TCP Connect Scanning

if does not have raw socket privileges, nmap will default to the tcp connect scan (berkeley socket)

```bash
nmap -sT target_ip
```

3. UDP Scanning

raw socket required

```bash
sudo nmap -sU target_ip
```

tips:

UDP scan(-sU) can be used in conjunction with TCP SYN scan (-sS)

```bash
sudo nmap -sS -sU target_ip
```

4. Network Sweeping

`-oG` greppable output
`-sn` ping scan, disable port scan

```bash
nmap -sn tartget_ips
```

`-A` OS detection, script scanning, traceroute
`--top-ports` top list, use the `/usr/share/nmap/nmap-services` file

```bash
nmap -sT -A --top-ports=20 target_ips
```

5. OS Fingerprinting

`-O` OS fingerprinting

```bash
sudo nmap -O target_ip
```

6. Banner Grabbing/Service Enumeration

`-sV` Probe open ports to determine service/version info
`-A` Enable OS detection, version detection, script scanning, and traceroute

```bash
nmap -sV -ST -A target_ip
```

tips:

> Keep in mind that banners can be modified by system administrators. As such, these can be
intentionally set to fake service names in order to mislead a potential attacker.

7. Nmap Scripting Engine (NSE)

`--script` to use scripts located in `/usr/share/nmap/scripts`

```bash
nmap --script=smb-os-discovery target_ip
nmap --script=dns-zone-transfer target_domain
nmap --script-help script_name
```

### Masscan

> Since masscan implements a custom TCP/IP stack, it will require access to raw sockets and therefore requires sudo.

```bash
masscan -p 80 sub_net --rate=1000 -e eth0 --router-ip router_ip
```