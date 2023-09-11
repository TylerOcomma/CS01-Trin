score1=str(input("Enter your score : "))

if str(score1) == "W":
    print("ติด ร")
    quit()

score1float=float(score1)

if score1float >30:
    print("Program stopped because the score is more than 30")
    quit()

score2=float(input("Enter your score : "))
if score2 >20:
    print("Program stopped because the score is more than 30.")
    quit()

score3=float(input("Enter your score : "))
if score3 >30:
    print("Program stopped because the score is more than 40.")
    quit()

score4=float(input("Enter your score : "))
if score4 >20:
    print("Program stopped because the score is more than 40.")
    quit()


sumscore=(score1float+score2+score3+score4)
if sumscore >= 80:
    grade="4"
elif sumscore >=75:
    grade="3.5"
elif sumscore >=70:
    grade="3"
elif sumscore >=65:
    grade="2.5"
elif sumscore >=60:
    grade="2"
elif sumscore >=55:
    grade="1.5"
elif sumscore >=50:
    grade="1"
elif sumscore >=0:
    grade="0"
else:
    grade="Error"
print("Your grade is", grade)