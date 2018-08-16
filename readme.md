### Windows下Scrapy框架安装
1、先到官网python下载对应版本的[Python](https://www.python.org/downloads/)并安装，我这里使用的是Python3.7

2、以管理员权限打开命令行，键入：
```
pip3 install Scrapy
```

如果以前未安装过C++编译工具，安装过程中可能会报以下错误：

```
building 'twisted.test.raiser' extension
    error: Microsoft Visual C++ 14.0 is required. Get it with "Microsoft Visual C++ Build Tools": http://landinghub.visualstudio.com/visual-cpp-build-tools

```

3、再Microsoft官网下载安装C++构建工具：[点击下载](https://www.microsoft.com/en-us/download/confirmation.aspx?id=48159)
，下载完毕点击安装即可。

4、下载Twisted并安装，[Twisted](https://www.lfd.uci.edu/~gohlke/pythonlibs/#twisted) 我的版本是Twisted‑18.7.0‑cp37‑cp37m‑win_amd64.whl。下载完成之后，进入使用命令行进入文件所在目录，键入:
```
pip install Twisted‑18.7.0‑cp37‑cp37m‑win_amd64.whl
```

5、安装完毕之后再次输入：
```
pip3 install Scrapy
```

完成安装。

6、Scrapy常用命令

```
# 创建一个项目
scrapy startproject your_project_name

# 初始化一个爬虫（spiders目录下）
scrapy genspider your_spider_file_name your_spider_name

# 运行一个爬虫（spiders目录下）
scrapy crawl your_spider_name

# 导出文件（spiders目录下）
scrapy crawl your_spider_name -o your_file_name

like:
# 导出json文件
scrapy crawl HelloWorld -o HelloWorld.json
# 导出csv文件
scrapy crawl HelloWorld -o HelloWorld.csv

```

### 使用Dockers 安装MongoDB
1、使用Docker 安装Mongo
```
// 搜索Mongo
[root@localhost ~]# docker search mongo
INDEX       NAME                                          DESCRIPTION                                     STARS     OFFICIAL   AUTOM
docker.io   docker.io/mongo                               MongoDB document databases provide high av...   4830      [OK]       
...

// 拉取官方版本的镜像
[root@localhost ~]# docker pull docker.io/mongo
Using default tag: latest
Trying to pull repository docker.io/library/mongo ... 
latest: Pulling from docker.io/library/mongo
...
Digest: sha256:232dfea36769772372e1784c2248bba53c6bdf0893d82375a3b66c09962b5af9
Status: Downloaded newer image for docker.io/mongo:latest

// 拉取成功
[root@localhost ~]# docker images
REPOSITORY                             TAG                 IMAGE ID            CREATED             SIZE
docker.io/mongo                        latest              8bf72137439e        4 days ago          380 MB

// 根据镜像生成容器
[root@localhost ~]# docker run --name myMongo -p 27017:27017 -d 8bf72137439e
04c5d3f66aa039013485c78c7329810f108d25c9ed29a214ed9c080359fb1238

// 查看状态
[root@localhost ~]# docker ps -a
CONTAINER ID        IMAGE                                  COMMAND                  CREATED             STATUS                      PORTS                                        NAMES
04c5d3f66aa0        8bf72137439e                           "docker-entrypoint..."   About an hour ago   Up About an hour            0.0.0.0:27017->27017/tcp                     myMongo
```

2、使用Mongo可视化工具：[NoSQL Manager](https://www.mongodbmanager.com/download) 连接使用即可