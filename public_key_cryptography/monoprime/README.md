# Explanation
We have access to the public modulus (n) and the public exponent (e), which is the public key. We can compute the private exponent, that is the private key, 
by computing, the modular inverse of e mod φ(n). Additionally, the public modulus isn't a product of 2 large prime numbers, so it is easy to factorize it.

# Flag
- crypto{0n3_pr1m3_41n7_pr1m3_l0l}
