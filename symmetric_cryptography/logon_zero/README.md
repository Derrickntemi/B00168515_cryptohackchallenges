# Explanation
Due to the poor implementation of the AES CFB mode used in this challenge, if we make the plaintext (IV + ciphertext) all zeros when resetting the password, the password will be set to be length zero. If the authentication fails, we just keep resetting and re-authenticating until we get the flag


# flag
crypto{Zerologon_Windows_CVE-2020-1472}