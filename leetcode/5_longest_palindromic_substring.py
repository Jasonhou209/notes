"""
5.最长回文子串
给定一个字符串 s，找到 s 中最长的回文子串。你可以假设 s 的最大长度为 1000。

示例 1：
输入: "babad"
输出: "bab"
注意: "aba" 也是一个有效答案。
示例 2：
输入: "cbbd"
输出: "bb"
"""
class Solution:
    def __init__(self):
        self.palindrome = []

    def longestPalindrome(self, s: str) -> str:
        for i in range(len(s)):
            for j in range(i+1,len(s)):
                if s[i:j] == s[i:j][::-1]:
                    if len(self.palindrome) == 0:
                        self.palindrome.append(s[i:j])
                    elif len(s[i:j]) > len(self.palindrome[0]):
                        self.palindrome[0] = s[i:j]
        if len(self.palindrome) == 0:
            return ""
        else:
            return self.palindrome.pop()

def main():
    s = Solution()
    n1, n2 = "babad", "cbbd"
    print(s.longestPalindrome(n1))
    print(s.longestPalindrome(n2))

if __name__ == "__main__":
    main()