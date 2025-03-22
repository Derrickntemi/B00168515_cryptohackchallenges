def xor_bin_strings(str1, str2):
    return [x ^ y for x, y in zip(str1, str2 * (1 + len(str1) // len(str2)))]


res = xor_bin_strings('label'.encode(), int.to_bytes(13))

print(bytes(res).decode())
