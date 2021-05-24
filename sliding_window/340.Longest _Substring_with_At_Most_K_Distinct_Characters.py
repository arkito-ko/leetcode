class Solution:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        if k == 0:
            return 0
        
        n = len(s)
        left = 0
        max_len = 0
        sliding_window = {}
        
        for right in range(n):
            sliding_window[s[right]] = right
            while left <= right and len(sliding_window) > k:
                if sliding_window[s[left]] == left:
                    del sliding_window[s[left]]
                left += 1
            
            max_len = max(max_len, right - left + 1)
        
        return max_len