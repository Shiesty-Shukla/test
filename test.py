import random

x = []

for i in range(25):
    x.append(random.randint(1, 25))

sum = 0

for nums in x:
    sum += nums

print(sum)