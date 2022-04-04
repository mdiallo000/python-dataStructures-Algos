# Given an array of strings strs, group the anagrams together. You can return the answer in any order.

# Input: strs = ["eat","tea","tan","ate","nat","bat"]
# Output: [["bat"],["nat","tan"],["ate","eat","tea"]]

# Input: strs = [""]
# Output: [[""]]

# Input: strs = ["a"]
# Output: [["a"]]

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap = {}

        for elem in strs:
            key = ''.join(sorted(elem))
            if key not in hashmap:
                hashmap[key] = []
                hashmap[key].append(elem)
            else:
                hashmap[key].append(elem)
        return list(hashmap.values())
