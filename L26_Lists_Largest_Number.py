nums = [10,3,2,5,23,43,2,3,4,2,32]
lar = nums[0]
i = 1
for i in nums:
    if(lar<i):
        lar = i
    i+=1
print(f"Largest Number in the List is {lar}")