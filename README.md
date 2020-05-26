# web_demo

### 使用方法
#### 1. 克隆项目/安装Python模块
* git clone https://github.com/Kazenouta/web_demo.git 
* cd web_demo
* pip3 install -r requirements.txt

#### 2. 填写配置项
* 在 *conf/nginx.conf* 文件中配置IP(或域名)和Nginx要映射的端口(默认8080)
* 在 *cmd/config.py* 文件中配置Gunicorn服务的端口(默认8080), 需跟Nginx配置文件中的端口一致

#### 3. 启动各项服务
* python3 main.py                 # 启动 Flask (用于开发调试) 
* python3 cmd/start.py start-gunicorn  # 启动 Gunicorn
* python3 cmd/start.py start-nginx  # 启动 Nginx
* python3 cmd/start.py start-all  # 启动 Nginx + Gunicorn