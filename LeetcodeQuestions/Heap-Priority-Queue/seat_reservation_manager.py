import heapq

# Design a system that manages the reservation state of n seats that are numbered from 1 to n.

# Implement the SeatManager class:

# SeatManager(int n) Initializes a SeatManager object that will manage n seats numbered from 1 to n. All seats are initially available.
# int reserve() Fetches the smallest-numbered unreserved seat, reserves it, and returns its number.
# void unreserve(int seatNumber) Unreserves the seat with the given seatNumber.


# Example 1:

# Input
# ["SeatManager", "reserve", "reserve", "unreserve", "reserve", "reserve", "reserve", "reserve", "unreserve"]
# [[5], [], [], [2], [], [], [], [], [5]]
# Output
# [null, 1, 2, null, 2, 3, 4, 5, null]

# Explanation
# SeatManager seatManager = new SeatManager(5); // Initializes a SeatManager with 5 seats.
# seatManager.reserve();    // All seats are available, so return the lowest numbered seat, which is 1.
# seatManager.reserve();    // The available seats are [2,3,4,5], so return the lowest of them, which is 2.
# seatManager.unreserve(2); // Unreserve seat 2, so now the available seats are [2,3,4,5].
# seatManager.reserve();    // The available seats are [2,3,4,5], so return the lowest of them, which is 2.
# seatManager.reserve();    // The available seats are [3,4,5], so return the lowest of them, which is 3.
# seatManager.reserve();    // The available seats are [4,5], so return the lowest of them, which is 4.
# seatManager.reserve();    // The only available seat is seat 5, so return 5.
# seatManager.unreserve(5); // Unreserve seat 5, so now the available seats are [5].


class SeatManager:

    #  for this question what we want to do is use a heapq to simulate the behavior of the two functions that need to be implemented
    #  the heapq will follow the min heap behavior

    def __init__(self, n: int):
        self.heap = [-val for val in range(1, n+1)]
        self.heapq.heapify(self.heap)
        print(self.heap)

    def reserve(self) -> int:
        #  the function will just return the lowest numbered table within the heap, this will be easy to do with a min heap since the lowest numbered table will be root of the tree
        val = heapq.heappop(self.heap)
        return -val

    def unreserve(self, seatNumber: int) -> None:
        #  to unreserve a table all we need to is put it back into the heap but make sure the number is negated
        heapq.heappush(-seatNumber)
