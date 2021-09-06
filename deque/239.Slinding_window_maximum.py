"""
239. Sliding window maximum
You are given an array of integers nums, there is a sliding window of size k which is moving from the very left of the array to the very right. You can only see the k numbers in the window. Each time the sliding window moves right by one position.

Return the max sliding window.
"""

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
    	"""
    	use a deque to maintain a decreasingly monotone stack
    	Think about why decreasing? 
    	In addition, keep deque updated with the sliding window
    	deque[0] is the max in the current window
    	"""

    	mono_deque = collections.deque()
    	ret = []

    	for i in range(len(nums)):
    		# remove nums not in the sliding window
    		leftmost = i - k
    		while mono_deque and mono_deque[0] <= leftmost:
    			mono_deque.popleft()

    		# maintain a decreasingly monotone stack
    		while mono_deque and nums[mono_deque[-1]] <= nums[i]:
    			mono_deque.pop()

    		mono_deque.append(i)

    		if i >= k - 1:
    			ret.append(nums[mono_deque[0]])

    	return ret