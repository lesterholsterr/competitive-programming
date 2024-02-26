# Overall: Was definitely overthinking. I think I tunnelled on integer division, which actually
# makes things a lot harder.
# Leaps
# - If the car behind me cannot pass me, then NO cars behind me can ever pass me.
#   This observation lends itself to traversing the cars from closest to the end
#   to furthest from the end and using a STACK.

import math

# Initial Solution: Doesn't work. Tried a brute force strategy but too many conditions/edge cases to keep track of. Really can't think of any ways to optimize and it's been 1 hour.
class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        fleets = 0

        def max_index(arr):
            maxsofar, index = -1, -1
            for i in range(len(arr)):
                if arr[i] > maxsofar:
                    maxsofar = arr[i]
                    index = i
            return index

        eta = [math.ceil((target - p)/s) for p, s in zip(position, speed)]
        while sum(eta) != 0:
            slowest_index = max_index(eta)
            fleets += 1
            
            # every car behind the slowest arriver will arrive in that same fleet
            # every car in front of the slowest arriver arriving at the same time will also arrive in the same fleet if
            # it is driving slower than the slowest arriver. Otherwise, they will arrive by themselves or in another fleet.
            # (there is no way it gets 'blocked' by another slower fleet, else there would be another fleet that arrives even slower)
            slowest_pos = position[slowest_index]
            for i in range(len(position)):
                if i == slowest_index:
                    pass
                elif position[i] < slowest_pos and speed[i] > speed[slowest_index]:
                    eta[i] = 0
                elif eta[i] == eta[slowest_index] and speed[i] < speed[slowest_index]:
                    eta[i] = 0
            eta[slowest_index] = 0

        return fleets
    
# Neetcode Solution
class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # "List comprehension"
        pair = [[p, s] for p, s in zip(position, speed)]
        stack = []

        # Reverse sorted order <-- did not know sorted() would work on a list of lists
        for p, s in sorted(pair)[::-1]:
            if len(stack) == 0:
                stack.append([p, s])
                continue
            
            p1, s1 = stack[-1]
            # if this car arrives slower than the car in front, then it is its own car fleet
            if (target-p)/s > (target-p1)/s1:
                stack.append([p, s])
        
        return len(stack)