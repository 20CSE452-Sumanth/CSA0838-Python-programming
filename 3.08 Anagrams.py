from collections import defaultdict
l= []
a=int(input("No of Words in the list"))
b=print("Enter the words")
for i in range(a):
    b=input()
    l.append(b)
print("The original list : " + str(l))
temp = defaultdict(list)
for ele in l:
    temp[str(sorted(ele))].append(ele)
res = list(temp.values())

print("The grouped Anagrams : " + str(res))
