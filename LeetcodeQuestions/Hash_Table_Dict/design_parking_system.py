# Design a parking system for a parking lot. The parking lot has three kinds of parking spaces: big, medium, and small, with a fixed number of slots for each size.

# Implement the ParkingSystem class:

# ParkingSystem(int big, int medium, int small) Initializes object of the ParkingSystem class. The number of slots for each parking space are given as part of the constructor.
# bool addCar(int carType) Checks whether there is a parking space of carType for the car that wants to get into the parking lot. carType can be of three kinds: big, medium, or small, which are represented by 1, 2, and 3 respectively. A car can only park in a parking space of its carType. If there is no space available, return false, else park the car in that size space and return true.


# Example 1:

# Input
# ["ParkingSystem", "addCar", "addCar", "addCar", "addCar"]
# [[1, 1, 0], [1], [2], [3], [1]]
# Output
# [null, true, true, false, false]

# Explanation
# ParkingSystem parkingSystem = new ParkingSystem(1, 1, 0);
# parkingSystem.addCar(1); // return true because there is 1 available slot for a big car
# parkingSystem.addCar(2); // return true because there is 1 available slot for a medium car
# parkingSystem.addCar(3); // return false because there is no available slot for a small car
# parkingSystem.addCar(1); // return false because there is no available slot for a big car. It is already occupied.

# so we need to create an object which functions like a parking system.
# With just two functions to do the bulk of the work
# the init function takes in three arguments, big, medium, small, these will be integers that will let us no how much of each parking spot type is still available. So right away i am thinking of some type of hastable where we can have the three types of parking spots as the keys and then we will map for its value the amount of spaces that have been allocated for that slot.
# Now how do i deal with the fact that the ints 1,2,3 will represent the types again, maybe i can do some type of conversition to map
class ParkingSystem:

    def __init__(self, big: int, medium: int, small: int):

    def addCar(self, carType: int) -> bool:

        # Your ParkingSystem object will be instantiated and called as such:
        # obj = ParkingSystem(big, medium, small)
        # param_1 = obj.addCar(carType)
