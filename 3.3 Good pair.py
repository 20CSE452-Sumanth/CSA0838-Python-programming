def GPair(nums):
   count=0
   n=len(nums)
   for i in range(n):
      for j in range(i+1,n):
         if nums[i] == nums[j]:
            count+=1
   return count

nums = []
a=int(input("Enter the Size of the array"))
print("Enter the numbers")
for i in range(a):
    b=int(input())
    nums.append(b)
print("Good pair", GPair(nums))
