#TwoSum
#Solution using two for-loops. Time complexity O(n^2)

def twoSum(nums, target):
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if (nums[i] + nums[j]) == target:
                    return [i,j]
