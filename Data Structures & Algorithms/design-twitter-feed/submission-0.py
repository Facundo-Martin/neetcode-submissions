class Twitter:
    def __init__(self):
        self.count = 0
        self.tweetMap = defaultdict(list)  # userId -> list of [count, tweetId]
        self.followMap = defaultdict(set)  # userId -> set of followeeId

    def postTweet(self, userId: int, tweetId: int) -> None:
        # Append tweet to the right. The most recent tweet is at the end of the list.
        self.tweetMap[userId].append([self.count, tweetId])
        self.count -= 1  # Decrementing makes the most recent tweet the smallest number for the Min-Heap

    def getNewsFeed(self, userId: int) -> List[int]:
        res = []  # Ordered starting from most recent
        minHeap = []

        # Ensure the user always sees their own tweets
        self.followMap[userId].add(userId)
        
        # 1. Grab the single most recent tweet from each followee (O(K) time)
        for followeeId in self.followMap[userId]:
            if followeeId in self.tweetMap:
                index = len(self.tweetMap[followeeId]) - 1
                count, tweetId = self.tweetMap[followeeId][index]
                # Store: [time_count, tweet_id, author_id, next_index_to_check]
                minHeap.append([count, tweetId, followeeId, index - 1])
        
        # Linear heapify is mathematically faster than pushing one by one
        heapq.heapify(minHeap)
        
        # 2. Extract the max (smallest count) up to 10 times (O(10 log K) time)
        while minHeap and len(res) < 10:
            count, tweetId, followeeId, index = heapq.heappop(minHeap)
            res.append(tweetId)
            
            # If this author has more tweets, push their next most recent into the heap
            if index >= 0:
                count, tweetId = self.tweetMap[followeeId][index]
                heapq.heappush(minHeap, [count, tweetId, followeeId, index - 1])
                
        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        self.followMap[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.followMap[followerId]:
            self.followMap[followerId].remove(followeeId)