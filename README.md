# 使用教程

- 打开`main.py`把api改成自己的代理api，记得添加白名单，数量设置为1。

- 将项目拷贝到服务器

- 请确保安装`docker`，cd 到项目路径

- ```cmd
  docker build -t myProxy:v1.0.0 .
  ```

- ```cmd
  docker run -d -p 5555:5555 --restart always -e TZ=Asia/Shanghai --name myProxy myProxy:v1.0.0
  ```
