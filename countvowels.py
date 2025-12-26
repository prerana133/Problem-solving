s = "prerana"
count = 0
for ch in s:
    if ch in "aeiouAEIOU":
        count+=1
print(count)


s = "prerana"
vowel = []
for ch in s:
    if ch in "aeiouAEIOU":
        vowel.append(ch)
print(vowel)