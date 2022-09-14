from itertools import permutations
s=int(input("Enter the size of the list"))
a=[]
print("Enter the elements in the list")
for i in range(s):
    b=int(input())
    a.append(b)
a=list(dict.fromkeys(a))
c=permutations(a)
print("The possible permuatations for the given list",a)
for i in (c):
    print(i)
