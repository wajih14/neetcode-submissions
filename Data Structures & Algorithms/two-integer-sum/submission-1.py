class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = dict()
        for i in range(len(nums)):
            n = target - nums[i]
            if (n in d.keys()):
                return [d[n], i]
            
            d[nums[i]] = i
            
        
