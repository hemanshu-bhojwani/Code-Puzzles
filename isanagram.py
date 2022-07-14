#Leetcode 242: Valid Anagram
# Time complextiy: O(n)
# Using dictionaries.

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hash1 = {}
        hash2 = {}
        
        if len(s) != len(t):
            return False
        
        for i in range(len(s)):
            if s[i] not in hash1:
                hash1[s[i]] = 1
            else:
                hash1[s[i]] += 1
        
        for i in range(len(t)):
            if t[i] not in hash2:
                hash2[t[i]] = 1
            else:
                hash2[t[i]] += 1
                
        if hash1 == hash2:
            return True
        
        return False
      
# One line solution
# Time Complexity: O(n log n)

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return sorted(s) == sorted(t)
