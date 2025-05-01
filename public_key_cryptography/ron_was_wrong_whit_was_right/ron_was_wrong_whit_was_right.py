import os

from Crypto.Cipher import PKCS1_OAEP
from Crypto.PublicKey import RSA
from Crypto.Util.number import inverse
from gmpy2 import gcd


class Challenge(object):
    def __init__(self, rsa_key, cipher_text):
        self.rsa_key = rsa_key
        self.cipher_text = cipher_text




path = "/Users/derrickntemi/PycharmProjects/B00168515_cryptohackchallenges/public_key_cryptography/ron_was_wrong_whit_was_right/keys_and_messages"
files = os.listdir(path)
public_keys_ciphers = []
for file in files:
    if file.endswith(".pem"):
        with open(path + "/" + file, "rb") as key_file:
            public_key = RSA.importKey(key_file.read())
            with open(path + "/" + file.split('.')[0].split('/')[-1] + '.ciphertext', "r") as ciphertext_file:
                ciphertext = ciphertext_file.read()
                public_keys_ciphers.append(Challenge(public_key, ciphertext))

for i in range(0, len(public_keys_ciphers)):
    for j in range(i + 1, len(public_keys_ciphers)):
        k1 = public_keys_ciphers[i].rsa_key
        k2 = public_keys_ciphers[j].rsa_key

        common = int(gcd(k1.n, k2.n))
        if common != 1:
            p = k1.n // common
            q = common

            phi = (p - 1) * (q - 1)
            d = inverse(k1.e, phi)
            rsa = RSA.construct((k1.n, k1.e, d))
            cipher = PKCS1_OAEP.new(rsa)
            c = bytes.fromhex(public_keys_ciphers[i].cipher_text)
            plaintext = cipher.decrypt(c)
            print(plaintext)