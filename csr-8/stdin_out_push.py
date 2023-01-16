import subprocess

# stdout и stdin програмы stdin_out.py будет использоваться этой программой
p = subprocess.Popen(['python.exe', 'stdin_out.py'], stdout=subprocess.PIPE, stdin=subprocess.PIPE)
out, err = p.communicate(input=b"3\n5\n7\nexit") # вводятся байты
print(out.decode())
