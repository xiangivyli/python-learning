class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {} # initiate an empty dic to store value:index
        for i, value in enumerate(nums):
            complement = target - value
            if complement in hashmap:
                return [hashmap[complement], i]
            else:
                hashmap[value] = i

# hashmap and enumerate
# Time complexity O(n) and Space complexity O(n)
# The algorithm iterates through the list of numbers (nums) exactly once in a single loop. 
# Each lookup and insertion into the hashmap takes constant time O(1) average.
# The space complexity comes from the hashmap, which stores each number from nums along with its index.
