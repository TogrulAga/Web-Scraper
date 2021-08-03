money = int(input())

p_chicken = 23
p_goat = 678
p_pig = 1296
p_cow = 3848
p_sheep = 6769

if money < p_chicken:
    print("None")
elif money < p_goat:
    print(f"{money // p_chicken} chicken{'s' if money // p_chicken > 1 else ''}")
elif money < p_pig:
    print(f"{money // p_goat} goat{'s' if money // p_goat > 1 else ''}")
elif money < p_cow:
    print(f"{money // p_pig} pig{'s' if money // p_pig > 1 else ''}")
elif money < p_sheep:
    print(f"{money // p_cow} cow{'s' if money // p_cow > 1 else ''}")
else:
    print(f"{money // p_sheep} sheep")
