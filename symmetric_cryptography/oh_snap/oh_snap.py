import asyncio
import aiohttp
from collections import Counter

def ksa(partial_key, O):
    S = [i for i in range(256)]
    j = 0
    for i in range(len(partial_key)):
        j = (j + S[i] + partial_key[i]) % 256
        S[i], S[j] = S[j], S[i]
    return (O - j - S[len(partial_key)]) % 256


async def main():
    known = b"crypto{"
    async with aiohttp.ClientSession() as session:

        async def send_cmd(ciphertext, nonce):
            async with session.get(
                f"http://aes.cryptohack.org/oh_snap/send_cmd/{ciphertext.hex()}/{nonce.hex()}"
            ) as resp:
                return (await resp.json())

        async def get_possible_keys(known, i):
            nonce = bytes([len(known) + 3, 255, i])
            result = ksa(nonce + known, int((await send_cmd(b"\0", nonce))["error"][-2:], 16))
            return result

        while len(known) == 0 or known[-1:] != b"}":
            results = Counter(await asyncio.gather(*[get_possible_keys(known, i) for i in range(256)]))
            print({chr(c): n for c, n in results.most_common()})
            results = list(e for e in results.most_common() if e[1] == results.most_common(1)[0][1])
            chosen = None
            print(results)
            if len(results) == 1:
                chosen = results[0]
            else:
                while True:
                    try:
                        for i, r in enumerate(results):
                            print(f"{i}: {chr(r[0])}, {r[1]}")
                        n = int(input("Choice: "))
                        chosen = results[n]
                        break
                    except Exception as e:
                        print(e)
            known += bytes([chosen[0]])
            print(known)


asyncio.run(main())