class Solution:
    def differenceOfSum(self, nums: List[int]) -> int:
        count = 0
        for i in nums:
            for j in str(i):
                count += int(j)
        return (abs(count - sum(nums)))