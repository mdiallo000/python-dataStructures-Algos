class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        #  we need to sort the input array so that we can later apply logic that will prevent the inclusion of duplicates
        nums.sort()
        #  sorting will cost a time complexity of O(logN)

        def generate(subsets, idx):
            #  what is our base case?
            #  when our idx is the same as the len(nums) that means we have reached the end of our options
            if idx == len(nums):
                res.append(subsets[:])
                return
            #  Now we can add this element into our subset and generate its subsets
            subsets.append(nums[idx])
            #  we now call our function again which will generate the subsets for this path
            generate(subsets, idx+1)
            #  Next we pop out the element to create the other variance
            subsets.pop()

            # Now here comes the real difference maker between this problem and its first version
            # We will need some type a loop that will move the idx whenever we encounter an element that was already chosen previously, this will help us avoid generating duplicate subests
            while idx < len(nums) and nums[idx] == nums[idx+1]:
                idx += 1
            # Now we can call the function again and continue on in our decision tree
