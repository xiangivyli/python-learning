class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # step1: set a output list
        n = len(nums)
        output = [1] * n

        # step2: prefix product
        for i in range(1, n):
            output[i] = output[i - 1] * nums[i - 1]
        
        # step3: suffix product
        product = 1
        for i in range(n-2, -1, -1):
            product *= nums[i + 1]
            output[i] = output[i] * product

        return output

# time complexity O(n)
# space complexity O(n) 
       
