"""
92.反转链表
反转从位置 m 到 n 的链表。请使用一趟扫描完成反转。

说明:
1 ≤ m ≤ n ≤ 链表长度。
示例:
输入: 1->2->3->4->5->NULL, m = 2, n = 4
输出: 1->4->3->2->5->NULL
"""
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
        first = ListNode(0)
        first.next = head

        before_m = first
        after_n = None

        between_head = None
        between_end = None

        i = 0
        cur = first
        while i < n:
            i += 1
            cur = cur.next
            if i == m - 1:
                before_m = cur
            elif i == m:
                between_end = ListNode(cur.val)
                between_head = between_end
            elif i > m:
                temp = between_head
                between_head = ListNode(cur.val)
                between_head.next = temp
                if i == n:
                    after_n = cur.next

        between_end.next = after_n
        before_m.next = between_head
        return first.next

def main():
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(3)
    head.next.next.next = ListNode(4)
    head.next.next.next.next = ListNode(5)

    s = Solution()
    head = s.reverseBetween(head, 2, 4)

    while head is not None:
        print(head.val, end=" ")
        head = head.next

if __name__ == "__main__":
    main()