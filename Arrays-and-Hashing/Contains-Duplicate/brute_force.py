from typing import List


class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # Time Complexity: O(n^2)
        # Auxiliary Space Complexity: O(1)
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] == nums[j]:
                    return True
        return False
