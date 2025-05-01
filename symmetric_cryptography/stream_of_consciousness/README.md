# Explanation
The encryption function initializes the counter from the same value (1), hence, the same key is used for all cipher texts. This makes this challenge a many time pad. We will xor any 2 unique ciphers to cancel out the key then using the flag prefix 'crypto{' we will attempt to retrieve a partial key and thereafter gues the remaining characters of the key.

# Flag
crypto{k3y57r34m_r3u53_15_f474l}