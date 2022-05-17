from collections import defaultdict


class Twitter:

    def __init__(self):
        self.count = 0
        self.FollowerMap = defaultdict(set)
        self.Tweets = defaultdict(list)

    def postTweet(self, userId: int, tweetId: int) -> None:
        # whenever a user posts a tweet we need a identifier which will be the userID and we also need the tweet

    def getNewsFeed(self, userId: int) -> List[int]:

    def follow(self, followerId: int, followeeId: int) -> None:
        # how would we follow a user? Well we would create a connection between one user and the other users they want to follow.
        self.FollowerMap[followeeId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.FollowerMap:
            self.FollowerMap[followerId].remove(followeeId)
