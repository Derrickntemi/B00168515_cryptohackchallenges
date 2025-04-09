# Explanation
When decrypting, OFB performs the same operations it performs during encryption. To encrypt, the algorithm generates a key stream by encrypting the IV using a block cipher then XORs the plain text with the key stream.
To decrypt, it generates the same key stream and XORs it with the cipher text. Since we have access to the IV, we can get the plain text by encrypting the cipher text of the flag with the IV.

# flag
crypto{0fb_15_5ymm37r1c4l_!!!11!}