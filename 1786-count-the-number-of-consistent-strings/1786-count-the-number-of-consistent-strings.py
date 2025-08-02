class Solution(object):
    def countConsistentStrings(self, allowed, words):
        """
        :type allowed: str
        :type words: List[str]
        :rtype: i
        
        """
        
        allowed_set = set(allowed)
        return sum(1 for word in words if set(word).issubset(allowed_set))

