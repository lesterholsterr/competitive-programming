# https://leetcode.com/problems/asteroid-collision/description/?envType=company&envId=facebook&favoriteSlug=facebook-thirty-days

# Initially tried to use "prefix arrays" before realizing stack was better
# Intuition: Find rules for when asteroids collide
# - One on the left must be +, one on the right must be -
# - Now start thinking about cases (one destroys another, destroy each other, etc.)
# - From there, many ways to implement the rules. Hard part is not missing any rules

class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        intact = True

        for a in asteroids:
            while stack and a < 0 < stack[-1]:
                if abs(a) > stack[-1]:
                    stack.pop()
                    continue
                elif abs(a) == stack[-1]:
                    stack.pop()
                # implicit else: abs(a) < stack[-1]
                intact = False
                break
            
            if intact:
                stack.append(a)
            intact = True
        
        return stack
