sentence = input()

print("".join(list(map(lambda x: chr(ord(x) + 1), sentence))))
