class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # how to find the lowerest point and highest point
        # the highest point is on the right as index is time
        min_so_far = prices[0]
        max_difference = 0

        # iterate from the second element
        for i in range(1, len(prices)):
            current_difference = prices[i] - min_so_far

            # update max_difference if the current_difference is larger
            max_difference = max(max_difference, current_difference)

            # update min_so_far
            min_so_far = min(min_so_far, prices[i])


        return max_difference

# time complexity: O(n)
# space complexity: O(1)
