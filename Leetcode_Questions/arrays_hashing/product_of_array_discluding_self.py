import numpy as np

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # step1: set a output list
        n = len(nums)
        pre_product = np.array([1] * n)
        suf_product = np.array([1] * n)

        # step2: prefix product
        for i in range(1, n):
            pre_product[i] = pre_product[i - 1] * nums[i - 1]
        
        # step3: suffix_product
        for i in range(n-2, -1, -1):
            suf_product[i] = suf_product[i + 1] * nums[i + 1] 

        # step4: product 2 arrays
        output = pre_product * suf_product

        return output.tolist()

# time complexity O(n)
# space complexity O(n)
       
