class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        s = s.lower()                          # Convert to lowercase
        s = ''.join(c for c in s if c.isalnum())  # Remove non-alphanumeric characters
        return s == s[::-1]                    # Check if string equals its reverse
