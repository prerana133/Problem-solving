num = 121
temp = num
rev = 0

while temp > 0:
    digit = temp % 10
    rev = rev*10+digit
    temp = temp//10
if num==rev:
    print("palindrom")
else:
    print("not")


num = 121
temp = num
rev = 0 

while temp !=0:
    rev = rev*10+(temp%10)
    temp = temp//10
if num == rev :
    print("palindrome")
        
else:
     print("Not")



