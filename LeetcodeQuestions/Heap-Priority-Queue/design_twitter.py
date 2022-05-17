from collections import defaultdict


class Twitter:

    def __init__(self):
        self.count = 0
        self.FollowerMap = defaultdict(set)
        self.Tweets = defaultdict(list)

    def postTweet(self, userId: int, tweetId: int) -> None:

    def getNewsFeed(self, userId: int) -> List[int]:

    def follow(self, followerId: int, followeeId: int) -> None:
        # how would we follow a user? Well we would create a connection between one user and the other users they want to follow.
        self.FollowerMap

    def unfollow(self, followerId: int, followeeId: int) -> None:
