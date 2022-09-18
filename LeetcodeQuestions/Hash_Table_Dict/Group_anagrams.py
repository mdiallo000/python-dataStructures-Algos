# Given an array of strings strs, group the anagrams together. You can return the answer in any order.

# Input: strs = ["eat","tea","tan","ate","nat","bat"]
# Output: [["bat"],["nat","tan"],["ate","eat","tea"]]

# Input: strs = [""]
# Output: [[""]]

# Input: strs = ["a"]
# Output: [["a"]]

from collections import defaultdict


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        #  Initiate a HashMap
        hashmap = {}
        # For each element in our array we will take an element sort it and join it back together ex: for "eat" key will be aet, for "ant" key will be ant so on
        for elem in strs:
            key = ''.join(sorted(elem))
        #  Now for each key we will check if its not in our hashMap, since its not we will first initialize an array and then append it its corresponding element into the array.
        #  The insight here is that since anagrams are have the same letter and frequency we will used the Keys as a way of inserting each elem in the correct array
            if key not in hashmap:
                hashmap[key] = []
                hashmap[key].append(elem)
            else:
                #  If we already encountered the key then we just put the corresponding elem into the correct list so what we get is {"aet": ['eat', 'tea', aet]} and so on for each key
                hashmap[key].append(elem)
        # Finally we put all the values of our hashmap into an array giving us the desired outcome [["bat"],["nat","tan"],["ate","eat","tea"]]
        return list(hashmap.values())

    def groupAnagramsOptimized(self, strs):

        Map = defaultdict(list)

        for wrd in strs:
            count = [0] * 26
            for char in wrd:
                count[ord(char) - ord('a')] += 1
            Map[tuple(count)].append(wrd)
        return list(Map.values())
        # This is a much optimized approach with a time complexity of N*K rather than N*Klogk from the more naive approach above which also required us to sort every word in the list
