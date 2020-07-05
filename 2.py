# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def addTwoNumbers(self, l1, l2):
        l1 = List2ListNode(l1)
        l2 = List2ListNode(l2)
        out = ListNode(0)
        add = 0
        result = []
        while l1 or l2:
            a = l1.val if l1 else 0
            b = l2.val if l2 else 0
            s = a + b + add
            add = s//10
            out.next = ListNode(s % 10)
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
            out = out.next
            result.append(out.val)
        if add > 0:
            out.next = ListNode(add)
            result.append(out.next.val)
        return result


def List2ListNode(list: list):
    listnode = ListNode(list[0])
    listnode.next = ListNode(list[1])
    listnode.next.next = ListNode(list[2])
    return listnode


if __name__ == '__main__':
    solution = Solution()
    print(solution.addTwoNumbers([2, 4, 3], [5, 6, 4]))


# class Solution:
#     def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
#         dummy = p = ListNode(None)
#         s = 0
#         while l1 or l2 or s:
#             s += (l1.val if l1 else 0) + (l2.val if l2 else 0)
#             p.next = ListNode(s % 10)
#             p = p.next
#             s //= 10
#             l1 = l1.next if l1 else None
#             l2 = l2.next if l2 else None
#         return dummy.next
