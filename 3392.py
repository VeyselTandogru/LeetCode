nums = [1, 2, 1, 4, 1]
n = len(nums)
k = 3
count = 0
for i in range(n - k + 1):
        subarray = nums[i:i+k]
        if (subarray[0] + subarray[2]) == (subarray[1]/2):
                count += 1
print(count)

