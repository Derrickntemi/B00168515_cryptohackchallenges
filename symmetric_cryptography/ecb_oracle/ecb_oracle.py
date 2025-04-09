import binascii
import json
import requests

URL = 'https://aes.cryptohack.org/ecb_oracle/encrypt/'


def encrypt(param):
    """
    Encrypts the provided input by sending a GET request to an external service that encrypts the plain text using a Block cipher ECB mode that use 16 bytes blocks.
    The received JSON response is then parsed to retrieve the ciphertext.

    :param param: The input string to be encrypted.
    :type param: str
    :return: The encrypted ciphertext obtained from the service.
    :rtype: str
    """
    response = requests.get(URL + param)
    parsed_response = json.loads(response.content.decode())
    return parsed_response['ciphertext']


def add_padding(guess, chars):
    """
    Pads the guessed flag string with hex strs from the `chars` list equally on both
    sides so that the final length aligns with a multiple of 16. This is because the encryption algorithm uses blocks of 16 bytes.

    :param guess: hex string to be padded.
    :type guess: str
    :param chars: List of hex characters to use for padding.
    :type chars: list[str]
    :return: The padded string.
    :rtype: str
    """
    count = len(guess) // 2
    padding_len = 16 - count % 16
    return ''.join(chars[:padding_len]) + guess + ''.join(chars[:padding_len])


def generate_all_possible_chars_hex():
    """
    Generate a list of all possible hexadecimal representations for numbers
    from 1 to 255.

    This function creates a list of two-character hexadecimal strings for
    integers within the range of 1 to 255. If the hexadecimal string for a
    number is a single character, it gets padded with a leading zero to
    ensure consistent two-character width.

    :return: List of strings, where each string is a two-character
             hexadecimal representation of numbers from 1 to 255.
    :rtype: list[str]
    """
    chars = []
    for i in range(1, 256):
        if len(hex(i)[2:]) == 1:
            chars.append('0' + hex(i)[2:])
        else:
            chars.append(hex(i)[2:])
    return chars


if __name__ == "__main__":
    chars = generate_all_possible_chars_hex()
    flag = ''
    last_char = ''
    # we know the last char will be a }, 7d is its hex representation
    while last_char != '7d':
        for char in chars:
            last_char = char
            guess = flag + char
            padded_guess = add_padding(guess, chars)
            cipher_text = encrypt(padded_guess)
            # when the length of our guess is 16 bytes long, we need to include the next block in the comparison
            len_guess = len(guess) // 2
            cipher_text_slice_len = 2 * (16 - (len_guess % 16) + len_guess)
            #print(cipher_text_slice_len)
            if cipher_text[:cipher_text_slice_len] == cipher_text[cipher_text_slice_len:cipher_text_slice_len * 2]:
                flag = guess
                print(binascii.unhexlify(flag).decode(), flush=True)
                break
