# Explanation
To retrieve the flag, we factorize n into p & q, then compute the phi (p - 1) * (q - 1), thereafter, we compute the private exponent by performing a modular inverse of e mod phi.
Finally, we compute the modular exponentiation of the ciphertext mod N to decrypt the message (c ** d mod N)

# Flag
crypto{f3rm47_w45_4_g3n1u5}