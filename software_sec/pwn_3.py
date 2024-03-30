from pwn import *

exe = ELF("./sw-19")

r = remote("url", port)

r.recvuntil(b'...')
r.sendafter(b'...', b'a')

while True:
  line = r.recvuntil(b':')
  line = line.strip().split(b' ')

  fun_name = line[1].decode('utf-8').rstrip(':')

  if fun_name != 'Congratulazioni!':
    address = exe.sym[fun_name]
    address = hex(address).lstrip('0x')

    address = address.encode()

    r.sendline(address)
  else:
    print(r.recvline())
    r.close()
    exe.close()
    break