# Leetcode 238: Product of Array Except Self

# O(n^2) Solution
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        ans = [1] * len(nums)
        for i in range(len(nums)):
            mullist = nums[0:i] + nums[i+1:]
            for elem in mullist:
                ans[i] *= elem
        return ans
