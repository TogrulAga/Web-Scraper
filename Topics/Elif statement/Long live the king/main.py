column = int(input())
row = int(input())

if 1 < column < 8 and 1 < row < 8:
    print(8)
elif column in (1, 8) and 1 < row < 8:
    print(5)
elif row in (1, 8) and 1 < column < 8:
    print(5)
elif column in (1, 8) and row in (1, 8):
    print(3)
