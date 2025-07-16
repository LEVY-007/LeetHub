class Solution(object):
    def maximumWealth(self, accounts):
        """
        :type accounts: List[List[int]]
        :rtype: int
        """
        n=len(accounts)
        max=0
        for i in range(n):
            if sum(accounts[i])>max:
             max=sum(accounts[i])
        return max    
            
