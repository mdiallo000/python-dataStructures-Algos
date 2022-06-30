from collections import defaultdict
from email.policy import default


class Solution:
    def invalidTransactions(self, transactions: List[str]) -> List[str]:

        # Input: transactions = ["alice,20,800,mtv","alice,50,100,beijing"]
        # Output: ["alice,20,800,mtv","alice,50,100,beijing"]

        result = []
        userInfo = defaultdict(lambda: defaultdict(set))

        for t in transactions:
            name, time, amount, city = t.split(",")
            userInfo[name][time].add(time)

        for t in transactions:
            name, time, amount, city = t.split(',')
            if int(amount) > 1000:
                result.append(t)
            else:
                for minutes in userInfo[name]:
