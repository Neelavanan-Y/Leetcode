class Solution(object):
    def shuffle(self, nums, n):
        s=[]
        for i  in range(len(nums)/2):
            s.append(nums[i])
            s.append(nums[i+n])
        return s