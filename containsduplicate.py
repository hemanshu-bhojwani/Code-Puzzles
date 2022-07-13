#Leetcode 217: Contains Duplicate
#Time complexity: O(n)

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        dict = {}
        
        for val in nums:
            if val not in dict:
                dict[val] = 1
            else:
                return True
        return False
        
