import random
n = 1
sum = 0
while n != 0:
    cache = random.randint(0,1)
    sum = sum + cache
    if n % 500 == 0:
        result = float(100 * (sum / n))
        print("第%s次实验所得抛硬币正面向上概率为：%.5f%%" % (n,result))
    n = n + 1
