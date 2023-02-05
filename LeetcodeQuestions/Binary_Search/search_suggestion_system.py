class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        # You are given an array of strings products and a string searchWord.

        # Design a system that suggests at most three product names from products after each character of searchWord is typed. Suggested products should have common prefix with searchWord. If there are more than three products with a common prefix return the three lexicographically minimums products.

        # Return a list of lists of the suggested products after each character of searchWord is typed.

        #  The system needs to suggest not more than three product names from the list of products we are initially given

        #  We are looking for products that have a common prefix with the searchword that was given as well

        #  ex: products = [mousepad, microphone, mackbook, iphone, chromebook, watch]
        #  searchword = mackbook

        #  sort of stuck as to how i may approach the problem.
        #  Thus far i am thinking of a prefix tree that can help us derive the common products to the searchword.

        #  so the way we solve the problem will involve using a bit of binary search indirectly
        # We first sort the list of products, now that it sorted we can use two pointers, a left at the start of the first character of the first word in the list, and the last pointer at the first character of the last word in the list. Now we just check wheter the char[l] and char[r] are equal to the character we are currently looking at in the searchword.
        #  If no then we move the left pointer to the next word in the products and repeat the this process until we have a match.
        #  The same will apply for the right pointer
        #  If the both the left and right pointer happen to match with the search word that means
