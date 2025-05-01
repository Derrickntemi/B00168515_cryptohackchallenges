import json
import pwn

remote = pwn.connect('socket.cryptohack.org', 13422)
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
            json_response = check(modified_ct)
            found = True
            if not json_response:
                continue
            else:
                for attempt in range(23):
                    response = check(modified_ct)
                    if not response:
                        print(f"Attempt {attempt} for {candidate} failed")
                        found = False
                        break
            if found:
                print(f"Success, candidate found: {candidate}")
                zeroing_iv[-pad_val] = candidate ^ pad_val
                break
        else:
            raise Exception("no valid padding byte found")

    return zeroing_iv


def check(modified_ct):
    remote.sendline(json.dumps({"option": "unpad", "ct": modified_ct}))
    response = remote.readline().strip().decode()
    return json.loads(response)['result']


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
