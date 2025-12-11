import random
N = int(input('Длина массива: '))

a1 = []
a2 = []
a3 = []

for i in range(N):
    num = random.randint(1, 100)
    a1.append(num)

for i in range(N):
    num = random.randint(1, 100)
    a2.append(num)
 
for i in range(N):
    num = random.randint(1, 100)
    a3.append(num)

print(a1, a2, a3)

print(max(max(a1), max(a2), max(a3)))
print(sum(a1) + sum(a2) + sum(a3))