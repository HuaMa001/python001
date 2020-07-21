import random

while True:
    n=random.randint(1, 100)
    # 若n 等於3的倍數就印出
    if n % 3 ==0:
        print(n)
        continue
    print(n)
    #若n 等於11 的倍數就停止
    if n % 11 ==0:
        break


