import pwn

input = '73626960647f6b206821204f21254f7d694f7624662065622127234f726927756d'
for b in range(255):
    xor_res = pwn.xor(bytes.fromhex(input), int.to_bytes(b))
    try:
        flag = xor_res.decode()
        if flag.startswith('crypto'):
            print(flag)
            break
    except UnicodeDecodeError:
        pass
