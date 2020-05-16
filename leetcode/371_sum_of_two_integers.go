/*
371.两整数之和
不使用运算符 + 和 - ​​​​​​​，计算两整数 ​​​​​​​a 、b ​​​​​​​之和。

示例 1:
输入: a = 1, b = 2
输出: 3
示例 2:
输入: a = -2, b = 3
输出: 1
*/
package main

import "fmt"

func getSum(a int, b int) int {
    if a == 0 {
        return b
    }
    if b == 0 {
        return a
    }
    return getSum(a^b, (a&b)<<1)
}

func main() {
    a, b := -2, 3
    fmt.Println(getSum(a,b))
    a, b = 1, 2
    fmt.Println(getSum(a,b))
}