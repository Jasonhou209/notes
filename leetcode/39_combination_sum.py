"""
39.组合之和
给定一个无重复元素的数组 candidates 和一个目标数 target ，
找出 candidates 中所有可以使数字和为 target 的组合。
candidates 中的数字可以无限制重复被选取。

说明：
所有数字（包括 target）都是正整数。
解集不能包含重复的组合。 

示例 1:
输入: candidates = [2,3,6,7], target = 7,
所求解集为:
[
  [7],
  [2,2,3]
]
示例 2:
输入: candidates = [2,3,5], target = 8,
所求解集为:
[
  [2,2,2,2],
  [2,3,3],
  [3,5]
]
"""
class Solution:
    def combinationSum(self, candidates: list, target: int) -> list:
        candidates.sort()
        path, result, size = [], [], len(candidates)
        self.helper(target, path, result, candidates, 0, size)
        return result

    def helper(self, target: int, path: list, result: list, candidates: list, begin: int, size: int) -> None:
        if target == 0:
            result.append(path.copy())
        else:
            for i in range(begin, size):
                left = target - candidates[i]
                if left < 0:
                    break
                path.append(candidates[i])
                self.helper(left, path, result, candidates, i, size)
                path.pop()

def main():
    s = Solution()
    print(s.combinationSum([2, 3, 6, 7], 7))
    print(s.combinationSum([2, 3, 5], 8))

if __name__ == "__main__":
    main()