"""
86.分隔链表
给定一个链表和一个特定值 x，对链表进行分隔，
使得所有小于 x 的节点都在大于或等于 x 的节点之前。
你应当保留两个分区中每个节点的初始相对位置。

示例:
输入: head = 1->4->3->2->5->2, x = 3
输出: 1->2->2->4->3->5
"""
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def partition(self, head: ListNode, x: int) -> ListNode:
        first_node = ListNode(0)
        first_node.next = head

        less_node = first_node
        prev_node = first_node
        curr_node = head

        while curr_node is not None:
            if curr_node.val < x:
                if prev_node is less_node:
                    prev_node = curr_node
                    less_node = curr_node
                    curr_node = curr_node.next
                else:
                    prev_node.next = curr_node.next
                    curr_node.next = less_node.next
                    less_node.next = curr_node
                    less_node = curr_node
                    curr_node = prev_node.next
            else:
                prev_node = curr_node
                curr_node = prev_node.next
        return first_node.next

def main():
    head = ListNode(1)
    head.next = ListNode(4)
    head.next.next = ListNode(3)
    head.next.next.next = ListNode(2)
    head.next.next.next.next = ListNode(5)
    head.next.next.next.next.next = ListNode(2)

    s = Solution()
    head = s.partition(head, 3)

    while head is not None:
        print(head.val, end=" ")
        head = head.next

if __name__ == "__main__":
    main()