import math 

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        # o(n2) solution
        answers = []
        for i in range(len(nums)):
            left_prod = math.prod(nums[:i])
            right_prod = math.prod(nums[i+1:])
            final = left_prod * right_prod
            answers.append(final)
        return answers



