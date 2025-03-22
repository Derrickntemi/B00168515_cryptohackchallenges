import pwn

cipher_text = '0e0b213f26041e480b26217f27342e175d0e070a3c5b103e2526217f27342e175d0e077e263451150104'
flag_prefix = 'crypto{'
key = pwn.xor(flag_prefix.encode(), bytes.fromhex(cipher_text))
print(key)
flag = pwn.xor('myXORkey'.encode(), bytes.fromhex(cipher_text))
print(flag.decode())
