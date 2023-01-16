import time
import sys
if __name__ == "__main__":
    if len(sys.argv) == 1:
        count = 100
    else:
        count = int(sys.argv[1])


for c in range(count):
    print(f'count = {c}')
    time.sleep(1)

