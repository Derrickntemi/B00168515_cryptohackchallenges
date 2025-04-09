# Explanation
We can compute d by finding the modular inverse of e mod φ(n). N is a small prime no, factorizing it will be easy (1 * n). To compute the φ(n) will be as easy as n - 1. To decrypt we will perform modular exponentiation on the ct (ct ^ d mod n).

# flag
- crypto{saltstack_fell_for_this!}