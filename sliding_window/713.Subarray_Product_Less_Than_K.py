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