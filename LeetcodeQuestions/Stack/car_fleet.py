from inspect import BoundArguments


class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:

        cars = []

        for p, s in zip(position, speed):
            cars.append([p, s])
        cars = sorted(cars)[::-1]

        #  Now we calculate the arrival time with the formula (T + P)/s
        arrivals = []

        for p, s in cars:
            time = self.calculateArrival(target, p, s)
            arrivals.append(time)
        # Now that we know at which time each care will arrive we can now determine how many fleets will be created as the cars run into one another
        fleet = 0
        boundedTime = None
        for time in arrivals:

            if not boundedTime or time > boundedTime:
                boundedTime = time
                fleet += 1
        return fleet

    def calculateArrival(self, target, p, s):
        return (target - p) / s
