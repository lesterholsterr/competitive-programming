# https://leetcode.com/problems/reconstruct-itinerary/

# Initial solution: Mem limit exceeded
# Let's see if the only difference was pre-sorting the array and short circuiting...
class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        # Backtracking required - can't necessarily take the lexically first flight leaving JFK
        # (e.g. [JFK, SFO], [JFK, ATL], [SFO, JFK] requires you to go to SFO before ATL)
        # At airport A, suppose I have unused tickets to airports [X_1, X_2, ..., X_n]
        # I have n choices
        # If n == 0 and I have no tickets left, I am done
        # If n == 0 and I have unused tickets, invalid solution
        # Keep track of all valid solutions, then sort lexicographically

        # Graph theory: This is a Eulerian circuit!
        # Properties: Each node even degree except the starting one?
        # Proof: Eliminate cycles until you have a path. Each edge used exactly once.
        # How to find cycles?
        
        adj = {} # str -> Map<str -> int>
        for frm, to in tickets:
            if frm in adj:
                if to in adj[frm]:
                    adj[frm][to] += 1
                else:
                    adj[frm][to] = 1
            else:
                adj[frm] = {to: 1}

        itineraries = []
        cur = ["JFK"]
        num_flights = [len(tickets)]

        def bt(frm: str) -> None:
            if frm in adj:
                destinations = adj[frm]
                for to in destinations.keys():
                    if adj[frm][to] > 0:
                        num_flights[0] -= 1
                        adj[frm][to] -= 1
                        cur.append(to)
                        bt(to)
                        num_flights[0] += 1
                        adj[frm][to] += 1
                        cur.pop()

            if num_flights[0] == 0:
                itineraries.append(cur.copy())
        
        bt("JFK")
        itineraries.sort(key=lambda x: ''.join(x))
        print(itineraries)
        return itineraries[0]

# Neetcode
# Hmm now it TLEs
class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        adj = { frm: [] for frm, to in tickets }
        tickets.sort(key=lambda x: ''.join(x))
        for frm, to in tickets:
            adj[frm].append(to)
        
        res = ["JFK"]
        def dfs(frm: str) -> bool:
            if len(res) == len(tickets) + 1:
                return True
            elif frm not in adj:
                return False
            
            destinations = adj[frm].copy()
            for i, to in enumerate(destinations):
                res.append(adj[frm].pop(i))
                if dfs(res[-1]):
                    return True
                adj[frm].insert(i, res.pop())
            return False
            
        dfs("JFK")
        return res

# Witchcraft solution
# https://leetcode.com/problems/reconstruct-itinerary/solutions/4041944/95-76-dfs-recursive-iterative/
# Apparently it's called Heirholzer's algorithm
# Eulerian circuit - go until you get stuck
# Just retrace your steps and look for cycles along the way
# I remembered the theory from MATH239 but couldn't figure out the algorithm
# Fucking elegant implementation
class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        adj = defaultdict(list)
        for frm, to in sorted(tickets, reverse=True): # <-- why sort in reverse?
            adj[frm].append(to)
        
        res = []
        def dfs(frm: str) -> bool:
            while adj[frm]:
                dfs(adj[frm].pop()) # <-- Answer: so you can take the smallest one by POPPING
            res.append(frm)
            
        dfs("JFK")
        return res[::-1] # notice the last line in dfs(). we build res in reverse as the call stack unwinds
