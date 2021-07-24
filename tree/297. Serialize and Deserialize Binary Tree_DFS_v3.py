# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:
	def serialize(self, root):
        if root is None:
            return "#"
        else:
        	# need to return data from _serialize
        	# ret = "" won't work because string is not immutable in python
        	# everytime ret will be a new string 
            data = self._serialize(root, "")
            return data
        
    def _serialize(self, root, data):
        if root is None:
            return data + "," + "#"
        
        if data == "":
            data += str(root.val)
        else:
            data += "," + str(root.val)
        
        data = self._serialize(root.left, data)
        data = self._serialize(root.right, data)
        return data 

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

            