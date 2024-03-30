from pwn import *

r = connect('url', port)

while True:
  line = r.recvline()
  line = line.decode('utf-8').split(' ')

  n = line[5]
  type = line[8].rstrip('-bit')
  endianness = line[9].rstrip('-endian')
  if endianness == 'littl':
    endianness = 'little'

  if n == 'line':
    r.send(b'\n')
    line = r.recvline()

  if type == '64':
    r.send(p64(int(n), endian=endianness))
    line = r.recvline()

  if type == '64':
    r.send(p32(int(n), endian=endianness))
    line = r.recvline()

  print(line)