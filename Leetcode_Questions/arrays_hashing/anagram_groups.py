class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap = {} # initiate an empty dic to store values
        for word in strs:
            # sorted return a list which is mutable and unhashable
            sorted_word = "".join(sorted(word))
            # create an empty list for each group
            if sorted_word not in hashmap:
                hashmap[sorted_word] = []
            # using sorted_word as key to put grouped anagrams together
            hashmap[sorted_word].append(word)

        return list(hashmap.values())


# 1. using hashmap + sorted anagram as the key to classify anagrams
# 2. using list to read hashmap values
# time complexity: O(n * k log k), k:avg length of words, n: the number of words
# space complexity: O(n * k)
