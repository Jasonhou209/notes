"""
46.全排列
给定一个 没有重复 数字的序列，返回其所有可能的全排列。

示例:
输入: [1,2,3]
输出:
[
  [1,2,3],
  [1,3,2],
  [2,1,3],
  [2,3,1],
  [3,1,2],
  [3,2,1]
]
"""
class Solution:
    def permute(self, nums: list) -> list:
        result = []
        def __backtrace(nums: list, p_list: list):
            if len(nums) <= 0:
                result.append(p_list)
            else:
                for i in nums:
                    c_list = p_list.copy()
                    c_list.append(i)
                    c_nums = nums.copy()
                    c_nums.remove(i)
                    __backtrace(c_nums, c_list)
        __backtrace(nums, [])
        return result

def main():
    s = Solution()
    print(s.permute([1,2,3]))

if __name__ == "__main__":
    main()