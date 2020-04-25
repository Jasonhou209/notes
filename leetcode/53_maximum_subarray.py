"""
53.给定一个整数数组 nums ，找到一个具有最大和的连续子数组（子数组最少包含一个元素），返回其最大和。

示例:

输入: [-2,1,-3,4,-1,2,1,-5,4],
输出: 6
解释: 连续子数组 [4,-1,2,1] 的和最大，为 6。
"""

class Solution:

    def __init__(self):
        self.sum = 0
        self.max_sum = 0

    def maxSubArray(self, nums: list) -> int:

        for x in range(len(nums)):
            self.sum = nums[x]
            for y in range(x+1, len(nums)):
                self.sum = self.sum + nums[y]
                if self.sum > self.max_sum:
                    self.max_sum = self.sum
        return self.max_sum

def main():
    n = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    s = Solution()
    print(s.maxSubArray(n))

if __name__ == "__main__":
    main()
