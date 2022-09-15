def solve(n):
    print("Pascal Triangle")
    for i in range(n+1):
        for j in range(n-i):
            print(' ',end='')
        C=1
        for j in range(1,i+1):
            print(C,' ',sep='',end='')
            C=C*(i-j)//j
        print()

class PascalTriangle :
	#  Sum of given row in pascal triangle
	def sumPascalRow(self, n) :
		if (n <= 0) :
			return
		#  Assume number is not overflow
		sum = (1 << n)
		print("Sum of elements in ",n+1,"th row is ",sum ," ")
	
b=int(input("Enter no of rows"))
a=int(input("Enter the row number"))
solve(b)
def main() :
    task = PascalTriangle()
    task.sumPascalRow(a-1)

if __name__ == "__main__": main()
