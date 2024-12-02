# https://leetcode.com/problems/hand-of-straights/

# Took a while to figure out the data structure of Map<int -> List<int>>
# Works because you can pop from these lists in O(1) time
class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        num_cards = len(hand)
        if num_cards % groupSize != 0:
            return False
        elif groupSize == 1:
            return True

        hand.sort()
        incomplete = {}
        for i in range(num_cards):
            cur = hand[i]
            if cur-1 in incomplete and incomplete[cur-1]:
                group_len = incomplete[cur-1].pop()
                if group_len + 1 != groupSize:
                    if cur in incomplete:
                        incomplete[cur].append(group_len + 1)
                    else:
                        incomplete[cur] = [group_len + 1]
            else:
                if cur in incomplete:
                    incomplete[cur].append(1)
                else:
                    incomplete[cur] = [1]
        
        for arr in incomplete.values():
            if arr:
                return False
        return True