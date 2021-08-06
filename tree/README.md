#### Binary tree 
297.Serialize binary tree这个题第一次见到是在leetcode interview中，看到hard的时候倒吸一口冷气，但是BFS的方法却不难做出来。这个题的经典解法之一就是使用BFS顺序遍历每个node，并且记录在serialization中。</br>
另一类经典的方法是基于DFS，serialize很直接，按照preorder遍历记录每个node值，而只有按照preorder的serialization才会唯一对应一个tree。更具体一点，preorder遍历每个node时，左右子树分别返回serialization，root + separator + left + separator + right，就是这个root的结果。注意要有separator，可以是",", "#"等等。对于None也要有特定的字符表示，比如"#","NULL"等等。 </br>
基于DFS的deserialize稍微有些难度，因为serialization后失去了tree的结构，不能确定哪些字符对应左子树，哪些对应右子树。[第一个方法](https://github.com/arkito-ko/leetcode/blob/main/tree/297.Serialize%20and%20Deserialize%20Binary%20Tree_DFS_v1.py) 利用helper函数返回每个新建子树的root和node个数，可以找到余下的字符建立右子树。 [第二个方法](https://github.com/arkito-ko/leetcode/blob/main/tree/297.Serialize%20and%20Deserialize%20Binary%20Tree_DFS_v2.py)更加巧妙的利用queue保存所有字符，每次preorder遍历时pop出当前的root，这样左子树完成后，左子树中所有的node都pop出去了，自然剩下都是右子树。</br>
最后，考虑一下对于serialization部分的优化。每次root + left + right其实都是重新遍历left和right，然后新建一个string。[第三个方法](https://github.com/arkito-ko/leetcode/blob/main/tree/297.Serialize%20and%20Deserialize%20Binary%20Tree_DFS_v3.py)在helper函数中多使用一个prefix保存preorder遍历过的node，这样每个node只需要visit一次就可以记录下来。但是因为python中string是immutable，不能像list一样不需要返回值，直接更改list。string需要每次返回，然后在input到下一个call中。



[652.Find duplicate trees](https://github.com/arkito-ko/leetcode/blob/main/tree/652.Find%20Duplicate%20Subtrees.py) 
这个题开始的时候毫无头绪，主要难点在于如何高效的比较多个tree是否相同。如果是两个tree，暴力的想法是，遍历每个node做比较。可是如果是k个tree该如何做呢？解决这个问题其实就是将serialize tree，然后用serialized tree作为比较的对象。从第297题可以了解serialize binary tree的方法，分别是基于BFS的顺序记录每个node，以及基于DFS的基于preorder的记录root + left + right。但是这道题不仅仅是serialize一个tree，而是每个node为root的tree都要serialize，然后记录在dict中寻找重复tree。显然BFS并不适用，DFS的方法更加合适，每次结束一个DFS返回一个subtree的serialization，记录在dict中。


449. Serialize and deserialize BST
这个题与297题唯一的区别就是BST，显然297的解法可以work，即preorder或者BFS遍历树，记录所有的node（包括空children），用separator分隔。对于BST，可以利用特殊的结构简化serialization string，保存更少的字符。因为是preorder，比如A,B,C,...，B有几种情况：
* B是A的left child
* 如果A没有left，那么B可能是A的right child
* 如果A没有children，B可能是A ancester的右子树的某个位置
如何确定是哪一种情况呢？可以在递归函数中加入low and high，判断当前node是不是在这个range，如果不在就不是一个valid node。


