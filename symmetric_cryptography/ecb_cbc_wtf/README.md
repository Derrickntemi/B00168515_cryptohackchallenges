# Explanation
ECB mode generates identical cipher if given the same plain text multiple times. On the other hand, 
CBC mode introduces randomness by using a random value called IV(initialization vector). In CBC mode, 
the plain text is xored with the cipher text of the previous block before the key is added. 
In the case of the first block, the initialization vector is used. 
In this challenge, we have a decrypt function that operates in ECB mode and an encrypt function 
that operates in CBC mode. Since they all use the same key, we will utilize them to retrieve the flag as follows:
- Retrieve the cipher text of the flag and take the first 16 bytes that represent the IV. The remaining bytes represent the cipher text of the flag.
- Decrypt the last 32 bytes that represent the last block of the cipher text using the ECB mode decrypt function then xor the result with the cipher text of the first block.
- Finally, decrypt the bytes representing the first block and xor that with the IV.

Mathematically, that look as follows:
- plain_text_last_block = Decrypt(cipher_text_last_block) ^ cipher_text_first_block
- plain_text_first_block = Decrypt(cipher_text_first_block) ^ IV

# Flag
crypto{3cb_5uck5_4v01d_17_!!!!!}
