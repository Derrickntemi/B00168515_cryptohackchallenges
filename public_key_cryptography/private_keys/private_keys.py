def extended_gcd(a, b):
    x,y, u,v = 0,1, 1,0
    while a != 0:
        q, r = b//a, b%a
        m, n = x-u*q, y-v*q
        b,a, x,y, u,v = a,r, u,v, m,n
    return x

# x is the multiplicative inverse of a mod b
print(extended_gcd(65537,882564595536224140639625987657529300394956519977044270821168))
