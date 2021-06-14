# Passive Information Gathering

*also know as Open-source Intelligence or OSINT*

passive:
    - never communicate with the target directly
    - might interact with the target, but only as a normal internet user would

## whois

```bash
# get basic information about a domain name
whois domain

# reverse lookup
whois ip
```

## Google Hacking

[Google Hacking for Penetration Testers](https://www.researchgate.net/publication/319621156_Google_Hacking_for_Penetration_Testers_Third_Edition_3rd_Edition)
[google-hacking-database](https://www.exploit-db.com/google-hacking-database)

- `site` limits searches to a single domain
- `filetype` limits search results to the specified file type
- `ext` discern what programming languages might be used on a web site
- `-` exclude operator
- `intitle` to find pages that contain parm in the title
- `"xxxx"` to find pages that contain param on the page

## Netcraft

www.netcraft.com

## Recon-ng

新版的 Recon-ng, 打开会提醒 '[*] No modules enabled/installed.', 此时可以通过在 Recon-ng 的 shell中执行 `marketplace install all` 来安装 modules, 当然最好是按需安装, 全安装的话, 很多模块会报key的缺失

> 安装源是github, 所以如果安装失败的话, 需要一点技术手段来解决
> 如果还不行的话, 可以尝试执行：
>> rm -fr ~/.recon-ng && git clone https://github.com/lanmaster53/recon-ng-marketplace.git ~/.recon-ng
> 
> 也就是说, 从git/码云等平台上的 marketplace 仓库放到 ~/.recon-ng 目录下就可以了

```bash
# search modules from marketplace
marketplace search keyword

# more about a module
marketplace info module

# install module
marketplace insatll module

# if module need key
keys add <name> <value>

# load module
modules load module

# next in module shell
set options <option-key> <option-value>

# run
run

# Recon-ng stores results in a local databases and these results will feed into other recon-ng modules
# use `show` to list this results
show hosts

# 模块所需参数如果取值 'default', 模块会自动从database中取合适的值作为输入
```

tips:
1. 有些 module 需要各种api key, 如何设置可以参考 [这里](https://github.com/Raikia/Recon-NG-API-Key-Creation/blob/master/README-v4.8.3.md)
2. OSCP 中, 提到使用 google_site_web, 但是由于众所周知的原因, 国内无法使用; 除此之外, google 也有难以绕过的 recaptcha: `google recaptcha triggered. no bypass available.`, 所以推荐 bing_domain_web
