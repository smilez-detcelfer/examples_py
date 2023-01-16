import subprocess

# stdout и stdin програмы stdin_out.py будет использоваться этой программой
p = subprocess.Popen(['ping', '1.1.1.1', '-t'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)

while True:
    output = p.stdout.readline().decode('utf-8')
    if output == '' and p.poll() is not None:
        break
    if output:
        print(output)
