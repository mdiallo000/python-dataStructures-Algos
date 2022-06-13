from tkinter.tix import ROW


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        #  we need the dimensions of the board

        ROWS = len(board)
        COLUMS = len(board[0])
        #  we also need to keep track of the characters we have already visited
        path = set()

        def pathfinder(r, c, idx):
            #  if our idx becomes the same as the words that means we have come accross every charcacter and the word does exist in the board.
            if idx == len(word):
                return True
            # now we chech to see if the word exist

            if r < 0 or r == ROWS or c < 0 or c == COLUMS or (r, c) in path or word[idx] != board[r][c]:
                return False
            path.add((r, c))
            res = (pathfinder(r+1, c, idx+1) or
                   pathfinder(r-1, c, idx+1) or
                   pathfinder(r, c+1, idx+1) or
                   pathfinder(r, c-1, idx+1))
            path.remove((r, c))
            return res

        for r in range(ROWS):
            for c in range(COLUMS):
                if pathfinder(r, c, 0):
                    return True
        return False
#  Time complexity will be O (n*m*pathfinder)
#  O of pathfindder is 4^N since we are calling the function fours times which will depend on the lenght of our word N
