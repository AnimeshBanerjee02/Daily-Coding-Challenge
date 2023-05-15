/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */
class Solution {
public:
    ListNode* swapNodes(ListNode* head, int k) {
        // Step 1: Find the length of the linked list
        int length = 0;
        ListNode* current = head;
        while (current) {
            length++;
            current = current->next;
        }
        
        // Step 2: Find the kth node from the beginning
        ListNode* kthFromBeginning = head;
        for (int i = 1; i < k; i++) {
            kthFromBeginning = kthFromBeginning->next;
        }
        
        // Step 3: Find the kth node from the end
        ListNode* kthFromEnd = head;
        for (int i = 1; i < length - k + 1; i++) {
            kthFromEnd = kthFromEnd->next;
        }
        
        // Step 4: Swap the values of the kth nodes
        int temp = kthFromBeginning->val;
        kthFromBeginning->val = kthFromEnd->val;
        kthFromEnd->val = temp;
        
        return head;
    }
};
