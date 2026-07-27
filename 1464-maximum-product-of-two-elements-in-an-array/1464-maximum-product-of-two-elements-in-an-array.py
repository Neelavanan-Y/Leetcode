class Solution(object):
    def maxProduct(self, nums):
       c=max(nums)
       nums.remove(c)
       d=max(nums)
       return (c-1)*(d-1)