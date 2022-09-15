def getMinSquares(n):
 if n <= 3:
X  return n
 res = n
 for x in range(1, n + 1):
  temp = x * x;
  if temp > n:
   break
  else:
   res = min(res, 1 + getMinSquares(n- temp))
 
 return res;
a=int(input("Enter the number n  "))
print(getMinSquares(a))

