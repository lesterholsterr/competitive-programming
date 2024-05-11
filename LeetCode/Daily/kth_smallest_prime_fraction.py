# thoughts
# - hm never crossed my mind to use binary search. the thing to search for is the number of 
#   fractions greater/less than mid. Even though that takes linear time to find, that makes
#   the algorithm O(nlogn) which is good enough.

# Initial - brute force TLE same old story
class Solution:
    def kthSmallestPrimeFraction(self, arr: List[int], k: int) -> List[int]:
        def nextSmallest():
            minsofar = inf
            minindex = -1
            num, den = -1, -1
            for i in range(len(fractions)):
                a, b = fractions[i][0], fractions[i][1]
                if arr[a]/arr[b] < minsofar:
                    minsofar = arr[a]/arr[b]
                    minindex = i
                    num, den = arr[a], arr[b]
            fractions[minindex][1] -= 1
            return num, den

        fractions = []
        for i in range(len(arr)-1):
            fractions.append([i, len(arr)-1])

        i, j = -1, -1
        while k:
            i, j = nextSmallest()
            k -= 1

        return [i, j]
    
# Actual solution: binary search
class Solution:
    def kthSmallestPrimeFraction(self, arr: List[int], k: int) -> List[int]:
        l, r = 0, 1
        while True:
            mid = (l + r) / 2
            count, f, num, den = 0, 0, 0, 0
            for i in range(len(arr)):
                j = 1 # <-- this can be moved outside of the for loop. Makes the code an order faster on leetcode.
                while j < len(arr) and arr[i]/arr[j] >= mid:
                    j += 1
                count += len(arr)-j
                
                if j < len(arr) and f < arr[i] / arr[j]:
                    f = arr[i] / arr[j]
                    num, den = arr[i], arr[j]
            
            if count == k:
                return [num, den]
            elif count > k:
                r = mid
            else:
                l = mid