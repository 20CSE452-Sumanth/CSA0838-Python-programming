t_1=[]
t_2=[]
a=int(input("List 1 range"))
print("Enter the elements in list 1")
for i in range(a):
    t1=int(input())
    t_1.append(t1)
b=int(input("List 2 range"))
print("Enter the elements in list 2")
for j in range(b):
    t2=int(input())
    t_2.append(t2)

res=sorted(t_1+t_2)
print("the coombined sorted list is:"+str(res))
