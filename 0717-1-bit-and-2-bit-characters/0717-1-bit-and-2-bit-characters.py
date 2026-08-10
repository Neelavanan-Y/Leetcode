class Solution(object):
    def isOneBitCharacter(self, bits):
        """
        :type bits: List[int]
        :rtype: bool
        """
        i = 0
        n = len(bits)
        
        # Loop through the array, stopping before the last element
        while i < n - 1:
            if bits[i] == 1:
                i += 2  # Skip the next bit for 2-bit characters (10 or 11)
            else:
                i += 1  # Move 1 step for 1-bit characters (0)
                
        # If the pointer lands exactly on the last index, it is a 1-bit character
        return i == n - 1
