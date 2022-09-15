class Solution:
    def findPeakElement(self, nums: list[int]) -> int:
        low, high = 0, len(nums) - 1
        
        while low <= high:
            mid = (low + high)//2
            left_val = float('-inf') if mid == 0 else nums[mid - 1]
            right_val = float('-inf') if mid == len(nums) - 1 else nums[mid + 1]
            
            if left_val < nums[mid] and nums[mid] > right_val:
                return mid 
            if left_val < nums[mid] < right_val:
                low = mid + 1
                continue   
            if left_val > nums[mid] > right_val:
                high = mid - 1
                continue
            low = mid + 1
        return 0
obl=Solution()
a=[]
b=int(input("Enter the size of the array"))
print("Enter the elements")
for i in range(b):
    c=int(input())
    a.append(c)
print(obl.findPeakElement(a))
