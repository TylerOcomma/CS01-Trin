sum=0
while True:
    user_input=int(input("Enter num: "))
    sum+=user_input
    if sum <= 100:
        print(user_input)
    else:
        print(sum)
        break