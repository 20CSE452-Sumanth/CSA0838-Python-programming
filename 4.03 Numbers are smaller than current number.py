a=int(input("Enter the size of the array"))
nums=[]
result=[]
for i in range(a):
    b=int(input())
    nums.append(b)
for i in range(a):
    c=0
    for j in range(a):
        if i!=j and nums[j]<nums[i]:
            c=c+1
    result.append(c)
print(result)
