"""
136.只出现一次的数字
给定一个非空整数数组，除了某个元素只出现一次以外，其余每个元素均出现两次。
找出那个只出现了一次的元素。

说明：
你的算法应该具有线性时间复杂度。 你可以不使用额外空间来实现吗？
"""
class Solution:
    def singleNumber(self, nums: list) -> int:
        single_num = 0
        for i in nums:
            single_num = single_num ^ i
        return single_num

def main():
    l1 = [2, 2, 1]
    l2 = [4, 1, 2, 1, 2]
    s = Solution()
    print(s.singleNumber(l1))
    print(s.singleNumber(l2))

if __name__ == "__main__":
    main()
