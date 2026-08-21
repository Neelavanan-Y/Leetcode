class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        sum_val = 0
        max_len = 0
        prefix_sum = {sum_val : -1}

        for i, num in enumerate(nums):
            sum_val += 1 if num == 1 else -1
            if sum_val not in prefix_sum:
                prefix_sum[sum_val] = i
            else:
                max_len = max(max_len, i - prefix_sum[sum_val])
        return max_len