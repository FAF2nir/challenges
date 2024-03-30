alphabet = "abcdefghijklmnopqrstuvwxyz"

enc_flag = "TTZK{Xrzlj_Alczlj_Trvjri}"
dec_flag = ""

for i in enc_flag:
  if i.lower() in alphabet:
    if i.islower():
      i = alphabet[(alphabet.index(i)+9)%len(alphabet)]
    else:
      i = alphabet[(alphabet.index(i.lower())+9)%len(alphabet)].upper()

  dec_flag += i

print(dec_flag)