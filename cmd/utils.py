import subprocess, os

def kill_by_port(port=8080):
    cmd = f'sudo lsof -i:{port}'
    cmd += " | awk '{print $2}'"
    pids = subprocess.getoutput(cmd).split('\n')
    for pid in pids:
        try:
            os.system(f'kill {pid}')
        except:
            pass

if __name__ == '__main__':
    kill_by_port()