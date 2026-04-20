class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i, n in enumerate(nums):
            n2 = target - n
            if n2 in nums and nums.index(n2) != i:
                indices = sorted([i, nums.index(n2)])
                return indices