class Solution:
    def addTwoNumbers(self, l1, l2):
        dummy = ListNode(0)
        tail = dummy
        carry = 0

        while l1 is not None or l2 is not None:
            if l1 is not None:
                carry += l1.val
                l1 = l1.next

            if l2 is not None:
                carry += l2.val
                l2 = l2.next

            tail.next = ListNode(carry % 10)
            tail = tail.next
            carry //= 10

        if carry:
            tail.next = ListNode(carry)

        return dummy.next