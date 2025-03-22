# Explanation
Since the key is derived by hashing a random word that is retrieved from a dictionary of words. We could brute force the key by iterating through all the words of dictionary. Also, we have an idea of the format of the flag (crypto{xxxxxxx}). 
If we find a key that decrypts the cipher text to a plain text that starts with 'crypto{' then that is the flag we are searching for 
The pseudocode will look like the following:

encrypted_flag = get_encrypted_flag()
for word in dictionary:
    key = hash(word)
    plain_text_hex = decrypt_flag(encrypted_flag, key)
    plain_text = decode(plain_text_hex)
    if plain_text.startswith('crypto{'):
        print(plain_text)
        break
    
