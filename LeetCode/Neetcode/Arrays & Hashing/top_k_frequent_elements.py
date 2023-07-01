class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """

        # Overall: Multiple ways to brute force. Linear time solution is similar to something I've done already, but still failed to produce it.
        # Leaps
        # - How can we map numbers to their frequencies such that the frequencies are sorted?
        # - Realize we can use an array where the index represents frequency, like we did in Group Anagrams

        # Initial Solution (30 minutes)
        # I know right? yikes...
        # Time: O(n^2), Memory: O(n)
        nums.sort()
        num, numfreq, res, freq = nums[0], 0, [], []
        for n in nums:
            if n == num:
                numfreq += 1
            else:
                if len(freq) == 0:
                    freq.append(numfreq)
                    res.append(num)
                else:
                    for i in range(len(freq) + 1):
                        if i == len(freq):
                            freq.append(numfreq)
                            res.append(num)
                            break
                        elif numfreq >= freq[i]:
                            freq.insert(i, numfreq)
                            res.insert(i, num)
                            break
                numfreq = 1
                num = n
        
        if len(freq) == 0:
            freq.append(numfreq)
            res.append(num)
        else:
            for i in range(len(freq) + 1):
                if i == len(freq):
                    freq.append(numfreq)
                    res.append(num)
                    break
                elif numfreq >= freq[i]:
                    freq.insert(i, numfreq)
                    res.insert(i, num)
                    break

        return res[0:k]

        # Neetcode Solution
        # Time and memory: O(n)
        count = {}
        freq = [[] for i in range(len(nums) + 1)]
        res = []

        for n in nums:
            count[n] = 1 + count.get(n, 0)
        
        for n, c in count.items():
            freq[c].append(n)
        
        for i in range(len(freq) - 1, 0, -1):
            for n in freq[i]:
                res.append(n)
                if len(res) == k:
                    return res