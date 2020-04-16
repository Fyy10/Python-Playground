F = [1, 1]

n = int(input())

for i in range(2, n + 1):
    # Fn = Fn-1 + Fn-2
    F.append(F[i-1] + F[i-2])

print(F[n])
