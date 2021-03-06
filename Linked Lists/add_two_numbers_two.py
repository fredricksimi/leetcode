"""
Add Two Numbers II: Leetcode 445

You are given two non-empty linked lists representing two non-negative integers. 
The most significant digit comes first and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.
You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Follow up:
What if you cannot modify the input lists? In other words, reversing the lists is not allowed.
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# 0(max(n+m)) time | 0(n+m) space
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:

        result = ListNode(-1)

        stack_one = []
        stack_two = []

        # fill up the stacks
        item_one = l1
        while item_one:
            stack_one.append(item_one.val)
            item_one = item_one.next
        item_two = l2
        while item_two:
            stack_two.append(item_two.val)
            item_two = item_two.next

        len_one = len(stack_one)
        len_two = len(stack_two)
        max_len = max(len_one, len_two)

        # addition
        i = 0
        carry = 0
        node_after_head = None
        while i <= max_len:  # iterate till max_len in order to handle carries

            # get values
            val_one = 0
            if i < len_one:
                val_one = stack_one.pop()
            val_two = 0
            if i < len_two:
                val_two = stack_two.pop()

            # arithmetic
            total = val_one + val_two + carry
            carry = 0
            if total > 9:
                total -= 10  # eg: when total = 19 : add (19-10) and carry 1
                carry = 1

            # add nodes to the result
            # if we are still adding or we have one left carry(eg: 99 + 99)
            if i < max_len or total > 0:
                node = ListNode(total)
                if node_after_head:
                    node.next = node_after_head
                    result.next = node
                    node_after_head = node
                else:
                    result.next = node
                    node_after_head = node
            i += 1

        # skip the first node (start at node_after_head)
        return result.next


"""
Example:

Input: (7 -> 2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 8 -> 0 -> 7

input:
    [7,2,4,3]
    [5,6,4]
    [9,8,7,6,6,7,8,9]
    [9,8,7,6,6,7,8,9]
    [1,2,3,4,5,5,6,9]
    [1,2,3,4,5,5,6,9]
output:
    [7,8,0,7]
    [7,8,0,7]
    [1,9,7,5,3,3,5,7,8]
    [2,4,6,9,1,1,3,8]
    [1,5]
"""
