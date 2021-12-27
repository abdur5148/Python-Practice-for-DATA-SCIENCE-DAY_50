import re
var1 = input("Enter Email : ")
num1 = re.split("@|.com", var1)
print(num1[1])
