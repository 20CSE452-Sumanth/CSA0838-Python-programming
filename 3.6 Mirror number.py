ip_number = int(input("Enter the number"))
mirror_Number = 0
while(ip_number > 0):
 Reminder = ip_number%10
 mirror_Number = (mirror_Number *10) + Reminder
 ip_number = ip_number //10
print("mirror number is = %d" %mirror_Number)
