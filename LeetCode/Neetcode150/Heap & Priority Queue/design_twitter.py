# Initial
class Twitter:

    def __init__(self):
        self.tweets = [] # List[(userId, tweetId)]
        self.following = {} # userId -> List[set(userId)]

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweets.append((userId, tweetId))

    def getNewsFeed(self, userId: int) -> List[int]:
        t = 10
        i = len(self.tweets)-1
        feed = []
        if userId not in self.following:
            self.following[userId] = set()

        while i >= 0 and t > 0:
            if self.tweets[i][0] in self.following[userId] or self.tweets[i][0] == userId:
                feed.append(self.tweets[i][1])
                t -= 1
            i -= 1
        return feed

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId in self.following:
            self.following[followerId].add(followeeId)
        else:
            self.following[followerId] = set()
            self.following[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId in self.following and followeeId in self.following[followerId]:
            self.following[followerId].remove(followeeId)


# Neetcode
import heapq
class Twitter:

    def __init__(self):
        self.count = 0
        self.tweets = defaultdict(list)
        self.following = defaultdict(set) # userId -> List[set(userId)]

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweets[userId].append((self.count, tweetId))
        self.count -= 1

    def getNewsFeed(self, userId: int) -> List[int]:
        feed = []
        minHeap = []

        self.following[userId].add(userId)
        for followeeId in self.following[userId]:
            if followeeId in self.tweets:
                index = len(self.tweets[followeeId]) - 1
                count, tweetId = self.tweets[followeeId][index]
                minHeap.append([count, tweetId, followeeId, index-1])
        heapq.heapify(minHeap)

        while minHeap and len(feed) < 10:
            count, tweetId, followeeId, index = heapq.heappop(minHeap)
            feed.append(tweetId)

            if index >= 0:
                count, tweetId = self.tweets[followeeId][index]
                heapq.heappush(minHeap, [count, tweetId, followeeId, index-1])
        return feed


    def follow(self, followerId: int, followeeId: int) -> None:
        self.following[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.following[followerId]:
            self.following[followerId].remove(followeeId)

