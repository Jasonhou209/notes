"""
349.两个数组的交集
给定两个数组，编写一个函数来计算它们的交集。

示例 1:
输入: nums1 = [1,2,2,1], nums2 = [2,2]
输出: [2]
示例 2:
输入: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
输出: [9,4]
说明:

输出结果中的每个元素一定是唯一的。
我们可以不考虑输出结果的顺序。
"""
class Solution:
    def intersection(self, nums1: list, nums2: list) -> list:
        d, res = {}, []
        for i in nums1:
            if i not in d:
                d[i] = i
        for j in nums2:
            if j in d:
                del d[j]
                res.append(j)
        return res

def main():
    nums1, nums2 = [4, 9, 5], [9, 4, 9, 8, 4]
    s = Solution()
    print(s.intersection(nums1, nums2))

    nums1[:], nums2[:] = [], []
    nums1, nums2 = [1, 2, 2, 1], [2, 2]
    print(s.intersection(nums1, nums2))

if __name__ =="__main__":
    main()