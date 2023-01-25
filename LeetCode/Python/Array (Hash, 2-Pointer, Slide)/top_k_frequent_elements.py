class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        # Solution 1: O(k*n)
        freq = {}
        for num in nums:
            if num in freq:
                freq[num] += 1
            else:
                freq[num] = 1
        
        res = []
        max_key = 0
        max_val = 0
        while len(res) < k:
            for key, val in freq.items():
                if val > max_val:
                    max_val = val
                    max_key = key
            res.append(max_key)
            freq[max_key] = 0
            max_val = 0

        return res

        # Solution 2: O(n)
        # Solution from https://www.youtube.com/watch?v=YPTqKIgVk-k&t=513s
        class Solution(object):
            count = {}
            freq = [[] for i in range(len(nums)+1)]

            for n in nums:
                if n in count:
                    count[n] += 1
                else:
                    count[n] = 1
            
            # In the list of lists, add n to the cth list, where c is the number of times n appears in nums!
            for n, c in count.items():
                freq[c].append(n)
            
            res = []
            for i in range(len(freq)-1, 0, -1):
                for n in freq[i]:
                    res.append(n)
                    if len(res) == k:
                        return res