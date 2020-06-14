"""
96.不同的二叉搜索树
给定一个整数 n，求以 1 ... n 为节点组成的二叉搜索树有多少种？
示例:

输入: 3
输出: 5
解释:
给定 n = 3, 一共有 5 种不同结构的二叉搜索树:

   1         3     3      2      1
    \       /     /      / \      \
     3     2     1      1   3      2
    /     /       \                 \
   2     1         2                 3
"""
class Solution:
    def __init__(self):
        self.visited = dict()

    def numTrees(self, n: int) -> int:
        if n in self.visited:
            return self.visited.get(n)
        if n <= 1:
            return 1
        result = 0
        for i in range(1, n+1):
            result += self.numTrees(i-1) * self.numTrees(n-i)
        self.visited[n] = result
        return result

def main():
    s = Solution()
    print(s.numTrees(3))

if __name__ == "__main__":
    main()