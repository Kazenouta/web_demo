import subprocess, os

PORT = 8080

PROJECT_BASE = subprocess.getoutput('pwd')
PROJECT_NGINX_CONF = os.path.join(PROJECT_BASE, 'conf/nginx.conf')
NGINX_CONF = '/etc/nginx/conf.d/nginx.conf'