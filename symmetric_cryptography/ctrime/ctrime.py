import json
import requests

URL = 'https://aes.cryptohack.org/ctrime/encrypt'


def generate_all_possible_chars_hex():
    chars = []
    for i in range(1, 256):
        if len(hex(i)[2:]) == 1:
            chars.append('0' + hex(i)[2:])
        else:
            chars.append(hex(i)[2:])
    return chars


def encrypt(plaintext):
    response = requests.get(URL + '/' + plaintext)
    json_data = json.loads(response.text)
    return json_data['ciphertext']


def bruteforce():
    chars = generate_all_possible_chars_hex()
    flag = 'crypto{'
    prefix = bytes.hex(flag.encode())
    size = len(encrypt(prefix))
    print(size)
    while True:
        for char in chars:
            current_size = len(encrypt(bytes.hex(flag.encode()) + char))
            if current_size == size:
                flag += bytes.fromhex(char).decode()
                print(f"Current_flag: {flag}")
                break

            if flag == "crypto{CRIM":
                flag += 'E'
                size += 2
                break

        if flag[-1] == '}':
            break
    print(f"Found flag: {flag}")


bruteforce()
