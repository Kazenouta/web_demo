import os, sys, time
from utils import *

PROJECT_BASE = subprocess.getoutput('pwd')
PROJECT_NGINX_CONF = os.path.join(PROJECT_BASE, 'config/nginx.conf')
NGINX_CONF = '/etc/nginx/conf.d/nginx.conf'


def main():
    os.system(f'cd {PROJECT_BASE}')
    os.system('sudo rm -rf /etc/nginx/conf.d/*.conf')
    os.system(f'sudo ln -s {PROJECT_NGINX_CONF} {NGINX_CONF}')
    kill_by_port('8080')
    kill_by_port('80')

    arg = sys.argv[1]
    if arg == 'install-gunicorn':  # 安装 Gunicorn
        os.system('sudo apt-get install gunicorn3')
    elif arg == 'start-gunicorn':  # 启动 Gunicorn, 后台运行
        os.system('gunicorn3 -w4 main:app -b 0.0.0.0:8080 -D')
    elif arg == 'install-nginx':   # 安装 Nginx
        os.system('sudo apt-get remove nginx')
        os.system('sudo apt-get install nginx')
    elif arg == 'start-nginx':     # 启动 Nginx, 后台运行
        os.system('sudo /etc/init.d/nginx start')
    elif arg == 'restart-nginx':
        os.system('sudo service nginx restart')
    elif arg == 'start-flask':     # 启动 Flask, 后台运行
        os.system(f'nohup python3 ./main.py >> ./log/main.log &')
    elif arg == 'start-all':
        os.system('gunicorn3 -w4 main:app -b 0.0.0.0:8080 -D')
        os.system('sudo /etc/init.d/nginx start')
    else:
        raise Exception(f'argv: {arg} is invalid!')



if __name__ == '__main__':
    main()
