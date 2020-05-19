"""
2.两数相加
给出两个非空的链表用来表示两个非负的整数。其中，它们各自的位数是按照逆序的方式存储的，并且它们的每个节点只能存储一位数字。
如果，我们将这两个数相加起来，则会返回一个新的链表来表示它们的和。
您可以假设除了数字0之外，这两个数都不会以0开头。

示例：
输入：(2 -> 4 -> 3) + (5 -> 6 -> 4)
输出：7 -> 0 -> 8
原因：342 + 465 = 807
"""
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def __init__(self):
        self.head = ListNode(0)

    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        result = str(int(self._helper(l1)) + int(self._helper(l2)))
        self.insert(result)

    def _helper(self, l: ListNode) -> str:
        if l is not None:
            return self._helper(l.next) + str(l.val)
        return ""
    
    def insert(self, s: str) -> None:
        temp = self.head
        for i in range(len(s)):
            temp.next = ListNode(s[-1-i])
            temp = temp.next

    def display(self) -> None:
        self.head = self.head.next
        while self.head is not None:
            print(self.head.val, end=" ")
            self.head = self.head.next

def main():
    l1 = ListNode(2)
    l1.next = ListNode(4)
    l1.next.next = ListNode(3)

    l2 = ListNode(5)
    l2.next = ListNode(6)
    l2.next.next = ListNode(4)

    s = Solution()
    s.addTwoNumbers(l1, l2)
    s.display()

if __name__ == "__main__":
    main()