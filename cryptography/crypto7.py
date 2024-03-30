from Crypto.Cipher import DES, AES, ChaCha20
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad

#PART 1
key = bytes.fromhex('168915e12f922f41')
plaintext = str.encode('Phrase to encode')
cipher = DES.new(key, DES.MODE_CBC)
iv = bytes.hex(cipher.iv)

print(f"ciphertext = {bytes.hex(cipher.encrypt(pad(plaintext, 8, 'x923')))}")
print(f"iv = {iv}")

#PART 2
key = get_random_bytes(32)
plaintext = str.encode('Phrase to encode')
cipher = AES.new(key, AES.MODE_CFB, segment_size=24)

print(f"key = {bytes.hex(cipher.encrypt(pad(plaintext, 16, 'pkcs7')))}")
print(f"iv = {bytes.hex(cipher.iv)}")


#PART 3
key = 'ee4295080b49de2610b7cda3074bbd2fb12220cf3f2aca32e6caff325d250973'
ciphertext = '6faa514cc5f750cda97ae25f1419086a3f68413db0b68c8d667f7061'
nonce = '9b78e09753ec8efa'

cipher = ChaCha20.new(key=bytes.fromhex(key), nonce=bytes.fromhex(nonce))
print(f"message = {cipher.decrypt(bytes.fromhex(ciphertext))}")
