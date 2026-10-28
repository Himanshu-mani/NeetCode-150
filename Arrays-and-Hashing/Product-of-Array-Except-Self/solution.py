
from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        output = [1] * n

        # Step 1: Store prefix products
        left = 1
        for i in range(n):
            output[i] = left
            left *= nums[i]

        # Step 2: Multiply by suffix products
        right = 1
        for i in range(n - 1, -1, -1):
            output[i] *= right
            right *= nums[i]

        return output


# Time Complexity: O(n)
# Auxiliary Space Complexity: O(1)
# Output Space Complexity: O(n)
