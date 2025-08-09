class Solution(object):
    def mostWordsFound(self, sentences):
        """
        :type sentences: List[str]
        :rtype: int
        """
        max=0
        for i in sentences:
            i=i.split()
            n=len(i)
            if max<n:
                max=n
        return max
