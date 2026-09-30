class Twitter:

    def __init__(self):
        self.user_to_feed = defaultdict(list)
        self.user_to_followings = defaultdict(set)
        self.time = 0


    def postTweet(self, userId: int, tweetId: int) -> None:
        self.time += 1
        self.user_to_feed[userId].append((-self.time, tweetId))
        

    def getNewsFeed(self, userId: int) -> List[int]:
        self.user_to_followings[userId].add(userId)
        heap = []
        for following in self.user_to_followings[userId]:
            temp = self.user_to_feed[following]
            if temp:
                idx = len(temp) - 1
                time, tweet = temp[idx]
                heapq.heappush(heap, (time, tweet, idx, following))
        
        feed = []
        while len(feed) < 10 and heap:
            time, tweet, idx, user = heapq.heappop(heap)
            feed.append(tweet)
            if idx > 0:
                idx -= 1
                time, tweet = self.user_to_feed[user][idx]
                heapq.heappush(heap, (time, tweet, idx, user))
        
        return feed
        

    def follow(self, followerId: int, followeeId: int) -> None:
        self.user_to_followings[followerId].add(followeeId)
        

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if (followerId != followeeId and 
            followeeId in self.user_to_followings[followerId]):
            self.user_to_followings[followerId].remove(followeeId)
        
