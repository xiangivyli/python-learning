class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = {}
        # count the occurrence of each num
        for num in nums:
            counter[num] = counter.get(num, 0) + 1
        # sort the sorted_counter by occurrence, and output the key list
        sorted_counter = sorted(counter, key=lambda k: counter[k], reverse=True)
        # iterate the counter dict
        return sorted_counter[:k]

# use dictionary to count the occurrence
# sorted dictionary by values with lambda
# time complexity: O(n log n)
# space complexity: O(n)
