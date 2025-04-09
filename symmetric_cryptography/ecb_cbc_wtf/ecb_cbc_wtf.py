import json

import requests

URL = 'https://aes.cryptohack.org/ecbcbcwtf/'


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


def get_encrypted_flag():
    response = requests.get(URL + 'encrypt_flag/').text
    json_data = json.loads(response)
    return json_data['ciphertext']


def decrypt_cipher_text(encrypted_text):
    response = requests.get(URL + 'decrypt/' + encrypted_text).text
    json_data = json.loads(response)
    return json_data['plaintext']


cipher_text = get_encrypted_flag()
iv, first_block_cipher, last_block_cipher = cipher_text[:32], cipher_text[32:64], cipher_text[64:]
last_block_plaintext = xor_hex_strings(decrypt_cipher_text(last_block_cipher), first_block_cipher)
first_block_plaintext = xor_hex_strings(decrypt_cipher_text(first_block_cipher), iv)

print(bytes.fromhex(first_block_plaintext).decode() + bytes.fromhex(last_block_plaintext).decode())
