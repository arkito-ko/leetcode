#### Sliding window 

992这道hard题目很有意思，让我们理解了sliding window的常规思路可以解决713和340中“less than k" "At most k"这样的问题，而“exactly k"这样的问题虽然更加specific，可是无法用sliding window的常规思路求解。所以992的难点就在于，当条件变成"exactly k"的时候，无法用sliding window常规求解，而关键解法就在于利用atMost(k) - atMost(k-1)求解。

做过713和340后，atMost(k)这样的问题就不难解决。关键在于，遍历right指针，符合条件时更新结果；不符合条件时，移动left指针直到满足条件，再更新结果。区别在于，713求解subarray数目，所以对于每个符合条件的right指针，需要`count = right - left + 1`求得个数；而340需要求"longest subarray"，所以对于每个符合条件的right指针，只需要得到当前的长度`right - left + 1`而不用去加入count。