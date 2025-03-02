import json
import requests

GET_COOKIE_URL = "https://aes.cryptohack.org/flipping_cookie/get_cookie/"
CHECK_ADMIN_URL = "https://aes.cryptohack.org/flipping_cookie/check_admin/"


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


def retrieve_cookie():
    request = requests.get(GET_COOKIE_URL)
    json_data = json.loads(request.text)
    return json_data['cookie']


def flip_bits(original_cookie):
    original_cookie = retrieve_cookie()
    original_iv = original_cookie[:32]
    ciphertext = original_cookie[32:]
    text = 'admin=False;expi'
    fake_cookie = 'admin=True;expir'
    flipped = xor_hex_strings(text.encode().hex(), fake_cookie.encode().hex())
    fake_iv = xor_hex_strings(flipped, original_iv)
    print(len(fake_iv))
    return ciphertext, fake_iv


def retrieve_flag():
    cookie = retrieve_cookie()
    ciphertext, iv = flip_bits(cookie)
    request = requests.get(CHECK_ADMIN_URL + "/" + ciphertext + "/" + iv)
    json_data = json.loads(request.text)
    if "flag" in json_data:
        print(f"Flag found: {json_data['flag']}")
    else:
        print(f"Flag not found: {json_data}")
    return


retrieve_flag()
