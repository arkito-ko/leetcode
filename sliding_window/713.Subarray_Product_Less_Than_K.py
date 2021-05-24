"""
Your are given an array of positive integers nums.

Count and print the number of (contiguous) subarrays where the product of all the elements in the subarray is less than k.

Example 1:
Input: nums = [10, 5, 2, 6], k = 100
Output: 8
Explanation: The 8 subarrays that have product less than 100 are: [10], [5], [2], [6], [10, 5], [5, 2], [2, 6], [5, 2, 6].
Note that [10, 5, 2] is not included as the product of 100 is not strictly less than k.
"""

class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        if k == 0 or k == 1 or len(nums) == 0:
            return 0

        ret = 0
        left = 0
        prefix = 1
        for right in range(len(nums)):
            prefix *= nums[right]
            while prefix >= k and left <= right:
                prefix /= nums[left]
                left += 1

            # if left <= right:
            #     ret += (right - left + 1)
            ret += (right - left + 1)
            
        return ret 