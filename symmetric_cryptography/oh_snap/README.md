# Explain
This challenges looks to break RC4 encryption using the FMS attack. The FMS attack exploits weaknesses in the RC4 algorithm's initialization vector (IV) and key derivation process, allowing an attacker to recover the secret key from a large number of encrypted messages. The algorithm works by generating a keystream from an initial state of a nonce and an unknown Flag. After this the keystream is xored with the plaintext to generate the cipher text.
 - ciphertext = m ^ KSA(nonce + k), KSA (Key scheduling algorithm)
 - m = ciphertext ^ KSA(nonce + k)
 - keystream = ciphertext ^ plaintext

# flag
crypto{w1R3d_equ1v4l3nt_pr1v4cy?!}