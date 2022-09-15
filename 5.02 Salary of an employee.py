a=input("Enter the grade of the employee ")
s=int(input("Enter the salary of the employee "))
b1=0
bonus=0
if(s<10000):
    b1=s/2
if a=='A':
    bonus = s*0.05
    print("Bonus",bonus)
if a=='B':
    bonus = s*0.1
    print("Bonus ",bonus)
print("TOtal to be paid ",s+bonus+b1)
