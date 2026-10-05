class Solution:
    def maxProduct(self, nums: list[int]) -> int:
        memo = {}

        def dp(i, max1, min1):
            if i == len(nums):
                return max1

            if i in memo:
                return memo[i]

            cur_max = max(nums[i], max1 * nums[i], min1 * nums[i])
            cur_min = min(nums[i], max1 * nums[i], min1 * nums[i])

            memo[i] = max(cur_max, dp(i + 1, cur_max, cur_min))
            return memo[i]

        return dp(1, nums[0], nums[0])