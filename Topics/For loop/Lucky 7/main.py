n = int(input())
nums = [int(input()) ** 2 for _ in range(n)]

print(*list(filter(lambda x: x % 7 == 0, nums)), sep="\n")
