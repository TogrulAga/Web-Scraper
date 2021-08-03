message = input()
key = sum((int(input())).to_bytes(byteorder="little", length=2))

print("".join(list(map(lambda x: chr(ord(x) + key), message))))
