import json
import requests

URL = 'https://aes.cryptohack.org/triple_des/'


def encrypt_flag(key):
    response = requests.get(URL + 'encrypt_flag/' + key)
    json_response = json.loads(response.text)
    if 'error' in json_response:
        raise ValueError(json_response['error'])
    else:
        return json_response['ciphertext']


def encrypt_plain_text(key, plain_text):
    response = requests.get(URL + 'encrypt/' + key + '/' + plain_text + '/')
    json_response = json.loads(response.text)
    if 'error' in json_response:
        raise ValueError(json_response['error'])
    else:
        return json_response['ciphertext']


key = '0101010101010101FEFEFEFEFEFEFEFE'
ciphertext = encrypt_flag(key)
plain_text = encrypt_plain_text(key, ciphertext)
print(bytes.fromhex(plain_text).decode('utf-8'))
