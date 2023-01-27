import sys
import subprocess
import datetime

p = subprocess.Popen(['ping', '1.1.1.1'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)

while True:
    line = p.stdout.readline() #read string
    ts = datetime.datetime.now()
    if not line:
        break
    with open('log.txt', 'a') as sys.stdout: # write string to file (append)
        print(f'{ts} || {line.rstrip().decode()}')
        
