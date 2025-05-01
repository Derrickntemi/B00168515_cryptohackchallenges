import requests
from Crypto.Util.Padding import unpad

url = "http://aes.cryptohack.org/paper_plane/"
flag_url = url + "encrypt_flag/"
send_url = url + "send_msg/%s/%s/%s/"

sess = requests.Session()
data = sess.get(flag_url).json()
ciphertext = bytes.fromhex(data["ciphertext"])
m0 = bytes.fromhex(data["m0"])
c0 = bytes.fromhex(data["c0"])


def guess_plaintext(ciphertext, m0, c0):
    data = sess.get(send_url % (ciphertext.hex(), m0.hex(), c0.hex())).json()
    return "error" not in data

pt = bytearray(len(ciphertext))
keys = bytearray(len(ciphertext))

for b in range(len(ciphertext) // 16):
    ct = ciphertext[16 * b:16 * b + 16]

    for i in range(16 - 1, -1, -1):
        for c in range(256):
            c0_2 = bytearray(c0)
            c0_2[i] = c
            for j in range(i + 1, 16):
                c0_2[j] = keys[16 * b + j] ^ (16 - i)

            if guess_plaintext(ct, m0, c0_2):
                k = c ^ (16 - i)
                keys[16 * b + i] = k
                pt[16 * b + i] = k ^ c0[i]
                break

        print(pt)

        if pt[16 * b + i] == 0:
            break

    m0 = pt[16 * b:16 * b + 16]
    c0 = ciphertext[16 * b:16 * b + 16]

print("flag", unpad(pt, 16))