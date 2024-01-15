#
# @lc app=leetcode id=9 lang=python3
#
# [9] Palindrome Number
#

# @lc code=start
class Solution:
    def isPalindrome(self, x: int) -> bool:
        return x == Solution.rev(x)
    
    def rev(num: int) -> int:
        reversed_num = 0
        while num > 0:
            reversed_num = (reversed_num * 10) + (num % 10)
            num = num // 10
        return reversed_num

        
# @lc code=end

