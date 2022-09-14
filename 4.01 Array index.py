answer=[]
a=int(input("Enter the number"))
for i in range(1,a+1):
    if (i%3==0 and i%5==0):
        answer.append("FizzBuzz")
    elif (i%3==0):
        answer.append("Fizz")
    elif (i%5==0):
        answer.append("Buzz")
    else:
        answer.append(i)

print(answer)
