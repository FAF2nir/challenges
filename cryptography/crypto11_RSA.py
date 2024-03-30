#Compute euler's function
def phi(p, q):
    return (p-1) * (q-1)

def gcd(a, b):
    if (b == 0):
        return a
    return gcd(b, a%b)

p = 17
q = 3

private_key = []
public_key = []

n = p * q
totient = phi(p, q)

for i in range(2, totient):
    if(gcd(i, totient) == 1):
        e = i
        break

public_key.append(e)
public_key.append(n)

d = pow(e, -1, totient)

private_key.append(d)
private_key.append(n)

print(f"p = {p} q = {q}")
print(f"n = {n} totient = {totient}")
print(f"e = {public_key[0]} n = {public_key[1]}")
print(f"d = {private_key[0]} n = {private_key[1]}")

#message to encode
m = 50

#encode
c = pow(m, e, n)
print(f"c = {c}")

#decode
m = pow(c, d, n)

