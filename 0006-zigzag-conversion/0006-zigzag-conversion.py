class Solution(object):
    def convert(self, s, numRows):
        # Edge case: if rows = 1 or string is shorter than rows, no zigzag happens
        if numRows == 1 or numRows >= len(s):
            return s
        
        # Initialize an empty string for each row
        rows = [""] * numRows
        current_row = 0
        going_down = False
        
        # Iterate through each character in the string
        for char in s:
            rows[current_row] += char
            
            # Change direction when hitting the top or bottom row
            if current_row == 0 or current_row == numRows - 1:
                going_down = not going_down
                
            # Move up or down based on direction
            current_row += 1 if going_down else -1
            
        # Combine all rows into a single string
        return "".join(rows)
