from Crypto.Hash import SHA3_384, SHA224, HMAC
from Crypto.PublicKey import DSA
from Crypto.Random import *
from Crypto.Util.number import *

#QUESTION 1
msg = input("1 - message: ")
sha = SHA3_384.new()
print(sha.hexdigest())

#QUESTION 2
msg = input("2 - message: ")
key = input("Key: ")

hash = HMAC.new(bytes.fromhex(key), msg.encode())
print("Hmac_digest = " + hash.hexdigest())

#QUESTION 3
dsa_key = bytes.fromhex(input("3 - DSA key: "))
key = DSA.import_key(dsa_key)
print(f"p = {key.p}")
print(f"q = {key.q}")
print(f"g = {key.g}")
print(f"y = {key.y}")

#QUESTION 4
size = input("4 - size: ")
print(getPrime(size))

#QUESTION 5
print(isPrime(int(input("5 - Number: "))))