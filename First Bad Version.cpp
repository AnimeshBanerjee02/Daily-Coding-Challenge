class Solution {
public:
    int firstBadVersion(int n)
    {
        size_t start = 1;
        size_t end = (size_t) n+1;

        size_t lastBad = 1;
        size_t pivot = 0;

        while (start < end)
        {
            pivot = start + (end - start) / 2;

            if (isBadVersion(pivot))
            {
                lastBad = pivot;
                end = pivot;
            }
            else
            {
                start = pivot+1;
            }
        }
        return (int) lastBad;
    }
};