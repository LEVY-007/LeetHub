class Solution(object):
    def countConsistentStrings(self, allowed, words):
        """
        :type allowed: str
        :type words: List[str]
        :rtype: i
        
        """
        allowed_set = set(allowed)
        count=0
        for w in words:
            if all(i in allowed_set for i in w):
                count += 1
        return count
