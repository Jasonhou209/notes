"""
24.两两交换链表中的节点
给定一个链表，两两交换其中相邻的节点，并返回交换后的链表。
你不能只是单纯的改变节点内部的值，而是需要实际的进行节点交换。

示例:
给定 1->2->3->4, 你应该返回 2->1->4->3.
"""
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def __init__(self):
        self.root = None
        self.parent = None

    def swapPairs(self, head: ListNode) -> ListNode:
        if self.root is None:
            self.root = head.next
        first_swap = head
        if first_swap is not None:
            second_swap = first_swap.next
            first_swap.next = second_swap.next
            second_swap.next = first_swap
            if self.parent is not None:
                self.parent.next = second_swap
            self.parent = first_swap
            return self.swapPairs(first_swap.next)

    def display(self) -> None:
        work = self.root
        while work is not None:
            print(work.val, end = " ")
            work = work.next

def main():
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(3)
    head.next.next.next = ListNode(4)

    s = Solution()
    s.swapPairs(head)
    s.display()

if __name__ == "__main__":
    main()