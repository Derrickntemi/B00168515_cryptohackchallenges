# Explanation
All png image file have the same header bytes. Using these bytes, we could extract the key stream by xoring the header bytes(16 bytes) and the first 16 bytes of the cipher text. 
Additionally, the generation of the key stream has been implemented wrongly, which leads to the same key stream being produced. Once we have the key stream, we can xor it with 
all the 16 bytes blocks created from the cipher text to get the original image.

-  known_png_bytes = '89504e470d0a1a0a0000000d49484452'
-  known_png_bytes ^ first_16_bytes_of_cipher_text = key_stream
-  key_stream xor cipher_text = plain_text

# flag
crypto{hex_bytes_beans}
