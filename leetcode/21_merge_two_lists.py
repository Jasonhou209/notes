"""
21. 将两个升序链表合并为一个新的升序链表并返回。新链表是通过拼接给定的两个链表的所有节点组成的。 

示例：

输入：1->2->4, 1->3->4
输出：1->1->2->3->4->4

"""
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:

    def __init__(self):
        self.head_node = ListNode(None)
        self.current_node = ListNode(None)
    
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:

        if l1 is None:
            return l2

        if l2 is None:
            return l1

        if l1.val <= l2.val:
            self.head_node.next = l1
        else:
            self.head_node.next = l2

        while (l1 is not None) and (l2 is not None):
            if l1.val <= l2.val:
                self.current_node.next = l1
                l1 = l1.next
            else:
                self.current_node.next = l2
                l2 = l2.next
            self.current_node = self.current_node.next
        else:
            if l1 is not None:
                self.current_node.next = l1
            if l2 is not None:
                self.current_node.next = l2

        return self.head_node.next

def main():
    l1 = ListNode(1)
    l1.next = ListNode(2)
    l1.next.next = ListNode(4)

    l2 = ListNode(1)
    l2.next = ListNode(3)
    l2.next.next = ListNode(4)

    s = Solution()
    l = s.mergeTwoLists(l1, l2)

    while l is not None:
        if l.next is not None:
            print(l.val, end="->")
        else:
            print(l.val)
        l = l.next

if __name__ == "__main__":
    main()