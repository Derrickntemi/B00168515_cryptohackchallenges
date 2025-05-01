# Explanation
- Intercept the message from Alice to Bob sending him a list of supported DH versions
- Alter the message by removing all other versions other than DH64, the weakest bit length, and forward the message to Bob.
- Bob will respond as having chosen DH64 since that was the only option.
- Alice will send the parameters p (prime modulus whose length is 64 bits), g (a generator of the group of integers modulo p ), A
- Since we have p, g, A parameters and we know that DH64 is the algorithm is in use, we can compute the discrete algorithm of A to the base g modulo p. 
  These will give us the secret key of Alice. We can also compute Bob's secret key and then use both keys to generate the shared secret and verify that they both generate the same value.
- After computing the shared secret key, we intercept the encrypted message sent to Bob by Alice and use the shared secret key and the AEs cipher to decrypt the flag.

# Flag
crypto{d0wn6r4d35_4r3_d4n63r0u5}