class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        for i, n1 in enumerate(numbers):
            n2 = target - n1
            if n2 in numbers and numbers.index(n2) > i:
                return [i + 1,numbers.index(n2) + 1]
        