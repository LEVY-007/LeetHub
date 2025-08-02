class Solution(object):
    def subtractProductAndSum(self, n):
        """
        :type n: int
        :rtype: int
        """
        sum=0
        product=1
        while n>0:
            m=n%10
            sum= sum+m
            product=product*m
            n=n//10
        return product-sum
             