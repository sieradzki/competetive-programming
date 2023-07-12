class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        l1_list = [l1.val]
        l2_list = [l2.val]
        next_list1 = l1.next
        next_list2 = l2.next

        while next_list1 is not None:
            l1_list.append(next_list1.val)
            next_list1 = next_list1.next

        while next_list2 is not None:
            l2_list.append(next_list2.val)
            next_list2 = next_list2.next

        l1_list.reverse()
        l2_list.reverse()

        l1_num = int(''.join(map(str, l1_list)))
        l2_num = int(''.join(map(str, l2_list)))
        sum = str(l1_num + l2_num)[::-1]

        output = tmp = ListNode()
        for i, chr in enumerate(sum):
            tmp.val = chr
            if i == len(sum)-1:
                break
            tmp.next = ListNode()
            tmp = tmp.next

        return output