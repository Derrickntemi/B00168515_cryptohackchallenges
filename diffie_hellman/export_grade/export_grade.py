import hashlib
import json

import pwn
from Crypto.Cipher import AES
from sympy import discrete_log


def intercept():
    r = pwn.connect('socket.cryptohack.org', 13379)

    try:

        # Alice sending to BOB a list of supported cipher suites
        r.readuntil(": ")
        line = json.loads(r.readline().strip().decode())
        print(line)


        # intercept the message to BOB and forward the weakest bit length of modulus p (64)
        payload = json.dumps({"supported": ["DH64"]})
        print(payload, len(payload))
        r.sendlineafter(": ", payload)

        # intercept the response of the chosen algorithm from BOB to Alice
        r.readuntil(": ")
        line = json.loads(r.readline().strip().decode())
        print(line)

        # forward the chosen algorithm to Alice
        payload = json.dumps({"chosen": "DH64"})
        print(payload, len(payload))
        r.sendlineafter(": ", payload)

        # intercept message from Alice
        r.readuntil(": ")
        line = json.loads(r.readline().strip().decode())
        print(line)
        p = int(line['p'], 16)
        g = int(line['g'], 16)
        A = int(line['A'], 16)

        print(f"p: {p}, g: {g}, A: {A}")

        r.readuntil(": ")
        line = json.loads(r.readline().strip().decode())
        B = int(line['B'], 16)
        print(f"B: {B}")

        r.readuntil(": ")
        line = json.loads(r.readline().strip().decode())
        iv = line['iv']
        encrypted_flag = line['encrypted_flag']
        print(line)

        return g, p, A, B, iv, encrypted_flag
    except Exception as e:
        print(e)

    finally:
        r.close()

# Solve the discrete logarithm problem in a finite field.
def solve_discrete_log(p, g, A, B):
    a = discrete_log(p, A, g)
    b = discrete_log(p, B, g)
    print(f"discrete log: {a}")
    alice_secret = pow(B, int(a), p)
    bob_secret = pow(A, int(b), p)
    print(f"Verification: {alice_secret}, {bob_secret}")
    return pow(B, int(a), p)

g, p, A, B, iv, encrypted_flag = intercept()
secret_key = solve_discrete_log(p, g, A, B)
# derive AES key from secret key
sha1 = hashlib.sha1()
sha1.update(str(secret_key).encode())
key = sha1.digest()[:16]
iv = bytes.fromhex(iv)
encrypted_flag = bytes.fromhex(encrypted_flag)
aes = AES.new(key, AES.MODE_CBC, iv)
print(aes.decrypt(encrypted_flag).decode())


