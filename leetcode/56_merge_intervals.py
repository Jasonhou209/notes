"""
56.合并区间
给出一个区间的集合，请合并所有重叠的区间。

示例 1:
输入: [[1,3],[2,6],[8,10],[15,18]]
输出: [[1,6],[8,10],[15,18]]
解释: 区间 [1,3] 和 [2,6] 重叠, 将它们合并为 [1,6].
示例 2:
输入: [[1,4],[4,5]]
输出: [[1,5]]
解释: 区间 [1,4] 和 [4,5] 可被视为重叠区间。
"""
class Solution:
    def merge(self, intervals: list) -> list:
        intervals.sort(key=lambda interval: interval[0])
        result = [intervals[0]]
        for i in range(1, len(intervals)):
            if intervals[i][0] <= result[-1][1]:
                result[-1] = [result[-1][0], max(result[-1][1], intervals[i][1])]
            else:
                result.append(intervals[i])
        return result

def main():
    s = Solution()
    print(s.merge([[8,10],[1,3],[2,6],[15,18]]))
    print(s.merge([[1,4],[4,5]]))

if __name__ == "__main__":
    main()