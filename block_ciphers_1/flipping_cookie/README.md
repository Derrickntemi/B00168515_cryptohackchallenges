# Explanation

AES CBC mode XORS the ciphertext of the previous block with the plain text of the current block before encrypting the current block. On the other hand, the decryption process, XORS the decrypted text with the cipher text of the previous block.
Mathematically that could be represented as:
- current_block_cipher_text = Encrypt(previous_block_cipher_text ^ current_block_plain_text)
- current_block_plaint_ext = Decrypt(current_block_cipher_text) ^ previous_block_cipher_text

Since the first block doesn't have a previous block, a random set of bits called the initialization vector (IV) is used.

The cookie we retrieve from the /flipping_cookie/get_cookie/ route is composed of the IV and the encrypted cookie. 
The first 16 bytes represent the IV and the remaining bytes represent the encrypted cookie. 
Flipping bits within the cipher text of the previous block, will alter the bits in the generated plain text of the current block
because the cipher text of the previous block is XORed with the plain text of the current block. In our case since it is the first block, we will attempt to flip bits in the IV.
We will XOR the following bytes:
-  fake_iv = b'original_iv' ^ (b'admin=False;expi' ^ b 'admin=True;expir')


This is done to ensure that the fake IV we will generate will contain the flipped bits, which during the decryption process will be XORed with the plain text, consequently, causing the final text to contain 'admin=True'.

# Flag
 crypto{4u7h3n71c4710n_15_3553n714l}