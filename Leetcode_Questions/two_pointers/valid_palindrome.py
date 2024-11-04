class Solution:
    def isPalindrome(self, s: str) -> bool:
        # extract only alphanumerical characters
        pure_s = "".join(char.lower() for char in s if char.isalnum())

        # set two pointers
        left, right = 0, len(pure_s) - 1

        # compare
        while left < right:
            if pure_s[left] != pure_s[right]:
                return False
            left += 1
            right -= 1
                    
        return True

# 2 pointers to set the first num and then move to the middle
# time complexity: O(n)
# space complexity: O(n)
