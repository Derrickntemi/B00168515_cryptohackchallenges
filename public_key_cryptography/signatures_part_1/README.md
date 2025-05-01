# Explanation
To get the signature we just need to send the secret message (ciphertext) which is computed by performing a modular exponentiation of the secret mod N (pow(secret, E, N)). To sign we perform modular exponentiation using D pow(message, D, N)

# Flag
crypto{d0n7_516n_ju57_4ny7h1n6}