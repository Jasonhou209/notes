"""
219.存在重复元素
给定一个整数数组和一个整数 k，判断数组中是否存在两个不同的索引 i 和 j，
使得 nums [i] = nums [j]，并且 i 和 j 的差的 绝对值 至多为 k。

示例 1:
输入: nums = [1,2,3,1], k = 3
输出: true
示例 2:
输入: nums = [1,0,1,1], k = 1
输出: true
示例 3:
输入: nums = [1,2,3,1,2,3], k = 2
输出: false
"""
class Solution:
    def containsNearbyDuplicate(self, nums: list, k: int) -> bool:
        d = {}
        temp = True
        for i, v in enumerate(nums):
            if v not in d:
                d[v] = i
            elif abs(d[v]-i) > k and v not in nums[i+1:]:
                return False
            else:
                d[v] = i
        else:
            if len(d) == 0:
                return False
            else:
                return True

def main():
    nums1 = [1, 2, 3, 1]
    nums2 = [1, 0, 1, 1]
    nums3 = [1, 2, 3, 1, 2, 3]

    s = Solution()
    print("case1: ", s.containsNearbyDuplicate(nums1, 3))
    print("case2: ", s.containsNearbyDuplicate(nums2, 1))
    print("case3: ", s.containsNearbyDuplicate(nums3, 2))

if __name__ == "__main__":
    main()