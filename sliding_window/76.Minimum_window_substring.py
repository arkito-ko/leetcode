class Solution:
    def minWindow(self, s: str, t: str) -> str:
        n = len(s)
        target = collections.Counter(t)
        min_substring = ""
        min_len = n + 1
        left = 0
        window = collections.defaultdict(int)
        count = 0
        
        for right in range(n):
            window[s[right]] += 1
            if window[s[right]] == target[s[right]]:
                count += 1
            
            while left <= right and count == len(target):
                substring_len = right - left + 1
                if substring_len < min_len:
                    min_len = substring_len
                    min_substring = s[left:right+1]
                    
                if window[s[left]] == target[s[left]]:
                    count -= 1
                window[s[left]] -= 1
                left += 1
        
        return min_substring