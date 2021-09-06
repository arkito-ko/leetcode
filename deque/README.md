#### Deque used as a monotone stack
239. Sliding window maximum
这个题brute force的解法是比较明显的，每个长度为k的sliding window都求出最大值，复杂度是O((n-k)k).显然这样做是有很多重复计算的，因为每次window只移动一格，delete the leftmost and add one from the right，所以只有两个变动的元素。如果sliding window是一个有序的data structure，每次删除一个添加一个，很可能复杂度是logk，那么最后复杂度就是O(nlogk)。第一次解题的时候使用了heap，保存了(-num, index)， 最大值保存在heap[0]中，保存index目的在于确保heap中的最大值的index在window中。

这道题最优的解法是O(n)，而且是一个典型利用deque作为monotone stack的题目。monotone stack是保存数组index的一个increasing or decreasing stack，比如一个decreasing monotone stack，deque[0]保存最大值的index，deque当中index对应的数值是递减的。遇到小于nums[deque[-1]]的数值，将它的的index加入deque；遇到大于nums[deque[-1]]的数值，使用while从后向前移出deque的元素直到不再大于。那么这道题为什么要使用monotone stack呢？因为我们只关心一个window中的最大值，以及index排它在后面的第二小，第三小，等等的cadidates。如果只关心最大值，那么只需要一个track一个key就可以，但是如果只关心最大值，那么当最大值被移出window，下个candidate怎么找呢？所以需要保存其他的candidates。为什么要decreasing stack呢？因为如果更大的值出现在靠后的位置，那么前面比它小的肯定不需要track了，我们需要track现在window的最大值，还需要track排在它后面的即时没有它大的值。如果只需要decreasing stack，常规的queue就可以，那么为什么要用deque呢？因为还需要检查当前的deque[0]是不是还在window中，这也是deque中保存index而不是value的原因。

总结一下，使用deque作为monotone stack，可以(1)保存极值在deque[0]；(2)deque中是递减或者递增的; (3)deque中保持了在数组中的位置，可以从front删除更早的元素。