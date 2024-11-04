class Solution:
    def maxArea(self, heights: List[int]) -> int:

        # the length equals differences of indexes
        left, right = 0, (len(heights) - 1)

        # initilise the product
        product = 0
        
        # start to move
        while left < right:

            width = right - left
            height = min(heights[left], heights[right])

            current_area = width * height

            product = max(product, current_area)
            # when the left bar is higher
            # calculate the product
            if heights[left] > heights[right]:
                # move the right bar to find a higher one
                right -= 1
        

            # when the right bar is higher or equal
            else:
                # move the right bar to find a higher one
                left += 1


        return product



# how to make the bar to make sure the product is largest
# 1. only move the shorter bar
# 2. combine if and while to move pointers until getting the max
# time complexity: O(n)
# space complexity: O(1)
