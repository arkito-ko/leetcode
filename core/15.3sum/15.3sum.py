# Solution 1
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        if n < 3:
            return []
        nums.sort()
        ret = []

        for start in range(n - 2):
            if start == 0 or nums[start] != nums[start - 1]:
                target = -nums[start]
                left, right = start + 1, n - 1
                while left < right:
                    tmp = nums[left] + nums[right]
                    if tmp == target:
                        if left == start + 1 or nums[left] != nums[left - 1]:
                            ret.append([nums[start], nums[left], nums[right]])
                        left += 1
                        right -= 1
                    elif tmp < target:
                        left += 1
                    else:
                        right -= 1

        return ret


