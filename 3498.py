#s = "abc"
s = "zaza"
count = 0
count2 = 1
for i in s:
    if i.islower():
        position = -(ord(i) - ord('a') + 1 - 27)
    elif i.isupper():
        position = -(ord(i) - ord('A') + 1 - 27)
    
    position *= count2
    count += position
    count2 += 1
    print(count)
    
    
    