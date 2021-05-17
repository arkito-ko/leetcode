#### 15.3Sum 

#### 3Sum是一道重要的双指针问题，需要熟练掌握。几个关键的地方：
1. 思路是借助two sum的方法，增加一层for循环；
2. 需要查重。排序后查重更容易，有两种方法；
3. 方法1：类似于DFS combination sum/subset两道题，检查`i == start_idx or nums[i] != nums[i - 1]`；
4. 方法2: 在找到一组解的if语句內，while循环left和right，直到不再重复

