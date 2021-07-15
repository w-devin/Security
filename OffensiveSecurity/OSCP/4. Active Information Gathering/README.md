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

## SMB Enumeration

1. Scanning for the NetBIOS Service

```bash
nmap -v -p 139,445 target_ips

# -r to specify the originating UDP port as 137
nbtscan -r target_sub_net
```

2. Nmap SMB NSE Scripts

list smb scripts

```bash
(base) root@kali:/home/jarvis# ls -l /usr/share/nmap/scripts/smb*
-rw-r--r-- 1 root root  3355 Oct 12  2020 /usr/share/nmap/scripts/smb2-capabilities.nse
-rw-r--r-- 1 root root  3075 Oct 12  2020 /usr/share/nmap/scripts/smb2-security-mode.nse
-rw-r--r-- 1 root root  1447 Oct 12  2020 /usr/share/nmap/scripts/smb2-time.nse
-rw-r--r-- 1 root root  5238 Oct 12  2020 /usr/share/nmap/scripts/smb2-vuln-uptime.nse
-rw-r--r-- 1 root root 45138 Oct 12  2020 /usr/share/nmap/scripts/smb-brute.nse
-rw-r--r-- 1 root root  5289 Oct 12  2020 /usr/share/nmap/scripts/smb-double-pulsar-backdoor.nse
-rw-r--r-- 1 root root  4840 Oct 12  2020 /usr/share/nmap/scripts/smb-enum-domains.nse
-rw-r--r-- 1 root root  5971 Oct 12  2020 /usr/share/nmap/scripts/smb-enum-groups.nse
-rw-r--r-- 1 root root  8043 Oct 12  2020 /usr/share/nmap/scripts/smb-enum-processes.nse
-rw-r--r-- 1 root root 27274 Oct 12  2020 /usr/share/nmap/scripts/smb-enum-services.nse
-rw-r--r-- 1 root root 12097 Oct 12  2020 /usr/share/nmap/scripts/smb-enum-sessions.nse
-rw-r--r-- 1 root root  6923 Oct 12  2020 /usr/share/nmap/scripts/smb-enum-shares.nse
-rw-r--r-- 1 root root 12527 Oct 12  2020 /usr/share/nmap/scripts/smb-enum-users.nse
-rw-r--r-- 1 root root  1706 Oct 12  2020 /usr/share/nmap/scripts/smb-flood.nse
-rw-r--r-- 1 root root  7471 Oct 12  2020 /usr/share/nmap/scripts/smb-ls.nse
-rw-r--r-- 1 root root  8758 Oct 12  2020 /usr/share/nmap/scripts/smb-mbenum.nse
-rw-r--r-- 1 root root  8220 Oct 12  2020 /usr/share/nmap/scripts/smb-os-discovery.nse
-rw-r--r-- 1 root root  4982 Oct 12  2020 /usr/share/nmap/scripts/smb-print-text.nse
-rw-r--r-- 1 root root  1831 Oct 12  2020 /usr/share/nmap/scripts/smb-protocols.nse
-rw-r--r-- 1 root root 63596 Oct 12  2020 /usr/share/nmap/scripts/smb-psexec.nse
-rw-r--r-- 1 root root  5190 Oct 12  2020 /usr/share/nmap/scripts/smb-security-mode.nse
-rw-r--r-- 1 root root  2424 Oct 12  2020 /usr/share/nmap/scripts/smb-server-stats.nse
-rw-r--r-- 1 root root 14159 Oct 12  2020 /usr/share/nmap/scripts/smb-system-info.nse
-rw-r--r-- 1 root root  7524 Oct 12  2020 /usr/share/nmap/scripts/smb-vuln-conficker.nse
-rw-r--r-- 1 root root  6402 Oct 12  2020 /usr/share/nmap/scripts/smb-vuln-cve2009-3103.nse
-rw-r--r-- 1 root root 23154 Oct 12  2020 /usr/share/nmap/scripts/smb-vuln-cve-2017-7494.nse
-rw-r--r-- 1 root root  6545 Oct 12  2020 /usr/share/nmap/scripts/smb-vuln-ms06-025.nse
-rw-r--r-- 1 root root  5386 Oct 12  2020 /usr/share/nmap/scripts/smb-vuln-ms07-029.nse
-rw-r--r-- 1 root root  5688 Oct 12  2020 /usr/share/nmap/scripts/smb-vuln-ms08-067.nse
-rw-r--r-- 1 root root  5647 Oct 12  2020 /usr/share/nmap/scripts/smb-vuln-ms10-054.nse
-rw-r--r-- 1 root root  7214 Oct 12  2020 /usr/share/nmap/scripts/smb-vuln-ms10-061.nse
-rw-r--r-- 1 root root  7344 Oct 12  2020 /usr/share/nmap/scripts/smb-vuln-ms17-010.nse
-rw-r--r-- 1 root root  4400 Oct 12  2020 /usr/share/nmap/scripts/smb-vuln-regsvc-dos.nse
-rw-r--r-- 1 root root  6586 Oct 12  2020 /usr/share/nmap/scripts/smb-vuln-webexec.nse
-rw-r--r-- 1 root root  5084 Oct 12  2020 /usr/share/nmap/scripts/smb-webexec-exploit.nse
```

use them

```bash
nmap -v -p 139,445 --script=smb-os-discovery.nse target_ips
```

## NFS Enumeration

1. Scanning for NFS Shares

```bash
nmap -v -p 111 target_ips

nmap -sV -p 111 --script=rpcinfo target_ips
```

## SMTP Enumeration

`VRFY` request asks the server to verify an email address
`EXPN` asks the server for the membership of a mailing list

## SNMP Enumeration

1. scanning for SNMP

```bash
sudo nmap -sU --open -p 161 target_ips
echo public > community
echo private >> community
echo manager >> community
for ip in $(seq 1 254); do echo 10.11.1.$ip; done > ips
onesixtyone -c community -i ips
```

2. Windows SNMP Enumeration

Windows SNMP MIB values

| MIB   | desc  |
| :---: | :---: |
| 1.3.6.1.2.1.25.1.6.0      | System Processes  |
| 1.3.6.1.2.1.25.4.2.1.2    | Running Programs  |
| 1.3.6.1.2.1.25.4.2.1.4    | Processes Path    |
| 1.3.6.1.2.1.25.2.3.1.4    | Storage Units     |
| 1.3.6.1.2.1.25.6.3.1.2    | Software Name     |
| 1.3.6.1.4.1.77.1.2.25     | User Accounts     |
| 1.3.6.1.2.1.6.13.1.3      | TCP Local Ports   |

```bash
# enumerating the Entire MIB Tree
snmpwalk -c public -v1 -t 10 target_ips

# Enumerating something
snmpwalk -c public -v1 target_ip MIB_something_value
```
