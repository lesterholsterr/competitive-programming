# https://leetcode.com/problems/gas-station/

# Knowing this is a greedy problem in advance helped with finding the algorithm
# Intuition: Kind of reminded me of asset prices... buy low sell high lol
class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        # Let net = [] where net[i] = net change in gas going from station i to i+1
        # and net[-1] = net change going from last to 0th station
        # if net < 0, return -1

        # brute force: try summing net starting from every index
        # only 1 solution should never go negative

        # greedy: start from the index of max(net)?
        # -> no doesn't always work [5, -4, -4, 2, 2]

        # greedy #2: cumulative sum from index 0
        # * Try the index AFTER the most negative
        # It can only go up and will never go lower than the most negative, so you will always be net positive!
        n = len(gas)
        net = [gas[i] - cost[i] for i in range(n)]

        if sum(net) < 0:
            return -1
        
        cur = 0
        min_so_far = float('inf')
        min_idx = -1
        for i in range(n):
            cur += net[i]
            if cur < min_so_far:
                min_so_far = cur
                min_idx = i
        return min_idx+1 if min_idx != n-1 else 0

# O(1) memory solution
# Intuition: There is either 0 or 1 solution
# 0 solutions if and only if net < 0 -> easy
# Otherwise 1 solution. ***THEN THE LAST PLACE WE "FAIL" MUST BE THE STARTING POINT***
class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        ans, net, cur = 0, 0, 0
        for i in range(len(gas)):
            net += gas[i] - cost[i]
            cur += gas[i] - cost[i]
            if cur < 0:
                cur = 0
                ans = i+1
        return ans if net >= 0 else -1