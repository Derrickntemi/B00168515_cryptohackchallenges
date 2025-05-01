# Explanation
To retrieve the flag, we import the public key from the .pem file, then compute the private key using e (public exponent), phi (p - 1) * (q - 1), where p & q are factors of n (prime modulus). 
To reconstruct the flag, we perform modular exponentiation on cipher text c (c ** d mod n)

# Flag
crypto{p00R_3570n14}