size = int(input())

if size < 1:
    print("no army")
elif 1 <= size <= 9:
    print("few")
elif 10 <= size <= 49:
    print("pack")
elif 50 <= size <= 499:
    print("horde")
elif 500 <= size <= 999:
    print("swarm")
elif size >= 1000:
    print("legion")
