# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        if root is None:
            return "#"
        else:
            return str(root.val) + "," + self.serialize(root.left) + "," + self.serialize(root.right)  


    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        data_list = data.split(",")
        data_list = collections.deque(data_list)
        root, tree_size = self._deserialize(data_list, 0)
        return root
    
    def _deserialize(self, data_list, start_idx):
        if data_list[start_idx] == "#":
            return None, 1
        
        root = TreeNode(data_list[start_idx])
        root.left, left_size = self._deserialize(data_list, start_idx + 1)
        root.right, right_size = self._deserialize(data_list, start_idx + left_size + 1)
        return root, left_size + right_size + 1