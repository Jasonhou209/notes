"""
342.4的幂
给定一个整数 (32 位有符号整数)，请编写一个函数来判断它是否是 4 的幂次方。

示例 1:
输入: 16
输出: true
示例 2:
输入: 5
输出: false
"""
class Solution:
    def isPowerOfFour(self, num: int) -> bool:
        return ((num >> 2) & 1) == 0

def main():
    n1, n2 = 16, 5
    s = Solution()
    print(s.isPowerOfFour(n1))
    print(s.isPowerOfFour(n2))

if __name__ == "__main__":
    main()