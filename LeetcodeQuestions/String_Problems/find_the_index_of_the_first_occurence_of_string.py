# Given two strings needle and haystack, return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.


class Solution:
    def strStr(self, haystack: str, needle: str) -> int:

        # so we are getting two strings, needle and haystack
        #  the goal is to find where needle will occur inside of haystrack
        #  ie haystack = sadbustsad; needle = sad,
        # `    here we see that there are two occurences of sad in haystack but w
        #  we are only interested in return the first occurence of sad which is index 0 rather than 6

        #  one edge case we can handle right away is if needle is ever larger than haystack in that case we should just return -1

        if len(needle) > len(haystack):
            return -1
        # we are essentially trying to seee if the word needle exists inside of haystack. I think a trie may work here but it might be overkill for this probelm. Since with a trie we can do some string matching
        #  the other idea that comes to mind is to use a sliding window and we can just check starting from each character if a window of len(needle) inside of haystack matches the word we are looking for
