# Hint: use BST properties
# Didn't use BST properties, left artifacts of a solution for traversing a 
# tree normally (queue), can also simplify conditions

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        curr = root
        
        if p.val < q.val:
            p, q = q, p
        # q is smallest, p is largest

        while curr:
            # if curr.val > q.val and curr.val < p.val:
            #     return curr
            # elif curr.val == p.val or curr.val == q.val:
            #     return curr
                
            if curr.val < q.val:
                curr = curr.right
            elif curr.val > p.val:
                curr = curr.left
            else:
                return curr

