"""
232.用栈实现队列
使用栈实现队列的下列操作：

push(x) -- 将一个元素放入队列的尾部。
pop() -- 从队列首部移除元素。
peek() -- 返回队列首部的元素。
empty() -- 返回队列是否为空。
示例:

MyQueue queue = new MyQueue();

queue.push(1);
queue.push(2);  
queue.peek();  // 返回 1
queue.pop();   // 返回 1
queue.empty(); // 返回 false
"""
class MyQueue:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.stack = []
        self.work_stack = []


    def push(self, x: int) -> None:
        """
        Push element x to the back of queue.
        """
        self.stack.append(x)


    def pop(self) -> int:
        """
        Removes the element from in front of queue and returns that element.
        """
        while len(self.stack) != 0:
            self.work_stack.append(self.stack.pop())
        tmp = self.work_stack.pop()
        while len(self.work_stack) != 0:
            self.stack.append(self.work_stack.pop())
        return tmp


    def peek(self) -> int:
        """
        Get the front element.
        """
        while len(self.stack) != 0:
            self.work_stack.append(self.stack.pop())
        tmp = self.work_stack.pop()
        self.work_stack.append(tmp)
        while len(self.work_stack) != 0:
            self.stack.append(self.work_stack.pop())
        return tmp


    def empty(self) -> bool:
        """
        Returns whether the queue is empty.
        """
        return len(self.stack) == 0

def main():
    obj = MyQueue()
    obj.push(1)
    obj.push(2)
    param_2 = obj.pop()
    param_3 = obj.peek()
    param_4 = obj.empty()
    print(param_2)
    print(param_3)
    print(param_4)

if __name__ == "__main__":
    main()