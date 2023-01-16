import subprocess

proc = subprocess.run(['ipconfig', '-all'], shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
str_out = proc.stdout.decode('windows-1252')
list_out = str_out.split('\n')
#delete elemnents like '\r' and strip all
filtered_out = list(map(lambda item: item.strip(), filter(lambda a: a!= '\r', list_out)))

for i in filtered_out:
    print(i)
