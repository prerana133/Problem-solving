s = "madam"
startchar = 0
lastchar = len(s)-1
 
while startchar<lastchar:
    if s[startchar]!=s[lastchar]:
        print("not palindrom")
    lastchar-=1
    startchar+=1
else:
    print("palindrom")


s = "madam"
lastindx = len(s)-1
new = ""
for i in range(lastindx,-1,-1):
    new += s[i]

if s == new:
    print("palindrom")
else:
    print("Not")
 

