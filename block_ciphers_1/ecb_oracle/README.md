## Explanation ##
We know the encryption algorithm is a block cipher operating in ECB mode and a block size of 16 bytes. This means identical blocks will generate identical cipher text.
Since our input is appended to the secret flag before it is encrypted, we can generate our input in the following manner to attempt and guess the characters of the secret flag.
Using AA as the padding and our guess as 'a', after our input is appended to the flag, it will look as follows:
- first block will be 15 bytes of the padding and the last character as the guessed character: AAAAAAAAAAAAAAAa. 
- second block will be 15 bytes of the padding and the last character will be of the actual flag: AAAAAAAAAAAAAAAc
- third block will have the remaining 16 characters of the flag: rypto{abcdefghi}

                                                                                                                          
If our guess is correct, the cipher text of the first and second block will be equal. In the next attempt we will reduce our padding to 14 bytes and guess the next character of the flag. This process will be repeated by guessing all the subsequent characters and comparing their cipher text blocks until we get the whole flag.

# Flag
crypto{p3n6u1n5_h473_3cb}