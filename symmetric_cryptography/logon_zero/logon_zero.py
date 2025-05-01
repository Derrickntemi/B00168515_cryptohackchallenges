import json

import pwn

remote = pwn.connect('socket.cryptohack.org', 13399)

token = (b"\x00" * 28).hex()

print(remote.readline().strip().decode())

while True:
    remote.sendline(json.dumps({"option": "reset_password", "token": token}))
    print(remote.readline().strip().decode())
    remote.sendline(json.dumps({"option": "authenticate", "password": ""}))
    response = remote.readline().strip().decode()
    if "admin" in response:
        print(response)
        break

    remote.sendline(json.dumps({"option": "reset_connection"}))
    print(remote.readline().strip().decode())
