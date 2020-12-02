# Literal First Time Coding in Python why is this so hard god help me
file = open("Receipt.txt", "r")
nums = []
for l in file:
    nums.append(l.strip())
print(nums)
def Front(nums):
    #aaaaaaaaaaaaa
    for a in nums:
        for b in nums:
            if int(a)+int(b) == 2020:
                return int(a)*int(b)
def Back(nums):
    for a in nums:
        for b in nums:
            for c in nums:
                if int(a)+int(b)+int(c) == 2020:
                    return int(a)*int(b)*int(c)


print(Front(nums))
print(Back(nums))
