/**
104.给定一个二叉树，找出其最大深度。
二叉树的深度为根节点到最远叶子节点的最长路径上的节点数。
说明: 叶子节点是指没有子节点的节点。

示例：
给定二叉树 [3,9,20,null,null,15,7]，

    3
   / \
  9  20
    /  \
   15   7
返回它的最大深度 3
*/
package main

import "fmt"

type TreeNode struct {
    Val int
    Left *TreeNode
    Right *TreeNode
}

func main() {
	tree := new(TreeNode)
	tree.Val = 3
	tree.Left = new(TreeNode)
	tree.Left.Val = 9
	tree.Right = new(TreeNode)
	tree.Right.Val = 20
	tree.Right.Left = new(TreeNode)
	tree.Right.Left.Val = 15
	tree.Right.Right = new(TreeNode)
	tree.Right.Right.Val = 7

	fmt.Print("depth: ", maxDepth(tree))
}

func maxDepth(root *TreeNode) int {

	if root == nil {
		return 0
	} else {
		leftTree := maxDepth(root.Left)
		rightTree := maxDepth(root.Right)
		if leftTree > rightTree {
			return 1 + leftTree
		} else {
			return 1 + rightTree
		}
	}
}