class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()

        for i , val in enumerate(nums):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            l,r = i+1, len(nums) -1
            while l < r:
                total = val + nums[l] + nums[r]
                if total > 0:
                    r = r - 1
                elif total < 0:
                    l = l + 1
                else:
                    res.append([val,nums[l],nums[r]])
                    l = l + 1
                    r = r - 1
                    while l < r and nums[l] == nums[l-1]:
                        l = l + 1
                    while l < r and nums[r] == nums[r+1]:
                        r = r - 1
        return res
                    
        