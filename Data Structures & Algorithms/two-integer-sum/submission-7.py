class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        for i, n1 in enumerate(nums):
            n2 = target - n1
            if n2 in nums and nums.index(n2) != i:
                return sorted([i, nums.index(n2)])
            
