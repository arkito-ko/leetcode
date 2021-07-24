# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import defaultdict
class Solution:
    def findDuplicateSubtrees(self, root: TreeNode) -> List[TreeNode]:
        self.serialized_tree_count = defaultdict(int)
        ret = []
        _ = self.serialize_tree(root, ret)
        return ret
    
    def serialize_tree(self, root, ret):
        if root is None:
            return "#"
        
        tree_string = str(root.val)
        tree_string += "," + self.serialize_tree(root.left, ret) + "," + self.serialize_tree(root.right, ret)
        
        self.serialized_tree_count[tree_string] += 1
        if self.serialized_tree_count[tree_string] == 2:
            ret.append(root)
        
        return tree_string