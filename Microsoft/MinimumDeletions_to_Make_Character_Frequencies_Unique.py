class Solution:
    # This approach is based on the observation that if multiple characters have the same frequency, then only one character can keep all of its instances. All other characters must have one or more of their instances deleted.

    # In this approach, we will push the frequency of each number into a max heap. Then, at each step, we will compare the top two elements in the heap. If they are the same, we will decrement one of them and push it back into the heap. Every time we detect that the two top elements are equal, we will increment the variable deleteCount.

    # An important point here is that when we compare the top two elements, we do so by popping the top element and comparing it to the new top element in the heap. Then, if the top two elements are equal, we will decrement the popped element by 111 so that the two elements are no longer equal, and then we can push the popped element back into the heap. Only when the top two elements are not equal can we say that the top element is unique and can be removed from the heap.

    def minDeletions(self, s: str) -> int:
        count = [] * 26

        for char in s:
            count[ord(char) - ord('a')] += 1
        #  now that we have the the frequencies of all the char, now lets create a max-heap
        heap = [-freq for freq in count]
        print(heap)
        heapq.heapify(heap)
        deletions = 0

        while len(heap) > 1:
            #  now we pop the topmost element and compare it with the new top element, if they happen to be the same then we can decremnt it, incremnet our deletions variable and then we will push it back into heap
            curr = heapq.heappop(heap)

            if curr == heap[0]:
                curr -= 1
                deletions += 1
                heapq.heappush(heap, curr)
