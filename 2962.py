nums = [61,23,38,23,56,40,82,56,82,82,82,70,8,69,8,7,19,14,58,42,82,10,82,78,15,82]

k = 2
max_ = sorted(nums)[-1]
print(nums.count(max_))
print(len(nums))
if k > nums.count(max_):
    print(0)
print((2) * max_)

