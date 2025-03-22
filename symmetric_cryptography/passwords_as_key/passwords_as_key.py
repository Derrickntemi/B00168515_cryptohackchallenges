import hashlib
import json
from functools import reduce
import requests

URL = 'https://aes.cryptohack.org/passwords_as_keys/'


def get_words():
    # /usr/share/dict/words from
    # https://gist.githubusercontent.com/wchargin/8927565/raw/d9783627c731268fb2935a731a618aa8e95cf465/words
    with open("/usr/share/dict/words") as f:
        return [w.strip() for w in f.readlines()]


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


words = get_words()
encrypted_flag_json_response = make_http_request('encrypt_flag')
encrypted_flag = encrypted_flag_json_response['ciphertext']
for word in words:
    try:
        print("Encrypting '" + word + "'")
        hashed_word = hashlib.md5(word.encode()).hexdigest()
        decrypted_flag_json_response = make_http_request('decrypt', encrypted_flag, hashed_word)
        decrypted_flag = decrypted_flag_json_response['plaintext']
        flag = bytes.fromhex(decrypted_flag).decode()
        if flag.startswith('crypto{'):
            print(flag)
            break
    except UnicodeDecodeError as e:
        pass
