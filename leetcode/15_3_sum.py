"""
15.3数之和
给你一个包含 n 个整数的数组 nums，判断 nums 中是否存在三个元素 a，b，c ，
使得 a + b + c = 0 ？请你找出所有满足条件且不重复的三元组。
注意：答案中不可以包含重复的三元组。

示例：
给定数组 nums = [-1, 0, 1, 2, -1, -4]，
满足要求的三元组集合为：
[
  [-1, 0, 1],
  [-1, -1, 2]
]
"""
class Solution:
    def threeSum(self, nums: list) -> list:
        result = []
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                k = 0-(nums[i]+nums[j])
                if k in nums and k != nums[i] and k != nums[j]:
                    ind = nums.index(0-(nums[i]+nums[j]))
                    tmp = [nums[i], nums[j], nums[ind]]
                    tmp.sort()
                    if tmp not in result:
                        result.append(tmp)
        return result

def main():
    nums = [-1, 0, 1, 2, -1, -4]
    s = Solution()
    print(s.threeSum(nums))

if __name__ == "__main__":
    main()