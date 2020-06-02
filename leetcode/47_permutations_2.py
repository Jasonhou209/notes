"""
47.全排列2
给定一个可包含重复数字的序列，返回所有不重复的全排列。

示例:

输入: [1,1,2]
输出:
[
  [1,1,2],
  [1,2,1],
  [2,1,1]
]
"""
class Solution:
    def permuteUnique(self, nums: list) -> list:
        nums.sort()
        result = []
        def __backtrace(nums: list, p_list: list):
            if len(nums) <= 0:
                result.append(p_list)
            else:
                for i in range(len(nums)):
                    if i > 0 and nums[i] == nums[i-1]:
                        continue
                    c_list = p_list.copy()
                    c_list.append(nums[i])
                    c_nums = nums.copy()
                    c_nums.pop(i)
                    __backtrace(c_nums, c_list)
        __backtrace(nums, [])
        return result

def main():
    s = Solution()
    print(s.permuteUnique([1,1,2]))

if __name__ == "__main__":
    main()