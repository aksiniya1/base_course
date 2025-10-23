a1 = 1
a2 = 1
n = int(input())

print(1, end=' ')
for i in range (n-1):
    print(a2, end=' ')
    a0 = a1
    a1 = a2
    a2 = a0 + a1