L = [4,5,3,1,7]
L2 = []

last_element = len(L)-1
for i in range(last_element,-1,-1):
    L2.append(L[i])
print(L2)