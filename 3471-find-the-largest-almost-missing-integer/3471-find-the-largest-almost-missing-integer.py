class Solution:
    def largestInteger(self, nums: List[int], k: int) -> int:
        c = {}
        for i in range(len(nums) - k + 1):
            n = set(nums[i:(i + k)])
            for x in n:
                c[x] = c.get(x, 0) + 1
        ans = -1
        for x, freq in c.items():
            if freq == 1:
                ans = max(ans, x)
        return ans