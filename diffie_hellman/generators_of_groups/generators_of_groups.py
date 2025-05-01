from sympy import isprime, factorint

def find_generator(p):
    assert isprime(p), "P must be prime"
    phi = p - 1
    factors = factorint(phi).keys()

    for g in range(2, p):
        if all(pow(g, phi // q, p) != 1 for q in factors):
            return g
    return None

P = 28151
g = find_generator(P)
print(f"A generator modulo {P} is: {g}")
