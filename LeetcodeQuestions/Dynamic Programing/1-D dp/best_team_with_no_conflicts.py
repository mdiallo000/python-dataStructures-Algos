class Solution:
    def bestTeamScore(self, scores: List[int], ages: List[int]) -> int:
        #  goal => choose team with highest overall score
        #  score ==  the sum of scores of all the players in the team
        #  no conflicts allowed
        #  we have a conflict if a younger player has a higher score than an
        #  older player

        #  we get two lists, scores and ages
        #  socre[i] == score for that player
        #  ages[i] == age of that player
        #   Potential pattern?
        #  elimimate slow-fast pointers, two pointer, sliding window,
        #  i am leaning towards a greedy solution
        #  but lets examine how this would would by hand anyways
        #  thus far we can pintpoint it down to sorting or some type of greedy?
