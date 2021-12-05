# [Recon-ng](https://github.com/lanmaster53/recon-ng)

## install & init

新版本的 recon-ng 需要自行安装module

```bash
marketplace install all

# 如果报： Invalid module path. 需要执行一下 

marketplace refresh
```

## use

```bash
# search modules on marketplace
marketplace search xxxx

# install modules from marketplace
marketplace install <module name>

# use module
modules load <module name>

# if the module require a key
## 1. show keys
keys list

## 2. add the key
keys add <key_name> <key_value>

## 3. reload the module if the module is loaded
reload

# show options
options list

# set option
options set <key name> <key value>

# run the module
run
```

## dev

1. recon-ng 会存储一些数据到 `~/.recon-ng/`, 有marketplace的信息， 下载的 modules和数据库文件
2. 开发过程中， 可以使用 `modules reload` 和 `reload` 来 reload 全部modules和当前module
3. 信息收集的信息分类和可维护性， 扩展性都不错

## reference

1. [github](https://github.com/lanmaster53/recon-ng)
2. [recon-ng详细使用教程](https://www.codenong.com/cs105955435/)

