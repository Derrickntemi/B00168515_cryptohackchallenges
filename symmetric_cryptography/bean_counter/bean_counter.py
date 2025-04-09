import json

import requests

URL = 'https://aes.cryptohack.org/bean_counter/'


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


def encrypt():
    try:
        response = requests.get(URL + '/encrypt')
        response.raise_for_status()
        return response.json()['encrypted']
    except requests.exceptions.HTTPError as e:
        print(f"An HTTP error encountered: {e}")
    except json.decoder.JSONDecodeError as e:
        print(f"Json decoding error occurred: {e}")
    except KeyError as e:
        print(f"Key error occurred: {e}")


if __name__ == '__main__':
    cipher_text = encrypt()
    # all png images have the same 16 header bytes
    known_png_bytes = '89504e470d0a1a0a0000000d49484452'
    # xor with the first 16 bytes of the cipher text to extract the key_stream
    key_stream = xor_hex_strings(known_png_bytes, cipher_text[:32])
    decrypted_image_hex = ''.join(
        [xor_hex_strings(key_stream, cipher_text[i: i + 32]) for i in range(0, len(cipher_text), 32)])

    with open('flag.png', 'xb') as f:
        f.write(bytes.fromhex(decrypted_image_hex))
