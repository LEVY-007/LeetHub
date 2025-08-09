
class Solution(object):
    def checkIfPangram(self, sentence):
        """
        :type sentence: str
        :rtype: bool
        """
        alphab = set('abcdefghijklmnopqrstuvwxyz')
        if alphab <= set(sentence.lower()):
            return True
        else:
            return False

