code = int(input())

if code in range(32, 127):
    print(chr(code))
else:
    print(False)
