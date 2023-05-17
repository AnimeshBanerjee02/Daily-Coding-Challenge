class Solution {
public:
    int pairSum(ListNode* head) {
        ListNode* current = head;
        vector<int> values;

        while (current) {
            values.push_back(current->val);
            current = current->next;
        }

        int maximumSum = 0;
        int left = 0;
        int right = values.size() - 1;
        while (left < right) {
            maximumSum = max(maximumSum, values[left] + values[right]);
            left++;
            right--;
        }

        return maximumSum;
    }
};
