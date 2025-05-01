import json
import requests

URL = 'https://aes.cryptohack.org/stream_consciousness/encrypt/'

prefix = 'crypto{'


def encrypt():
    return json.loads(requests.get(URL).text)['ciphertext']


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


ciphers = set()
while True:
    ciphertext = encrypt()
    ciphers.add(ciphertext)
    if len(ciphers) == 22:
        break

ciphers_list = list(ciphers)

attack_word = b'And I shall'
found = [b'crypto{', b'How pro', b'Three b', b'Dolly w', b"I'm unh", b'What a ', b'Dress-m', b'But I w', b'I shall',
         b"No, I'l", b'The ter', b'And I s', b'Our? Wh', b'As if I', b'Love, p', b'Perhaps', b"It can'", b'Would I',
         b'Why do ', b'These h']

founds = []
attacks = []
xored = []
attacks.append(attack_word)
founds.append(found)

'''
then I xored everything in the 'xored' array with 'crypto{' and manually observed the generated english words!
afterwards I xored strings by guessing and got the entire flag!
'''

while True:
    newlyfound = []
    newlyfound.append(attack_word)
    for i in xored:
        ln = min(len(i), len(attack_word))
        xoring = xor_hex_strings(attack_word[:ln], i[:ln])

        for i in found:
            if i in xoring:
                newlyfound.append(xoring)

    for i in newlyfound:
        print(i.decode())

    word = input("Enter next plausible phrase, 'back'or 'end':")
    if word == 'back':
        attacks.remove(attacks[-1])
        founds.remove(founds[-1])
        found = founds[-1]
        attack_word = attacks[-1]
    elif word == 'exit':
        for i in newlyfound:
            if b'crypto' in i:
                print(i.decode())
        break
    else:
        attack_word = word.encode()
        found = newlyfound
        attacks.append(attack_word)
        founds.append(newlyfound)
