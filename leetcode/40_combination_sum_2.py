"""
40.组合总和2
给定一个数组 candidates 和一个目标数 target ，
找出 candidates 中所有可以使数字和为 target 的组合。
candidates 中的每个数字在每个组合中只能使用一次。

说明：
所有数字（包括目标数）都是正整数。
解集不能包含重复的组合。 

示例 1:
输入: candidates = [10,1,2,7,6,1,5], target = 8,
所求解集为:
[
  [1, 7],
  [1, 2, 5],
  [2, 6],
  [1, 1, 6]
]
示例 2:
输入: candidates = [2,5,2,1,2], target = 5,
所求解集为:
[
  [1,2,2],
  [5]
]
"""
class Solution:
    def combinationSum2(self, candidates: list, target: int) -> list:
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
                if i > begin and candidates[i] == candidates[i-1]:
                    continue
                path.append(candidates[i])
                self.helper(left, path, result, candidates, i+1, size)
                path.pop()

def main():
    s = Solution()
    print(s.combinationSum2([10,1,2,7,6,1,5], 8))
    print(s.combinationSum2([2,5,2,1,2], 5))

if __name__ == "__main__":
    main()