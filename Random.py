import random

lis = []

for i in range(10):
    random_num = int(random.randint(1, 1000))
    lis.append(random_num)
    print(lis[i])
print(lis)