import hashlib
import json
import pwn
from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad
from Crypto.Util.number import inverse


def intercept():
    remote = pwn.connect('socket.cryptohack.org', 13380)

    try:
        # intercepted from Alice
        remote.recvuntil("Intercepted from Alice:".encode())
        response = remote.recvline()
        alice_to_bob = json.loads(response)

        print(f"{alice_to_bob}\n")


        p = int(alice_to_bob['p'], 16)
        g = int(alice_to_bob['g'], 16)
        A = int(alice_to_bob['A'], 16)

        print(f"p: {p}\n g: {g}\n A: {A}\n")

        # intercept from BOB
        remote.recvuntil("Intercepted from Bob:".encode())
        response = remote.recvline()
        bob_to_alice = json.loads(response)
        B = int(bob_to_alice['B'], 16)

        print(f"B: {B}\n")

        # intercepted from Alice
        remote.recvuntil("Intercepted from Alice:".encode())
        response = remote.recvline()
        alice_to_bob = json.loads(response)

        print(f"Message: {alice_to_bob}\n")

        b = B * inverse(g,p)
        a = A * inverse(g,p)

        secret_key = (A * b) % p

        print(f"{(g*a*b)%p == (B*a)%p == (A*b)%p}")

        return (secret_key, alice_to_bob['iv'], alice_to_bob['encrypted'])
    finally:
        remote.close()

def is_pkcs_7_padded(message):
    padded_slice = message[-message[-1]:]
    return all(padded_slice[index] == len(padded_slice) for index in range(0, len(padded_slice)))

key, iv, encrypted_flag = intercept()
sha1 = hashlib.sha1()
sha1.update(str(key).encode())
key = sha1.digest()[:16]
iv = bytes.fromhex(iv)
encrypted_flag = bytes.fromhex(encrypted_flag)
aes = AES.new(key, AES.MODE_CBC, iv)
plaintext = aes.decrypt(encrypted_flag)

if is_pkcs_7_padded(plaintext):
    print(unpad(plaintext, AES.block_size).decode())
else:
    print(plaintext.decode())