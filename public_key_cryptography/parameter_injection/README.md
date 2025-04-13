# Explanation
This is a Man in the middle attack, since we have access to g, p, and A, we could intercept A when party A is sending the value to party B and swap it out with p. On the other hand, when party B computes
its public value B, we could intercept it and swap it with for p. Since we have swapped out the public values with p then the secret key will evaluate to a zero (p ^ x mod p = 0, where x is the private value). Therefore, we can decrypt all the messages exchanged between the 2 parties.

# Flag
crypto{n1c3_0n3_m4ll0ry!!!!!!!!}