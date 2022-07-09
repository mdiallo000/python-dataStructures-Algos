import heapq


class Leaderboard:

    def __init__(self):
        self.database = {}

        # Update the leaderboard by adding score to the given player's score. If there is no player with such id in the leaderboard, add him to the leaderboard with the given score.
    def addScore(self, playerId: int, score: int) -> None:
        if playerId not in self.database:
            self.database[playerId] = score
        # Return the score sum of the top K players.
        self.database[playerId] += score

    def top(self, K: int) -> int:
        heap = []
        for val in self.database.values():
            heapq.heappush(heap, val)
            if len(heap) > K:
                heapq.heappop(heap)
        Top_scores = 0
        while heap:
            Top_scores += heapq.heappop(heap)
        return Top_scores

        # Reset the score of the player with the given id to 0 (in other words erase it from the leaderboard). It is guaranteed that the player was added to the leaderboard before calling this function.

    def reset(self, playerId: int) -> None:
        del self.database[playerId]
