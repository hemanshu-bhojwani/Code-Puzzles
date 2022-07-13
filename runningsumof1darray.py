#Leetcode 1480: Running Sum of 1d Array
#Time-complexity: O(n)

class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        result = []
        for i in range(len(nums)):
            if i == 0:
                result = [nums[i]]
            else:
                result.append(nums[i] + result[i-1])
        return result
