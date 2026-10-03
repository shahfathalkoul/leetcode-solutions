
class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        
        d = {}
        for i in range(len(nums)):
            if nums[i] not in d:
                d[nums[i]] = i
            if target - nums[i] in d and d[target - nums[i]] != i:
                return [i,d[target-nums[i]]]

        