import threading
import time

def cnt(num1, num2):
    for i in range(num1, num2):
        time.sleep(1)
        print("1번")

a = threading.Thread(target=cnt, args=[0, 100])
a.daemon = True
a.start()


for i in range(300,400):
    print("2번")
    time.sleep(0.5)