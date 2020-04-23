"""
	给定一个只包括 '('，')'，'{'，'}'，'['，']' 的字符串，判断字符串是否有效。

	有效字符串需满足：

	1. 左括号必须用相同类型的右括号闭合。
	2. 左括号必须以正确的顺序闭合。
	
	注意空字符串可被认为是有效字符串。

	示例 1:

		输入: "()"
		输出: true
	
	示例 2:

		输入: "()[]{}"
		输出: true
	
	示例 3:

		输入: "(]"
		输出: false
	
	示例 4:

		输入: "([)]"
		输出: false
	
	示例 5:

		输入: "{[]}"
		输出: true

"""

class Solution:

    def __init__(self):
        self.d = {'(':')','[':']','{':'}'}
        self.stack = []

    def isValid(self, s: str) -> bool:

    	for v in s:
    		if v in self.d:
    			self.stack.append(v)
    		elif len(self.stack) == 0:
    			return False
    		elif self.d[self.stack.pop()] == v:
    			continue
    		else:
    			return False
    	else:
    		return True


if __name__ == "__main__":

	s = Solution()
	print("()", "=>", s.isValid("()"))
	print("()[]{}", "=>", s.isValid("()[]{}"))
	print("(]", "=>", s.isValid("(]"))
	print("([)]", "=>", s.isValid("([)]"))
	print("{[]}", "=>", s.isValid("{[]}"))
	print("()[{]}", "=>", s.isValid("()[{]}"))
