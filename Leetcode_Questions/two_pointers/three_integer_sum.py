class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        if len(nums) < 3:
            return []

        # sort the nums list
        nums.sort()

        # initialise a list
        output = []

        # locate the 1st pointer
        for i in range(len(nums) - 2):
            if i > 0 and nums[i] == nums[i-1]:
                continue

            # locate 2nd and 3rd pointers
            left, right = i+1, len(nums)-1

            # find sum 0
            while left < right:
                total = nums[i] + nums[left] + nums[right]

                if total == 0:
                    output.append([nums[i], nums[left], nums[right]])
                    left += 1
                    right -= 1 

                    # skip duplicates
                    while left < right and nums[left] == nums[left-1]:
                        left += 1
                    while left < right and nums[right] == nums[right+1]:
                        right -= 1


                elif total < 0:
                    left += 1
                
                else:
                    right -= 1

        return output

            

# key: the triplets are distinct! using continue and == to skip duplicates
# time complexity: O(n^2)
# space complexity: O(n)

