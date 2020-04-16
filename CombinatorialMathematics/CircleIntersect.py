a = [1, 2]

n = int(input())

for i in range(2, n + 1):
    # an = an-1 + 2*(n-1)
    a.append(a[i-1] + 2*(i-1))

print(a[n])
