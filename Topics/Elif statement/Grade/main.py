grade = float(input())
max_grade = float(input())
alpha_grade = grade / max_grade * 100
if alpha_grade < 60:
    print("F")
elif 60 <= alpha_grade < 70:
    print("D")
elif 70 <= alpha_grade < 80:
    print("C")
elif 80 <= alpha_grade < 90:
    print("B")
elif 90 <= alpha_grade <= 100:
    print("A")
