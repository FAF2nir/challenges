from pwn import *

r = remote("url", port)

r.sendlineafter(b"...", b"a")

while True:
  try:
    data = r.recvline(b"Somma?")

    #select the section with the list of numbers
    string_data = data.split(b"\n")[1]

    to_convert = string_data.decode("utf-8").lstrip('[').rstrip(']')

    #create list of int from the decoded bytes
    final_list = [int(x) for x in to_convert.split(',')]

    sum = 0
    for i in final_list:
      sum += i

    #send the answer to the server
    r.sendline(str(sum))

  except (EOFError):
    flag = r.recvline()
    print(flag)
    break

r.close()