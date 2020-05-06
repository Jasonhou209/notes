"""
203.移除链表元素
删除链表中等于给定值 val 的所有节点。

示例:

输入: 1->2->6->3->4->5->6, val = 6
输出: 1->2->3->4->5
"""
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        while head != None and head.val == val:
            head = head.next
        else:
            cur = head
        while cur != None and cur.next != None:
            if cur.next.val == val and cur.next.next != None:
                cur.next = cur.next.next
            elif cur.next.val == val:
                cur.next = None
                break
            cur = cur.next
        return head

def main():
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(6)
    head.next.next.next = ListNode(3)
    head.next.next.next.next = ListNode(4)
    head.next.next.next.next.next = ListNode(5)
    head.next.next.next.next.next.next = ListNode(6)

    resNone = Solution().removeElements(head, 6)

    while resNone != None:
        print(resNone.val, end=" ")
        resNone = resNone.next

if __name__ == "__main__":
    main()