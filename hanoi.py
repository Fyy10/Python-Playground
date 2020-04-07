a = [0]

n = int(input())

for i in range(1, n + 1):
    # an = 2*an-1 + 1
    a.append(2 * a[i-1] + 1)

print(a[n])
