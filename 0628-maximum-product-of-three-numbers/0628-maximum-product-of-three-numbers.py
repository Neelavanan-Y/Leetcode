class Solution(object):
    def maximumProduct(self, nums):
        nums.sort()
        # Product of the three largest numbers
        prod1 = nums[-1] * nums[-2] * nums[-3]
        # Product of the two smallest numbers and the largest number
        prod2 = nums[0] * nums[1] * nums[-1]
        
        return max(prod1, prod2)