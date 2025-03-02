# Explanation
The encryption is wrongly implemented because it uses the KEY as an IV instead of using a random set of bits. To exploit this flaw,
we will follow the following process:
- since the key is used as the IV, key could be retrieved by the following operation:
  - key = Decrypt(C) ^ p
- If we can curate some cipher text of 3 block each with 16 bytes such that the first block is equal to the last block and the mid block is a zero, then we can retrieve the key. That will work as follows:
  - first_block_plain_text = Decrypt(C0) ^ IV
  - second_block_plain_text = Decrypt(C1) ^ C0
  - third_block_plain_text = Decrypt(C2) ^ C1

- By making the first block same as the last block (C0 == C2) and replacing the middle block with zeros (C1 = 0), we will get:
  - first_block_plain_text = Decrypt(C0) ^ IV
  - second_block_plain_text = Decrypt(0) ^ C0
  - third_block_plain_text = Decrypt(C0) ^ 0
- XORing first and last block will give us the flag since IV == KEY: 
  - (Decrypt(C0) ^ IV) XOR  (Decrypt(C0) ^ 0) = IV

# Flag
crypto{50m3_p30pl3_d0n7_7h1nk_IV_15_1mp0r74n7_?}