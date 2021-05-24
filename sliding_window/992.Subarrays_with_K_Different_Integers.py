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