"""

    1.给定一个整数数组nums和一个目标值target,请你在该数组中找出和为目标值的那两个整数,并返回他们的数组下标。
      你可以假设每种输入只会对应一个答案。但是,你不能重复利用这个数组中同样的元素。

    示例:
        给定 nums =[2, 7, 11, 15], target =9
        因为 nums[0] +nums[1] =2 +7 =9
        所以返回 [0, 1]

"""

class Solution:

    def __init__(self):
        self.result = []
    
    def twoSum(self, nums: list, target: int) -> list:
        for i in range(len(nums) - 1):
            for j in range(i+1, len(nums)):
                if nums[i] + nums[j] == target:
                    self.result.append(i)
                    self.result.append(j)
        return self.result

if __name__ == "__main__":

    nums = [2, 7, 11, 15]
    target = 9

    s = Solution()
    r = s.twoSum(nums, target)
    print(r)