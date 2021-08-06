# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root: TreeNode) -> str:
        """Encodes a tree to a single string.
        """
        """
        Compared to regular binary trees, take advantage of
        BST's structure to skip marking empty children, instead,
        locate its position by comparing the value with node and 
        parent. In preorder, the next node could be left child or 
        right child or parent's right child, depending on its value.
        """
        if root is None:
            return ""
        
        ret = str(root.val)
        if root.left:
            ret += "," + self.serialize(root.left)
        if root.right:
            ret += "," + self.serialize(root.right)
        
        return ret 
        
        

    def deserialize(self, data: str) -> TreeNode:
        """Decodes your encoded data to tree.
        """
        data_queue = collections.deque(data.split(","))
        if data_queue[0] == "":
            return None 
        
        root = self._deserialize(data_queue, -1, 10001)
        return root
    
    def _deserialize(self, data_queue, low, high):
        if len(data_queue) == 0 or int(data_queue[0]) < low or int(data_queue[0]) > high:
            return None 
        
        root_val = int(data_queue.popleft())
        root = TreeNode(root_val)
        root.left = self._deserialize(data_queue, low, root_val)
        root.right = self._deserialize(data_queue, root_val, high)
        return root

        