class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for n in range(len(nums)):
            for n2 in range(n+1,len(nums)):
                if (target - nums[n]) == nums[n2]:
                    return [n,n2]
                
        