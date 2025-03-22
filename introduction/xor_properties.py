import pwn

flag_key1_key2_key_3 = '04ee9855208a2cd59091d04767ae47963170d1660df7f56f5faf'
key_1 = 'a6c8b6733c9b22de7bc0253266a3867df55acde8635e19c73313'
key_2_key_1 = '37dcb292030faa90d07eec17e3b1c6d8daf94c35d4c9191a5e1e'
key_2_key_3 = 'c1545756687e7573db23aa1c3452a098b71a7fbf0fddddde5fc1'
print(pwn.xor(bytes.fromhex(flag_key1_key2_key_3), bytes.fromhex(key_1), bytes.fromhex(key_2_key_3)).decode())
