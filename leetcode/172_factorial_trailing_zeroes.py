"""
172.阶乘后的零
给定一个整数 n，返回 n! 结果尾数中零的数量。

示例 1:
输入: 3
输出: 0
解释: 3! = 6, 尾数中没有零。

示例 2:
输入: 5
输出: 1
解释: 5! = 120, 尾数中有 1 个零.
说明: 你算法的时间复杂度应为 O(log n) 。
"""
class Solution:
    def trailingZeroes(self, n: int) -> int:
        count, tmp = 0, 0
        while n // 5 > 0:
            tmp = n // 5
            count += tmp
            n = tmp
        return count

def main():
    n1 = 3
    n2 = 5
    s = Solution()
    print(s.trailingZeroes(n1))
    print(s.trailingZeroes(n2))

if __name__ == "__main__":
    main()