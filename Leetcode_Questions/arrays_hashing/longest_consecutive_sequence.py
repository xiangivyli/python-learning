class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        # using set for O(1) lookup
        num_set = set(nums)

        # initialise a longest length
        longest_length = 0

        # randomly choose a num and find the start point
        for num in num_set:
            if (num - 1) not in num_set: # until find 
                current_length = 1

                while (num + current_length) in num_set:
                    current_length += 1

                # compare the streak 
                longest_length = max(longest_length, current_length)

        return longest_length

# key1: set can hold elements
# key2: using in to find num-1 and num+length
# key3: when num-1 in this set, num+length in set, iterate 
# time complexity: O(n)
# space complexity: O(n)
        
