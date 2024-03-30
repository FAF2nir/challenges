import random

def isPrime(n):
  for i in range(2, int(n/2)):
    if n%i == 0:
      return False
  
  return True

#only if p is prime
def phi(p):
  return p-1

def discrete_log(x, a, p):
  for b in range(phi(p)-1):
    if(pow(a, b, p) == x):
      return b
    
  return "There is a problem"

x = 14
a = 2
p = 59

print(discrete_log(x, a, p))

p = 97
g = 2

primes = [i for i in range(2, p) if isPrime(i)]
a = 50
b = random.choice(primes)

A = pow(g, a, b)
print(f"Alice info: A->{A}, a->{a}")
B = pow(g, b, p)
print(f"Bob info: B->{B}, b->{b}")

shared_key = pow(A, b, p)
print(f"Shared key --> {shared_key}")