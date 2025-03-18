# Explanation
Triple DES has known weak keys that make the algorithm to behave in an undesirable manner. The keys are listed on wikipedia (https://en.wikipedia.org/wiki/Weak_key#Weak_keys_in_DES).
The algorithm splits the given key into 2 or 3 keys depending on the length of the initial key. If the key is 16 bytes, the key is split into K1 and K2, where K1 and K2 are independent and K3 == K1. On the other hand, if the key is 24 bytes long, the key split into 3 independent keys where K1 != K2 != K3. When a weak key is used, running the encryption process twice will generate the plain text, i.e 
- Encryption(Encryption(p)) = p

To circumvent the error generated when a 16 bytes key is provided such that K1 == K2, we use 2 different 8 bytes weak keys. For instance, 0x0101010101010101, 0xFEFEFEFEFEFEFEFE will do the trick

# Flag
crypto{n0t_4ll_k3ys_4r3_g00d_k3ys}