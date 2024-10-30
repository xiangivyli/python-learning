class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        return len(nums) != len(set(nums))

#time complexity: O(n)
#space complexity: O(n)

class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seen = set()
        for num in nums:
            if num in seen:
                return True
            seen.add(num)
        return False
#more efficient, as it may stop early 
#time complexity: O(n)
#space complexity: O(n) 
