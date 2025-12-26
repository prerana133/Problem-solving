S = "prerana"
temp = ""
for i in S:
    temp = i+temp
print(temp)

S = "Rohan" 
lastchar = len(S)-1
rev = ""
for i in range(lastchar,-1,-1):
    rev+=S[i]
print(rev)