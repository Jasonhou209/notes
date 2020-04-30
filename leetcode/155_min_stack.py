"""
155.最小栈
设计一个支持 push ，pop ，top 操作，并能在常数时间内检索到最小元素的栈。

push(x) —— 将元素 x 推入栈中。
pop() —— 删除栈顶的元素。
top() —— 获取栈顶元素。
getMin() —— 检索栈中的最小元素。
"""
class MinStack:

    def __init__(self):
        self.stack = []
        self.min_val = []

    def push(self, x: int) -> None:
        self.stack.append(x)
        if len(self.min_val) == 0:
            self.min_val.append(x)
        elif self.min_val[-1] > x:
            self.min_val.append(x)
        else:
            self.min_val.append(self.min_val[-1])

    def pop(self) -> None:
        self.stack.pop()
        self.min_val.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min_val[-1]

def main():
    minStack = MinStack()
    minStack.push(-2)
    minStack.push(0)
    minStack.push(-3)
    print(minStack.getMin()) # -3
    minStack.pop()
    print(minStack.top()) # 0
    print(minStack.getMin()) # -2

if __name__ == "__main__":
    main()