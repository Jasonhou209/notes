"""
33.搜索旋转排序数组
假设按照升序排序的数组在预先未知的某个点上进行了旋转。
( 例如，数组 [0,1,2,4,5,6,7] 可能变为 [4,5,6,7,0,1,2] )。
搜索一个给定的目标值，如果数组中存在这个目标值，则返回它的索引，否则返回 -1 。
你可以假设数组中不存在重复的元素。
你的算法时间复杂度必须是 O(log n) 级别。

示例 1:
输入: nums = [4,5,6,7,0,1,2], target = 0
输出: 4
示例 2:
输入: nums = [4,5,6,7,0,1,2], target = 3
输出: -1
"""
class Solution:
    def search(self, nums: list, target: int) -> int:
        if len(nums) == 0:
            return -1
        
        left, right = 0, len(nums)-1
        
        while left < right:
            middle = (right - left) // 2 + left
            if nums[middle] == target:
                return middle
            if nums[middle] > nums[left]:
                if nums[left] <= target and target <= nums[right]:
                    right = middle
                else:
                    left = middle + 1
            else:
                if nums[middle+1] <= target and target <= nums[right]:
                    left = middle + 1
                else:
                    right = middle
        else:
            if nums[left] == target:
                return left
            else:
                return -1

def main():
    s = Solution()
    print(s.search([4,5,6,7,0,1,2], 0))
    print(s.search([4,5,6,7,0,1,2], 3))

if __name__ == "__main__":
    main()