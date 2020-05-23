"""
19.删除链表的倒数第n个节点，并且返回链表的头节点
示例：

给定一个链表: 1->2->3->4->5, 和 n = 2.
当删除了倒数第二个节点后，链表变为 1->2->3->5.
说明：
给定的 n 保证是有效的。

进阶：
你能尝试使用一趟扫描实现吗？
"""
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        p = head
        q = head
        for _ in range(n):
            p = p.next
                
        while p.next is not None:
            p = p.next
            q = q.next
        else:
            q.next = q.next.next
            return head

    def display(self, head: ListNode) -> None:
        while head.next is not None:
            head = head.next
            print(head.val, end=" ")

def main():
    head = ListNode(0)
    head.next = ListNode(1)
    head.next.next = ListNode(2)
    head.next.next.next = ListNode(3)
    head.next.next.next.next = ListNode(4)
    head.next.next.next.next.next = ListNode(5)

    s = Solution()
    head = s.removeNthFromEnd(head, 2)
    s.display(head)

if __name__ == "__main__":
    main()