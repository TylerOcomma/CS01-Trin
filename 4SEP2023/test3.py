x = int(input("Input: "))
result=0

for num in range(x):
    result+=1
    if result %3==0 or result %5 ==0:
        print(result)
    else:
        continue