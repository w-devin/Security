# Web Application Attacks

## Web Application Enumeration

- Programming language and frameworks
- Web server software
- Database software
- Server operating system

## Web Application Assessment Tools

1. dirb

- `r` scan no-recursively
- `z` to add N millisecond delay to each request

```bash
dirb url -r -z 10
```

tips:
> DirBuster is a Java application similar to DIRB that offers multi-threading and a GUI-based interface.

2. BurpSuite

proxy tools

- Firefox: FoxyProxy
- Chrome: SwitchyOmega

3. Nikto

- `maxtime` scan time limit
- `T` tune the scan
- `host` host

```bash
nikto -host=url -maxtime=30s
```
