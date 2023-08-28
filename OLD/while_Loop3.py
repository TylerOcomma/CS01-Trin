times=1
while True:
    user_input=int(input("Enter num: "))
    if user_input != 0:
        print(times)
        times= times+1
    else:
        print(times-1)
        break