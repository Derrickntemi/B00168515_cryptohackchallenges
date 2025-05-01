from Crypto.Cipher import PKCS1_OAEP
from Crypto.PublicKey import RSA
from Crypto.Util.number import inverse
from factordb.factordb import FactorDB

with open("key_17a08b7040db46308f8b9a19894f9f95.pem", "rb") as f:
    public_key = RSA.importKey(f.read())
    n = public_key.n
    e = public_key.e
    f = FactorDB(n)
    f.connect()
    p, q = f.get_factor_list()
    phi = (p - 1) * (q - 1)
    d = inverse(e, phi)
    c = bytes.fromhex('249d72cd1d287b1a15a3881f2bff5788bc4bf62c789f2df44d88aae805b54c9a94b8944c0ba798f70062b66160fee312b98879f1dd5d17b33095feb3c5830d28')
    key = RSA.construct((n, e, d))
    cipher = PKCS1_OAEP.new(key)
    plain_text = cipher.decrypt(c)
    print(plain_text)
