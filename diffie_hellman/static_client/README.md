# Explanation
Since party B uses a static secret key, we could trick them to generate the shared secret key by swapping out g for A (g ^ a mod p), that will lead party B to compute,
A ^ b mod P which is equal to the shared secret key.
- Party A send g, p, and A (g ^ a mod p)
- Party B responds with B (g ^ b mod p)
- Party A computes the shared secret using (B ^ a mod p)
- since party B is using a static secret key(b), we will send g, p, and A to it again but this time swap g with A, so we will send, A, p, A instead of g, p, A.
- party B will respond with the shared secret key B (A ^ b mod p)

# Flag
crypto{n07_3ph3m3r4l_3n0u6h}