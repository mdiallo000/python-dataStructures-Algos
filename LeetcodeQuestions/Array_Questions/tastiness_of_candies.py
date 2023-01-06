class Solution:
    def maximumTastiness(self, price: List[int], k: int) -> int:
        # You are given an array of positive integers price where price[i] denotes the price of the ith candy and a positive integer k.

        # The store sells baskets of k distinct candies. The tastiness of a candy basket is the smallest absolute difference of the prices of any two candies in the basket.

        # Return the maximum tastiness of a candy basket.
        # ------------------------------------------------------------------------------------------------------------------------
        #  so we are given an list of numbers where the number at i represents the price of the ith candy
        #  we are also given an interger k  where k represents the baskets of distinct candies sold at the store
