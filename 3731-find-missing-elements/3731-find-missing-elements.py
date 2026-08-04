class Solution:
    def findMissingElements(self, nums: list[int]) -> list[int]:
        if not nums:
            return []
            
        # Identify the range boundaries
        min_num = min(nums)
        max_num = max(nums)
        
        # Convert to set for O(1) time complexity checks
        nums_set = set(nums)
        
        # Build the sorted list of missing integers
        return [x for x in range(min_num, max_num + 1) if x not in nums_set]
