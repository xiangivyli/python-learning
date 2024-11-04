class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # O(1) means no new list created
        left, right = 0, len(numbers)-1

        while left < right:
            current_sum = numbers[left] + numbers[right]
            if current_sum == target:
                return [left+1, right+1]
            elif current_sum < target:
                left += 1
            else:
                right -= 1

# key: 2 pointers do not move at the same time
# time complexity: O(n)
# space complexity: O(1)
