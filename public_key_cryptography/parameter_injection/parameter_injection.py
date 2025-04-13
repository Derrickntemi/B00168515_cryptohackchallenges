import hashlib
import json

import pwn
from Crypto.Cipher import AES

decrypted_flag = None
def hack():
    r = pwn.connect('socket.cryptohack.org', 13371)
    try:
        r.readuntil(": ")
        line = json.loads(r.readline().strip().decode())
        p = int(line['p'], 16)
        g = int(line['g'], 16)
        A = int(line['A'], 16)

        payload = json.dumps({"p":hex(p),"g":hex(g),"A":hex(p)})
        print(payload, len(payload))
        r.sendlineafter(": ", payload)

        r.readuntil(": ")
        line = json.loads(r.readline().strip().decode())
        B = int(line['B'], 16)

        payload = json.dumps({"B":hex(p)})
        print(payload, len(payload))
        r.sendlineafter(": ", payload)

        r.readuntil(": ")
        line = json.loads(r.readline().strip().decode())
        print(line)

        iv = bytes.fromhex(line['iv'])
        encrypted_flag = bytes.fromhex(line['encrypted_flag'])
        sha1 = hashlib.sha1()
        secret = 0
        sha1.update(str(secret).encode())
        key = sha1.digest()[:16]
        aes = AES.new(key, AES.MODE_CBC, iv)
        print(aes.decrypt(encrypted_flag).decode())
    finally:
        r.close()

hack()


