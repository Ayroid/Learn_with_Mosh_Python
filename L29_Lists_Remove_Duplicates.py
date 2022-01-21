# My Method

number = [1,2,3,4,5,6,7,1,2,3,4,5,6]

for i in number:
    cnt = number.count(i)
    while(cnt>1):
        number.remove(i)
        cnt-=1
    i+=1

print(number)

# Method in the video

number = [1,2,4,1,3,5,1,2,4,3]
unique = []
for i in number:
    if i not in unique:
        unique.append(i)

print(unique)