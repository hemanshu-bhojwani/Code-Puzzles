# Leetcode 125: Valid Palindrome
# Time Complexity O(n)

class Solution:
    def isPalindrome(self, s: str) -> bool:
        clean = ""
        for char in s:
            if (97 <= ord(char) <=122) or (65 <= ord(char) <= 90) or (48 <= ord(char) <= 57):
                clean += char.lower()
        
        length = len(clean)
        
        for i in range(length):
            if clean[i] != clean[length-i-1]:
                return False
        return True
