l = [2,4,5,6,5,6]
duplicate = []

for i in range(len(l)+1):
    for j in range(i+1,len(l)):
        if l[i]==l[j]:
            duplicate.append(l[i])
print(duplicate)


