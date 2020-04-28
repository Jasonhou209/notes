"""
125.验证回文串
给定一个字符串，验证它是否是回文串，只考虑字母和数字字符，可以忽略字母的大小写。
说明：本题中，我们将空字符串定义为有效的回文串。

示例 1:

输入: "A man, a plan, a canal: Panama"
输出: true
示例 2:

输入: "race a car"
输出: false
"""
class Solution:

    def isPalindrome(self, s: str) -> bool:
        left, right = 0, len(s) - 1
        while left <= right:
            if not s[left].isalpha():
                left = left + 1
                continue
            elif not s[right].isalpha():
                right = right - 1
                continue
            elif s[left].upper() == s[right].upper():
                left = left + 1
                right = right - 1
                continue
            else:
                return False
        else:
            return True

def main():
    s1 = "A man, a plan, a canal: Panama"
    s2 = "race a car"
    s = Solution()
    print(s.isPalindrome(s1))
    print(s.isPalindrome(s2))

if __name__ == "__main__":
    main()