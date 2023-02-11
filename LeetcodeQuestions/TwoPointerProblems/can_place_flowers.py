class Solution:
    def canPlaceFlowers(flowerbed, n):
        #  we have a surface where we can plant flowers aka a flowerbed
        #  One rule is that flowers cannot be placed next to one another
        #  we have a list of ints in binary format
        #  0 means empty at this ith position while 1 means occupied
        #  return true/ false if n flowers can be planted without violating the adjacency rule
        #  this problem false under the two pointer technique catagory
        #  however i dont see how this may apply thus far
        #  test case: [1,0,0,0,1] n = 1 ==> return True since we can place enougth flowers without braking the rule
        #  test case: [1,0,0,0,1] n = 2 ==> return False since we cannot place the flowers unless we brake the rule

        #  the only thing thats comes to mind is kepping a count of the numbers as well as their position iniside of the list, but i cant see how that would solve the problem
        #  i dont see the naive approach either at this point into the problem

        flowerbed = [0] + flowerbed + [0]
        print(flowerbed)
        if n == 0:
            return True
        for i in range(1, len(flowerbed)-1):
            if flowerbed[i] == 1:
                continue
            if flowerbed[i-1] == 0 and flowerbed[i] == 0 and flowerbed[i+1] == 0:
                flowerbed[i] = 1
                n -= 1
                if n == 0:
                    return True
        return False

        #  my initial intuition was correct, but i overlooked one edge case where we could have a list like this [0,0,1]
