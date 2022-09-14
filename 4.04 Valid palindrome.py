a=input("enter the string")
s=''.join(filter(str.isalpha,a))
s=s.lower()
if(s == s[::-1]):
    print("True")
else:
    print("False")
          
