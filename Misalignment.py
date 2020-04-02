# n-2, n-1, n
# Misalignment

D = [0, 0, 1]

n = int(input('Input n (n > 2): '))

assert(n > 2)

for i in range(3, n+1):
    D[0] = D[1]
    D[1] = D[2]
    D[2] = (i-1) * (D[0] + D[1])

print('D:', D[2])
print('Q:', D[2] + D[1])
