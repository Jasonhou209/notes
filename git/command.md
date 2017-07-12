# git常用命令
1. 配置本机的用户名和email地址
```
$ git config --global user.name "Your Name"
$ git config --global user.email "email@example.com"
```
2. 创建并初始化仓库
```
$ cd C:/git-repositories
$ mkdir new_repository_1           创建新的目录
$ cd new_repository_1              进入到创建的目录
$ git init
Initialized empty Git repository in C:/git-repositories/new_repository_1/.git/
(显示信息意思为：初始化了一个空的Git仓库，new_repository_1目录下多了一个.git目录，时用来管理版本库的)
```
3. 添加文件
```
$ git add .        添加所有的文件、文件夹
$ git add <file>   添加指定名称的文件,<>内部写文件全称
```
4. 提交文件
```
$ git commit –m “commit info”      提交本次事务，即将add的文件提交到git仓库，引号内部表示本次提交的提示信息
```
5. 查询状态
```
$ git status       显示提交的状态：已经添加，等待提交事务的文件(绿色字体表示)；已经改变但是没有添加(not staged)的文件(红色字体表示)；
```
6. 查询不同
```
$ git diff <文件全称>      如果已经add了，就打印不出有什么修改了，这一步骤应该在add之前，即添加之前可以用来看看做了什么修改。
```
7. 打印历史记录
```
$ git log
Commit xxx               commit id 版本号
Author:xxx<xxx@xxx.com>  提交人和邮箱
Date：xxx                提交的时间
    XXXXXXXXXXXXXX       提交的信息(所以说，提交信息很重要！！！)
$ cat <文件全名称>        显示整个文件的内容
```
8. 提交服务器
```
$ git push
```
