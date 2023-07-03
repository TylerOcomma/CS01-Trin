score1=float(input("Enter your score :"))
if score1 >30:
    print("Program stopped because the score is more than 30")
    quit()

score2=float(input("Enter your score :"))
if score2 >30:
    print("Program stopped because the score is more than 30.")
    quit()

score3=float(input("Enter your score :"))
if score3 >40:
    print("Program stopped because the score is more than 40.")
    quit()

sumscore=(score1+score2+score3)
if sumscore >= 80:
    grade="A"
elif sumscore >=75:
    grade="B+"
elif sumscore >=70:
    grade="B"
elif sumscore >=65:
    grade="C+"
elif sumscore >=60:
    grade="C"
elif sumscore >=55:
    grade="D+"
elif sumscore >=50:
    grade="D"
elif sumscore >=0:
    grade="f"
else:
    grade="Error"
print("Your grade is", grade)