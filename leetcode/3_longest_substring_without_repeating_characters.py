"""
3.无重复字符的最长字串
给定一个字符串，请你找出其中不含有重复字符的最长子串的长度。

示例 1:
输入: "abcabcbb"
输出: 3 
解释: 因为无重复字符的最长子串是 "abc"，所以其长度为 3。
示例 2:
输入: "bbbbb"
输出: 1
解释: 因为无重复字符的最长子串是 "b"，所以其长度为 1。
示例 3:
输入: "pwwkew"
输出: 3
解释: 因为无重复字符的最长子串是 "wke"，所以其长度为 3。
     请注意，你的答案必须是 子串 的长度，"pwke" 是一个子序列，不是子串。
"""
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        i, count, res = 0, 0, 0
        for j in range(len(s)):
            if s[i:j+1].count(s[j]) == 1:
                count += 1
            else:
                i = j
                res = max(res, count)
                count = 1
        return res

def main():
    s1 = "abcabcbb"
    s2 = "bbbbb"
    s3 = "pwwkew"

    s = Solution()
    print(s.lengthOfLongestSubstring(s1) == 3)
    print(s.lengthOfLongestSubstring(s2) == 1)
    print(s.lengthOfLongestSubstring(s3) == 3)

if __name__ == "__main__":
    main()