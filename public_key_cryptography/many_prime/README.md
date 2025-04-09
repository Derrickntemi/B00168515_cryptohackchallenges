# Explanation
The public modulus(n) is constructed using 30 prime nos. To calculate the φ(n), we use factor db lib to get factors then multiply each one of them reduced by one. 
To compute the private exponent (d), we compute the modular inverse of e mod φ(n). Finally, to get the plain text, we perform a modular exponentiation on the cipher text.

# Flag
- crypto{700_m4ny_5m4ll_f4c70r5}