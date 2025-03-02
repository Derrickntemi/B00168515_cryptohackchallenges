import json

import requests

ENCRYPT_URL = "https://aes.cryptohack.org/lazy_cbc/"


def encrypt(plain_text):
    response = requests.get(ENCRYPT_URL + "encrypt/" + plain_text)
    json_data = json.loads(response.text)
    return json_data['ciphertext']


def decrypt(cipher_text):
    response = requests.get(ENCRYPT_URL + "receive/" + cipher_text)
    json_data = json.loads(response.text)
    result = ""
    if "error" in json_data:
        response = json_data['error']
        start = response.rindex(":")  # get the last index of :
        result = response[start + 2:]  # add 2 because there is a space character after :
    return result


def get_flag(key):
    response = requests.get(ENCRYPT_URL + "get_flag/" + key)
    json_data = json.loads(response.text)
    if "plaintext" not in json_data:
        print("Key retrieval failed")
        return
    return json_data['plaintext']


def xor_hex_strings(hex1: str, hex2: str):
    # Convert hex to bytes
    bytes1 = bytes.fromhex(hex1)
    bytes2 = bytes.fromhex(hex2)

    # Determine the longer and shorter byte sequences
    if len(bytes1) > len(bytes2):
        long_bytes, short_bytes = bytes1, bytes2
    else:
        long_bytes, short_bytes = bytes2, bytes1

    # pad with zeros
    padded_short_bytes = short_bytes.ljust(len(long_bytes) - len(short_bytes), b'0')

    # XOR the two byte sequences
    res = bytes((a ^ b) for a, b in zip(long_bytes, padded_short_bytes))
    return res.hex()


def reveal_flag():
    plain_text = 'AA' * (16 * 3)
    cipher_text = encrypt(plain_text)
    fake_cipher_text = cipher_text[:32] + ('00' * 16) + cipher_text[:32]
    fake_plain_text = decrypt(fake_cipher_text)
    key = xor_hex_strings(fake_plain_text[:32], fake_plain_text[64:])
    print(str(bytes.fromhex(get_flag(key))))


reveal_flag()
