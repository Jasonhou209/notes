"""
22.括号生成
数字 n 代表生成括号的对数，请你设计一个函数，用于能够生成所有可能的并且有效的括号组合。

示例：
输入：n = 3
输出：[
       "((()))",
       "(()())",
       "(())()",
       "()(())",
       "()()()"
     ]
"""
class Solution:
    def __init__(self):
        self.result = []

    def generateParenthesis(self, n: int) -> list:
        self.__back_track("", 0, 0, n)
        return self.result

    def __back_track(self, s: str, left: int, right: int, m: int) -> None:
        if len(s) == m * 2:
            self.result.append(s)
            return
        if left < m:
            self.__back_track(s+"(", left+1, right, m)
        if right < left:
            self.__back_track(s+")", left, right+1, m)

def main():
    s = Solution()
    print(s.generateParenthesis(3))

if __name__ == "__main__":
    main()