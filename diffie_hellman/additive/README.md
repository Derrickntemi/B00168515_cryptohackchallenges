# Explanation
An additive group, is a group of integers whose operation is addition. it is trivial to compute a or b i.e the secret keys by simply reversing the operation(addition).
A = g*a (mod p)
B = g*b (mod p)
key = A*b = B*a = g*a*b (mod p)

To compute the exponent:
g*a = A (mod p) --> g = A*inverse(g) (mod p)
g*b = B (mod p) --> g = B*inverse(g) (mod p)


# Flag
crypto{cycl1c_6r0up_und3r_4dd1710n?}