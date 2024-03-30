#from the formula (x mod n = a)

n = [58, 51, 41, 61, 95]
a = [17, 24, 5, 10, 26]
N = 1
b = []
x = []

for i in n:
    N *= i

for i in range(len(n)):
    product = 1
    for j in range(len(n)):
        if( i != j):
            product *= n[j]

    b.append(product)

for u, z in zip(b, n):
    inverse = pow(u, -1, z)
    x. append(inverse)

final = 0
for a,b,c in zip(a, b, x):
    final += a*b*c

print(final%N)

