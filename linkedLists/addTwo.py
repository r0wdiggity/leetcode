class Solution:
    def addTwoNumbers(self, l1, l2):
        one = []
        two = []
        while True:
            one.insert(0, str(l1.val))
            if l1.next == None:
                break
            l1 = l1.next
        while True:
            two.insert(0, str(l2.val))
            if l2.next == None:
                break
            l2 = l2.next
        one = int(''.join(one))
        two = int(''.join(two))
        num = one + two
        ans = ((list(str(num)))[::-1])

        listnode = tmp = ListNode(0)

        for num in ans:
            new = ListNode(int(num))
            tmp.next = new
            tmp = tmp.next

        return listnode.next