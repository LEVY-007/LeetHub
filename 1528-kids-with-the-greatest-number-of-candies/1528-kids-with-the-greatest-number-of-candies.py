class Solution(object):
    def kidsWithCandies(self, candies, extraCandies):
        n=len(candies)
        max=0
        boo=candies
        for i in range(n):
            if (candies[i]>max):
                max=candies[i]
        for i in range(n):
            if (candies[i]+extraCandies>=max):
                boo[i]=True
            else:
                boo[i]=False
        return boo
        
