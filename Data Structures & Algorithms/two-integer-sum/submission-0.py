class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        comps = {}

        for i in range(len(nums)):
            num = nums[i]
            if (target - num) in comps:
                return [comps[target - num], i]
            comps[num] = i
        
        return [-1,-1]