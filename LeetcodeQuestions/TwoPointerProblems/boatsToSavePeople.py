class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        # You are given an array people where people[i] is the weight of the ith person, and an infinite number of boats where each boat can carry a maximum weight of limit. Each boat carries at most two people at the same time, provided the sum of the weight of those people is at most limit.

        # Return the minimum number of boats to carry every given person.
        l = 0
        curr = 0
        boats = 1
        r = len(people)-1
        people.sort()
        while r < len(people)-1:
            curr = limit - people[r]
            r -= 1
            boats += 1
            if l <= r and curr >= people[l]:
                l += 1

        print(boats)
        return boats
