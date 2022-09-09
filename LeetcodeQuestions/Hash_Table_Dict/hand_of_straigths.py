class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:

        if len(hand) % groupSize != 0:
            return False

        count = Counter(hand)

        while count:
            minNum = min(count.keys())

            for i in range(groupSize):

                if (minNum + i) in count:
                    if count[minNum + i] == 1:
                        del count[minNum + i]
                    else:
                        count[minNum + i] -= 1

                else:
                    return False
        return True
