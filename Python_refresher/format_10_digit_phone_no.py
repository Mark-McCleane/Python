#format a 10 digit phone number
#Author: Mark McCleane

phoneNumber = str(input("Enter Phone No: ") )
print phoneNumber[0]

phoneNumberPrinted = "(" + phoneNumber[:3]+ ") "+ phoneNumber[3:6] + "-" + phoneNumber[6:]

print(phoneNumberPrinted)