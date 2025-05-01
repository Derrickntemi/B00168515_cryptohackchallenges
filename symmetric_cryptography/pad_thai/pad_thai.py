import json
import pwn

remote = pwn.connect('socket.cryptohack.org', 13421)
BLOCK_SIZE = 16


def attack(iv, ct):
    """Given the iv, ciphertext, finds and returns the plaintext"""
    assert len(iv) == BLOCK_SIZE and len(ct) % BLOCK_SIZE == 0

    msg = iv + ct
    blocks = [msg[i:i + BLOCK_SIZE] for i in range(0, len(msg), BLOCK_SIZE)]
    result = ''

    # loop over pairs of consecutive blocks performing CBC decryption on them
    iv = blocks[0]
    for ct in blocks[1:]:
        dec = single_block_attack(ct)
        pt = bytes(iv_byte ^ dec_byte for iv_byte, dec_byte in zip(iv, dec))
        result += pt.decode()
        iv = ct

    return result


def single_block_attack(block):
    """Returns the decryption of the given ciphertext block"""

    # zeroing_iv starts out nulled. each iteration of the main loop will add
    # one byte to it, working from right to left, until it is fully populated,
    # at which point it contains the result of DEC(ct_block)
    zeroing_iv = [0] * BLOCK_SIZE

    for pad_val in range(1, BLOCK_SIZE + 1):
        padding_iv = [pad_val ^ b for b in zeroing_iv]

        for candidate in range(256):
            padding_iv[-pad_val] = candidate
            iv = bytes(padding_iv)
            modified_ct = bytes.hex(iv) + bytes.hex(block)
            remote.sendline(json.dumps({"option": "unpad", "ct": modified_ct}))
            response = remote.readline().strip().decode()
            json_response = json.loads(response)['result']
            if json_response:
                print(f"correct padding: {json_response}")
                if pad_val == 1:
                    # make sure the padding really is of length 1 by changing
                    # the penultimate block and querying the oracle again
                    padding_iv[-2] ^= 1
                    iv = bytes(padding_iv)
                    ct = bytes.hex(iv) + bytes.hex(block)
                    remote.sendline(json.dumps({"option": "unpad", "ct": ct}))
                    response = remote.readline().strip().decode()
                    json_response = json.loads(response)['result']
                    if not json_response:
                        continue  # false positive; keep searching
                break
        else:
            raise Exception("no valid padding byte found")

        zeroing_iv[-pad_val] = candidate ^ pad_val

    return zeroing_iv


try:
    remote.sendline(json.dumps({"option": "encrypt"}))
    print(remote.readline().strip().decode())
    response = remote.readline().strip().decode()
    ciphertext = json.loads(response)['ct']
    iv = ciphertext[:32]
    cipher = ciphertext[32:]
    message = attack(bytes.fromhex(iv), bytes.fromhex(cipher))
    remote.sendline(json.dumps({"option": "check", "message": message}))
    response = remote.readline().strip().decode()
    flag = json.loads(response)['flag']
    print(f"flag: {flag}")
finally:
    remote.close()
