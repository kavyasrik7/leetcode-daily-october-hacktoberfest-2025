class Solution {
    public int finalValueAfterOperations(String[] operations) {
        int X = 0; // Initialize the variable X to 0

        // Loop through all operations
        for (String op : operations) {
            // If the operation contains "++", increment X
            if (op.contains("++")) {
                X++;
            } 
            // Otherwise, it must be a decrement operation ("--")
            else {
                X--;
            }
        }

        // Return the final value of X after performing all operations
        return X;
    }
}
