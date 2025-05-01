# Explanation
To retrieve the flag, we will perform the padding attack.
Steps:
- To decrypt the last byte of a ciphertext block C, we will manipulate the last byte of the preceding ciphertext block C - 1 by guessing all possible byte values from 0 - 255.
- After each guess we will send the modified ((C - 1) + C) to the oracle. If the last byte of the decrypted plaintext is flipped to 0x01, then the oracle will respond with true since the padding is valid.
- We will repeat this process for the remaining 15 bytes and move on to the next block.
- We will then xor guessed bytes and an array of their positions to get the decrypted ciphertext which we will in turn xor with the previous block ciphertext ot iv for the first block to retrieve the plaintext.


# flag 
crypto{if_you_ask_enough_times_you_usually_get_what_you_want}