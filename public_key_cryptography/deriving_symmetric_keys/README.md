# Explanation
To compute the shared secret, we raise the public value we received (A) to b (our secret value) mod P (A ^ b mod). Fundamentally the public value from the other party is, (g ^ a mod p), where a is the secret value of the other party.

# Flag
crypto{sh4r1ng_s3cret5_w1th_fr13nd5}
