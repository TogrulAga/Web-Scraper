number = int(input())

print(sum(n for n in (number).to_bytes(byteorder="little", length=len(str(number)))))
