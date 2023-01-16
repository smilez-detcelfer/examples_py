import subprocess

p = subprocess.Popen(['python', 'stdout_generator.py', '5'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
while True:
    line = p.stdout.readline()
    if not line:
        break
    print(f'string: {line.rstrip().decode()}')
#p.wait() # ожидание завершения процесса
#1 change