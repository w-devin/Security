# DNS

## 协议概况

### DNS, Domain Name System. host name to ip.

1. host aliasing/canonical hostname
2. mail server aliasing
3. load distribution




### 最简情况下的 DNS 系统:

```
                 Local Host                        |  Foreign
                                                   |
    +---------+               +----------+         |  +--------+
    |         | user queries  |          |queries  |  |        |
    |  User   |-------------->|          |---------|->|Foreign |
    | Program |               | Resolver |         |  |  Name  |
    |         |<--------------|          |<--------|--| Server |
    |         | user responses|          |responses|  |        |
    +---------+               +----------+         |  +--------+
                                |     A            |
                cache additions |     | references |
                                V     |            |
                              +----------+         |
                              |  cache   |         |
                              +----------+         |                              
```

### Glossary

1. RRs, Resource records


## 传输层

DNS协议建立在UDP或TCP协议之上，客户端默认通过 UDP 协议进行通讯，但是由于广域网中不适合传输过大的 UDP 数据包，因此规定当报文长度超过了 512 字节时，应转换为使用 TCP 协议进行数据传输。

可能会出现如下的两种情况：
- 客户端认为 UDP 响应包长度可能超过 512 字节，主动使用 TCP 协议
- 客户端使用 UDP 协议发送 DNS 请求，服务端发现响应报文超过了 512 字节，在截断的 UDP 响应报文中将 TC 设置为 1 ，以通知客户端该报文已经被截断，客户端收到之后再发起一次 TCP 请求

## 应用层

### 报文格式

完整报文由五部分组成:

```
    +---------------------+
    |        Header       |
    +---------------------+
    |       Question      | the question for the name server
    +---------------------+
    |        Answer       | RRs answering the question
    +---------------------+
    |      Authority      | RRs pointing toward an authority
    +---------------------+
    |      Additional     | RRs holding additional information
    +---------------------+
```

### Header

The header contains the following fields:

```
                                    1  1  1  1  1  1
      0  1  2  3  4  5  6  7  8  9  0  1  2  3  4  5
    +--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+
    |                      ID                       |
    +--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+
    |QR|   Opcode  |AA|TC|RD|RA|   Z    |   RCODE   |  Flags
    +--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+
    |                    QDCOUNT                    |
    +--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+
    |                    ANCOUNT                    |
    +--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+
    |                    NSCOUNT                    |
    +--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+
    |                    ARCOUNT                    |
    +--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+
```





### Question

### Answer

### Authority

### Additional

## Security

```todo: https://xz.aliyun.com/t/9047```

## Q&A

## Reference

### RFC

1. [RFC-1034 DOMAIN NAMES - CONCEPTS AND FACILITIES](https://tools.ietf.org/html/rfc1034)
2. [RFC-1035 DOMAIN NAMES - IMPLEMENTATION AND SPECIFICATION](https://tools.ietf.org/html/rfc1035)
3. [RFC-1123 Requirements for Internet Hosts -- Application and Support](https://tools.ietf.org/html/rfc1123)
4. [RFC-3596 DNS Extensions to Support IP Version 6](https://tools.ietf.org/html/rfc3596)
5. [RFC-5011 Automated Updates of DNS Security (DNSSEC) Trust Anchors](https://tools.ietf.org/html/rfc5011)
6. [RFC-6376 DomainKeys Identified Mail (DKIM) Signatures](https://tools.ietf.org/html/rfc6376)
7. [RFC-6891 Extension Mechanisms for DNS (EDNS(0))](https://tools.ietf.org/html/rfc6891)
8. [RFC-7766 DNS Transport over TCP - Implementation Requirements](https://tools.ietf.org/html/rfc7766)

### Blog

1. [阮一峰 DNS 原理入门](https://www.ruanyifeng.com/blog/2016/06/dns.html)
2. [万字长文爆肝 DNS 协议！](https://network.51cto.com/art/202101/641655.htm)
3. [详解 DNS 与 CoreDNS 的实现原理](https://draveness.me/dns-coredns/)