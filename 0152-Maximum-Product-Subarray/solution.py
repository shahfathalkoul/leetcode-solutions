class Solution:
    def maxProduct(self, nums: list[int]) -> int:
        def dp(i,sum1):
            if i >= len(nums) - 1:
                return 0
            take = 1
            if sum1 * nums[i] > 1:
                take = dp(i + 1, sum1 * nums[i])
            not_take = dp(i + 1, sum1)
            return max(take,not_take)
        return dp(0,1)

        