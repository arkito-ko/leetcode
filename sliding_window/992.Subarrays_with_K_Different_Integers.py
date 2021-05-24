"""
992. Subarrays with K Different Integers
Given an array nums of positive integers, call a (contiguous, not necessarily distinct) subarray of nums good if the number of different integers in that subarray is exactly k.

(For example, [1,2,3,1,2] has 3 different integers: 1, 2, and 3.)

Return the number of good subarrays of nums.

Example 1:

Input: nums = [1,2,1,2,3], k = 2
Output: 7
Explanation: Subarrays formed with exactly 2 different integers: [1,2], [2,1], [1,2], [2,3], [1,2,1], [2,1,2], [1,2,1,2].

Example 2:

Input: nums = [1,2,1,3,4], k = 3
Output: 3
Explanation: Subarrays formed with exactly 3 different integers: [1,2,1,3], [2,1,3], [1,3,4].
"""
class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        return self.subarraysAtMost(nums, k) - self.subarraysAtMost(nums, k - 1)
    
    def subarraysAtMost(self, nums, k):
        left = 0 
        count = 0
        window = {}
        
        for right in range(len(nums)):
            window[nums[right]] = right
            # if len(window) <= k:
            #     count += right - left + 1
            # else:
            #     while left <= right and len(window) > k:
            #         if window[nums[left]] == left:
            #             del window[nums[left]]
            #         left += 1
            #     count += right - left + 1
            
            while left <= right and len(window) > k:
                if window[nums[left]] == left:
                    del window[nums[left]]
                left += 1
            
            count += right - left + 1            
        
        return count 