class Solution:
    def bestTeamScore(self, scores: List[int], ages: List[int]) -> int:
        #  goal => choose team with highest overall score
        #  score ==  the sum of scores of all the players in the team
        #  no conflicts allowed
        #  we have a conflict if a younger player has a higher score than an
        #  older player

        #  we get two lists, scores and ages
        #  score[i] == score for that player
        #  ages[i] == age of that player
        #   Potential pattern?
        #  eliminate slow-fast pointers, two pointer, sliding window,
        #  i am leaning towards a greedy solution
        #  but lets examine how this would would by hand anyways
        #  thus far we can pint point it down to sorting or some type of greedy?
        #  after checking the related topics its clear that this will involve sorting than  dynamic programing for better optimization
        # scores = [1,3,5,10,15], ages = [1,2,3,4,5]
        #  zip  trough both list and add the age and score of each person into a tuple or list
        #  now with the new list we can check for the condition

        data = []
        for a, s in zip(ages, scores):
            data.append([a, s])
        n = len(data)
        dp_table = [0]
