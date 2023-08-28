times=1
sum=0
while True:
    user_input=int(input("Enter num: "))
    if times == 10:
        break
    elif user_input<0:
        times =times+1
        pass
    else:
        times+=1
        sum+=user_input

print(sum)