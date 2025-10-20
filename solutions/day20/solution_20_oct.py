from typing import List

class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        count = 0  # Initialize the variable X to 0

        # Loop through each operation in the list
        for op in operations:
            if "-" in op:  # If operation contains '-', decrement X
                count -= 1
            else:  # Otherwise (operation contains '+'), increment X
                count += 1

        return count  # Return the final value of X
