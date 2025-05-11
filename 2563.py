nums = [0,1,7,4,4,5]
nums = sorted(nums)
lower = 3
upper = 6
count = 0
n = len(nums)
i = n - 2
j = n -1
while i >= 0:
    sum_ = nums[i] + nums[j]
    
