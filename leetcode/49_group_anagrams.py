"""
49.字母异位词分组
给定一个字符串数组，将字母异位词组合在一起。字母异位词指字母相同，但排列不同的字符串。

示例:
输入: ["eat", "tea", "tan", "ate", "nat", "bat"]
输出:
[
  ["ate","eat","tea"],
  ["nat","tan"],
  ["bat"]
]
"""
class Solution:
    def groupAnagrams(self, strs: list) -> list:
        result_map = {}
        for s in strs:
            tmp = 0
            for n in s:
                tmp = tmp + ord(n)
            else:
                if tmp not in result_map:
                    result_map[tmp] = []
                result_map.get(tmp).append(s)
        else:
            return list(result_map.values())

def main():
    strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
    s = Solution()
    print(s.groupAnagrams(strs))

if __name__ == "__main__":
    main()
