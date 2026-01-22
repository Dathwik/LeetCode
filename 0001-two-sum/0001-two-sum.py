class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
         numMap = {}

         for i, num in enumerate(nums):
            if target - num in numMap:
                return [i, numMap[target - num]]
            numMap[num] = i

        