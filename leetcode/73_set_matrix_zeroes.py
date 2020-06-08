"""
73.矩阵置零
给定一个 m x n 的矩阵，如果一个元素为 0，则将其所在行和列的所有元素都设为 0。
请使用原地算法。

示例 1:
输入: 
[
  [1,1,1],
  [1,0,1],
  [1,1,1]
]
输出: 
[
  [1,0,1],
  [0,0,0],
  [1,0,1]
]
示例 2:
输入: 
[
  [0,1,2,0],
  [3,4,5,2],
  [1,3,1,5]
]
输出: 
[
  [0,0,0,0],
  [0,4,5,0],
  [0,3,1,0]
]
"""
class Solution:
    def setZeroes(self, matrix: list) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        for row in matrix:
            for col in range(len(row)):
                if row[col] == 0:
                    for i in range(len(row)):
                        row[i] *= 10
                    for j in range(len(matrix)):
                        matrix[j][col] *= 10

        for row in matrix:
            for col in range(len(row)):
                if row[col] // 10 != 0:
                    row[col] = 0 

def main():
    s = Solution()
    matrix1 = [[1,1,1],[1,0,1],[1,1,1]]
    s.setZeroes(matrix1)
    print(matrix1)
    matrix2 = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
    s.setZeroes(matrix2)
    print(matrix2)

if __name__ == "__main__":
    main()

