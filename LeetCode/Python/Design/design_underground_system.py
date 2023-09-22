class UndergroundSystem(object):

    def __init__(self):
        self.on = {}
        self.off = {}

    def checkIn(self, id, stationName, t):
        """
        :type id: int
        :type stationName: str
        :type t: int
        :rtype: None
        """
        self.on[id] = (stationName, t)

    def checkOut(self, id, stationName, t):
        """
        :type id: int
        :type stationName: str
        :type t: int
        :rtype: None
        """
        onStation, onTime = self.on[id]
        key = onStation + ' ' + stationName
        if key in self.off:
            self.off[key].append(t - onTime)
        else:
            self.off[key] = [t - onTime]

    def getAverageTime(self, startStation, endStation):
        """
        :type startStation: str
        :type endStation: str
        :rtype: float
        """
        key = startStation + ' ' + endStation
        times = self.off[key]

        sum = 0
        for t in times:
            sum += t
        return float(sum) / float(len(times))


# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)
