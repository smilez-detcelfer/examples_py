import subprocess
reply = subprocess.run(['nc', '51.250.85.161', '18668', '<', 'cow'], stdout=subprocess.PIPE)

print(reply.stdout)