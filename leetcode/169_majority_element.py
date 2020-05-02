"""
169.多数元素
给定一个大小为 n 的数组，找到其中的多数元素。多数元素是指在数组中出现次数大于[n/2]的元素。
你可以假设数组是非空的，并且给定的数组总是存在多数元素。

示例 1:
输入: [3,2,3]
输出: 3

示例 2:
输入: [2,2,1,1,1,2,2]
输出: 2
"""
class Solution:
    def majorityElement(self, nums: list) -> int:
        times = len(nums) // 2
        d = {}
        for v in nums:
            if v not in d:
                d[v] = 1
            else:
                d[v] += 1
            if d[v] > times:
                return v

def main():
    n1 = [3, 2, 3]
    n2 = [2, 2, 1, 1, 1, 2, 2]
    s = Solution()
    print(s.majorityElement(n1))
    print(s.majorityElement(n2))

if __name__ == "__main__":
    main()
