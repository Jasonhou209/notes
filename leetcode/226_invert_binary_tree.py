"""
226.翻转二叉树
翻转一棵二叉树。

示例：
输入：

     4
   /   \
  2     7
 / \   / \
1   3 6   9
输出：
     4
   /   \
  7     2
 / \   / \
9   6 3   1
"""
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        cur = root
        cur.left, cur.right = cur.right, cur.left 
        if cur.left is not None:
            self.invertTree(cur.left)
        if cur.right is not None:
            self.invertTree(cur.right)
        return root

    def display(self, root: TreeNode):
        if root.left is not None:
            self.display(root.left)
        print(root.val)
        if root.right is not None:
            self.display(root.right)
        return


def main():
    root = TreeNode(4)
    root.left = TreeNode(2)
    root.right = TreeNode(7)
    root.left.left = TreeNode(1)
    root.left.right = TreeNode(3)
    root.right.left = TreeNode(6)
    root.right.right = TreeNode(9)

    s = Solution()
    resNode = s.invertTree(root)
    s.display(resNode)

if __name__ == "__main__":
    main()