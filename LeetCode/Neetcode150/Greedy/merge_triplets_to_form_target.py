# https://leetcode.com/problems/merge-triplets-to-form-target-triplet/

# Easy peasy lemon squeezy
class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        """
        [[2,5,3],[2,3,4],[1,2,5],[5,6,0]]
        
        target = [5,5,5]

        find triplets where triplet[0] = target[0]
        make sure triplet[1] <= target[1], triplet[2] <= target[2]
        repeat for triplet[1] and triplet[2]
        """
        found = [False, False, False]
        for triplet in triplets:
            if triplet[0] == target[0] and triplet[1] <= target[1] and triplet[2] <= target[2]:
                found[0] = True
            if triplet[0] <= target[0] and triplet[1] == target[1] and triplet[2] <= target[2]:
                found[1] = True
            if triplet[0] <= target[0] and triplet[1] <= target[1] and triplet[2] == target[2]:
                found[2] = True
        return found[0] and found[1] and found[2]
        