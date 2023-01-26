import sys
import subprocess

p = subprocess.Popen(['ping', '1.1.1.1'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
with open('log', 'w') as sys.stdout:

    while True:
        line = p.stdout.readline()
        if not line:
            break
        print(f'string: {line.rstrip().decode()}')

# or just python script.py > log