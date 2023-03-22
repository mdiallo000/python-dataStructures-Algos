class Solution:

    def sortPeople(self, heights, names):

        container = []

        for i in range(len(names)):
            container.append([heights[i], names[i]])

        container = sorted(container, reverse=True)

        res = []

        for h, n in container:
            res.append(n)
        return res
