# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        # check if either list is empty, if so return the other list
        if not list1:
            return list2
        if not list2:
            return list1

        # set up a new linked list to hold the merged values
        merged = ListNode()
        # set the current node to the head of the new list
        current = merged

        # loop while there are still nodes in both lists
        while list1 and list2:
            # compare the values of the current nodes of both lists
            if list1.val < list2.val:
                # add the current node of list1 to the new list
                current.next = list1
                # move to the next node in list1
                list1 = list1.next
            else:
                # add the current node of list2 to the new list
                current.next = list2
                # move to the next node in list2
                list2 = list2.next

            # move to the next node in the new list
            current = current.next

        # add any remaining nodes from list1 or list2 to the new list
        if list1:
            current.next = list1
        if list2:
            current.next = list2

        # return the head of the new list
        return merged.next
