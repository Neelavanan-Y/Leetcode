class Solution(object):
    def majorityElement(self, nums):
        s=set(nums)
        max=0
        for i in s:
            if max<(nums.count(i)):
                max=nums.count(i)
                m=i
        return m
