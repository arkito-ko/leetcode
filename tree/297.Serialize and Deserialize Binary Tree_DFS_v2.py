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
        # root, tree_size = self._deserialize(data_list, 0)
        root = self._deserialize_v2(data_list)
        return root

    def _deserialize_v2(self, data_list):
        if len(data_list) == 0:
            return None
        
        val = data_list.popleft()
        if val == "#":
            return None
        else:
            root = TreeNode(val)
            root.left = self._deserialize_v2(data_list)
            root.right = self._deserialize_v2(data_list)
            return root 
            