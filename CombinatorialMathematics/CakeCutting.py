a = [1]

n = int(input())

for i in range(1, n + 1):
    # an = an-1 + n
    a.append(a[i-1] + i)

print(a[n])
