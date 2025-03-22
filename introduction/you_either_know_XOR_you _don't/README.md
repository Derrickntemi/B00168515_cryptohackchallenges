# Explanation
The cipher text can be represented as: 
- cipher_text = flag ^ key. 

The flag starts with the 'crypto{' prefix. Since the XOR operation is an inverse of itself we could xor the prefix
with the ciphertext to extract the key.

# Key
- myXORkey

# Flag
- crypto{1f_y0u_Kn0w_En0uGH_y0u_Kn0w_1t_4ll}
