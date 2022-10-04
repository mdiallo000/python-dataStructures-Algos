class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        # You are given an array people where people[i] is the weight of the ith person, and an infinite number of boats where each boat can carry a maximum weight of limit. Each boat carries at most two people at the same time, provided the sum of the weight of those people is at most limit.

        # Return the minimum number of boats to carry every given person.
        l = 0
        boats = 0
        r = len(people)-1
        people.sort()
        while l <= r:

            boats += 1
            if people[l] + people[r] <= limit:
                l += 1
            r -= 1

        print(boats)
        return boats
