# put your python code here
number_1 = float(input())
number_2 = float(input())
operator = input()

if operator == "mod":
    operator = "%"
elif operator == "pow":
    operator = "**"
elif operator == "div":
    operator = "//"

if operator in ['/', '//', '%'] and number_2 == 0.0:
    print("Division by 0!")
else:
    print(eval(f"({number_1}) {operator} {number_2}"))
