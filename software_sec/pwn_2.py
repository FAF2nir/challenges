from pwn import *

r = remote("url", port)

r.recvutil(b'...')
r.sendlineafter(b'...', b' ')

while True:
  data = r.recvline()
  if data == b'\n':
    data = r.recvline()

  print(data)
  data = data.split(b" ")
  num = data[5]
  option = data[6].decode('utf-8')
  formato = data[8].decode('utf-8')[:2]

  if option == 'packed':
    p = make_packer(formato)
    
    print(p(int(num, 0)))

    r.send(p(int(num, 0)))
    r.recvuntil(b": ")