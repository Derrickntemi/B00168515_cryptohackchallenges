import requests
import json
from functools import reduce

URL = 'https://aes.cryptohack.org/symmetry/'


def make_http_request(*args):
    try:
        path = reduce(lambda x, y: x + '/' + y, args)
        response = requests.get(URL + path)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.HTTPError as e:
        print(f"An HTTP error encountered: {e}")
    except json.decoder.JSONDecodeError as e:
        print(f"Json decoding error occurred: {e}")


def get_encrypted_flag():
    return make_http_request('encrypt_flag')['ciphertext']


def encrypt(plain_text, iv):
    return make_http_request('encrypt', plain_text, iv)


flag_cipher_text = get_encrypted_flag()
# first 16 bytes of the cipher text represent the IV
iv = flag_cipher_text[:32]
# when decrypting OFB performs a reverse of the operations it performs during encryption, since we know the IV we can get the algorithm to generate the same key stream used during encryption
# and xor that with the cipher text to get the flag
cipher_text_hex = encrypt(flag_cipher_text[32:], iv)['ciphertext']
print(bytes.fromhex(cipher_text_hex).decode())
