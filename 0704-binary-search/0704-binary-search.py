class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        n=len(nums)
        low=0
        high=n-1
        while(n!=0):
            n//=2
            mid=(low+high)//2
            if (target<nums[mid]):
                high=mid-1

            elif (target==nums[mid]):
                return mid
            
            elif (target>nums[mid]):
                low=mid+1

        return -1    

