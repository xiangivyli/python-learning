class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        # using set for O(1) lookup
        num_set = set(nums)

        if len(num_set) == 1:
            return 1

        # initialise a longest streak
        longest_streak = 0

        # randomly choose a num and find the smallest 
        for num in num_set:
            if num - 1 in num_set: # until not find 
                current_num = num 
                current_streak = 2

                while current_num + 1 in num_set:
                    current_num += 1
                    current_streak += 1

                # compare the streak 
                longest_streak = max(longest_streak, current_streak)

        return longest_streak

# key1: set can hold elements
# key2: using in to find num-1 and num+1
# time complexity: O(n)
# space complexity: O(n)
