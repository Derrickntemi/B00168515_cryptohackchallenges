from factordb.factordb import FactorDB

f = FactorDB(510143758735509025530880200653196460532653147)
f.connect()
print(f.get_factor_from_api())
