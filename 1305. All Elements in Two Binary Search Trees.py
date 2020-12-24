# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def getAllElements(self, root1: TreeNode, root2: TreeNode) -> List[int]:
        ns = []
        
        def getElemets(root):
            ns.append(root.val) #每個值存進去
            if root.left: #若還有繼續找
                getElemets(root.left)
            if root.right:
                getElemets(root.right)
        
        if root1: #拆成roo1跟root2下去找
            getElemets(root1)
        if root2:
            getElemets(root2)
        
        return sorted(ns)
