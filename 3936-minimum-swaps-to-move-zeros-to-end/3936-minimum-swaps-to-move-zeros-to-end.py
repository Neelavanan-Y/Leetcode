class Solution(object):
    def minimumSwaps(self, nums):
        n = nums.count(0)
        m = nums[len(nums)-n:].count(0)
        return n - m
        