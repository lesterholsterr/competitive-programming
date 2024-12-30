# https://leetcode.com/problems/partition-labels/description/

# Pretty straightforward
class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        # include a in first partition -> i must go until the last a
        # for each of the letters between those as, must go until the last of those letters
        last = {}
        for i in range(len(s)):
            last[s[i]] = i
        
        prev = 0
        i = 0
        partitions = []
        while i < len(s):
            end = last[s[i]]
            while i <= end:
                end = max(end, last[s[i]])
                i += 1
            partitions.append(i-prev)
            prev = i
        return partitions
