# Leetcode 53: Maximum Subarray
# O(n^2) Solution

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_sum = -10000
        if len(nums) == 1:
            return nums[0]
        
        for i in range(len(nums)):
            for j in range(i+1, len(nums)+1):
                if sum(nums[i:j]) > max_sum:
                    max_sum = sum(nums[i:j])
        return max_sum

# O(n) Solution
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        sum = nums[0]
        res = nums[0]
        
        for i in range(1,len(nums)):

            sum = max(nums[i], sum+nums[i])
        
            if sum > res:
                res = sum
        return res
