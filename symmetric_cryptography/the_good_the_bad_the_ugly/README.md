# Explanation
This challenge is quite similar to the pad thai challenge where we exploited the leaking padding information to retrieve the flag. The only difference is the oracle. The oracle performs a logical or operation when checking the padding (good | (rng.random() > 0.4)). This leads to false positives.
So, for each individual call to rng.random(), there is a 60% chance that the returned value will be greater than 0.4.
We can circumvent this hurdle by checking the padding multiple times. However, there is limit of the no of requests that can be made, 12,000. For every block, in the worst case scenario, we make 16 * 256 requests.
Steps:
- To decrypt the last byte of a ciphertext block C, we will manipulate the last byte of the preceding ciphertext block C - 1 by guessing all possible byte values from 0 - 255.
- After each guess we will send the modified ((C - 1) + C) to the oracle. If the last byte of the decrypted plaintext is flipped to 0x01, then the oracle will respond with true since the padding is valid.
- We will repeat this process for the remaining 15 bytes and move on to the next block.
- We will then xor guessed bytes and an array of their positions to get the decrypted ciphertext which we will in turn xor with the previous block ciphertext ot iv for the first block to retrieve the plaintext.


# flag 
crypto{if_you_ask_enough_times_you_usually_get_what_you_want}