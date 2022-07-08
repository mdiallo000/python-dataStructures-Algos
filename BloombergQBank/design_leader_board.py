class Leaderboard:

    def __init__(self):
        self.database = {}

        # Update the leaderboard by adding score to the given player's score. If there is no player with such id in the leaderboard, add him to the leaderboard with the given score.
    def addScore(self, playerId: int, score: int) -> None:
        self.database[palyerId] = score
        # Return the score sum of the top K players.

    def top(self, K: int) -> int:

        # Reset the score of the player with the given id to 0 (in other words erase it from the leaderboard). It is guaranteed that the player was added to the leaderboard before calling this function.

    def reset(self, playerId: int) -> None:
