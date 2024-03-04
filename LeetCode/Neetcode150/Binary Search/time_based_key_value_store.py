# Overall: Just another "binary search with a twist" question. Took me 2 submissions but I found all
# the edge cases.

# Initial Solution
class TimeMap:

    def __init__(self):
        self.store = {}
        # {key: List of (timestamp, val)}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key in self.store:
            self.store[key].append((timestamp, value))
        else:
            self.store[key] = [(timestamp, value)]

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.store:
            return ""

        arr = self.store[key]
        if len(arr) == 0:
            return ""
        elif arr[-1][0] < timestamp:
            return arr[-1][1]

        l, r = 0, len(arr)-1
        while l <= r:
            mid = (l + r) // 2
            t = arr[mid][0]
            if t == timestamp:
                return arr[mid][1]
            elif t < timestamp and mid+1 <= len(arr)-1 and arr[mid+1][0] > timestamp:
                return arr[mid][1]
            elif t > timestamp:
                r = mid - 1
            else:
                l = mid + 1
        return ""

# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)

# Neetcode Solution
# Other 2 functions the same. Much more concise binary search. 
def get(self, key: str, timestamp: int) -> str:
        res = ""
        values = self.store.get(key, [])

        l, r = 0, len(values) - 1
        while l <= r:
            m = (l + r) // 2
            if values[m][0] <= timestamp:
                res = values[m][1]
                l = m + 1
            else:
                r = m - 1
        return res