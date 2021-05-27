#### Sliding window 

[992.Subarrays with k different integers](https://github.com/arkito-ko/leetcode/blob/main/sliding_window/992.Subarrays_with_K_Different_Integers.py) 这道hard题目很有意思，让我学到了sliding window的常规做法可以解决713和340中“less than k" "At most k"这样的问题，而“exactly k"这样的问题虽然搜索目标更加specific，可是无法用sliding window的常规求解。所以992的难点就在于，当条件变成"exactly k"的时候，无法用sliding window常规求解，而关键解法就在于求解问题subarrays with at most k different (distinct) integers， 然后atMost(k) - atMost(k-1)。

做过713和340后，atMost(k)这样的问题就不难解决。思路是，遍历right指针，符合条件时用当前的left和right所得到的sliding window更新结果；不符合条件时，移动left指针直到满足条件，再用新的sliding window更新结果。每个符合条件的sliding window可以看作是以right为结尾的最长的window。

下面是713和340的区别在于选择subarray的条件不同，以及要求的结果不同：</br>
[713.Subarray product less than k](https://github.com/arkito-ko/leetcode/blob/main/sliding_window/713.Subarray_Product_Less_Than_K.py)求符合条件subarray数目，这个与992相同。而条件是数字乘积不大于k，这个与992不同。求subarrat个数的问题，在找到最大的subarray (sliding window)，需要`count = right - left + 1`求以right作为尾数的满足条件的subarray个数。这道题也可以求"longest subarray with product less than k"。

[340.Longest substring with at most k distinct characters](https://github.com/arkito-ko/leetcode/blob/main/sliding_window/340.Longest%20_Substring_with_At_Most_K_Distinct_Characters.py) 求符合条件的"longest subarray"，这个与992不同。但是条件是k distinct characters，这与992类似。在找到最大的subarray (sliding window)，只需要得到当前的长度`right - left + 1`而不用去加入count。类似的，这道题也可以求"substrings with at most k distinct characters"。
