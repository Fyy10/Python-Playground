a = [1, 1]

n = int(input())

for i in range(2, n + 1):
    tmp = 0
    for j in range(1, i):
        tmp += a[j] * a[i-j]
    a.append(tmp)

print(a[n])
