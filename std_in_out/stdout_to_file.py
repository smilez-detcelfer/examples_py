import sys
import subprocess

p = subprocess.Popen(['ping', '1.1.1.1', '-t'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)

while True:
    line = p.stdout.readline()
    if not line:
        break
    with open('log.txt', 'a') as sys.stdout:
        print(f'string: {line.rstrip().decode()}')

# or just python script.py > log