class Solution {
    public int numWaterBottles(int numBottles, int numExchange) {

        int drinkedBottles = 0;   // total bottles drunk
        int emptyBottles = 0;     // empty bottles available

        while (numBottles > 0) {
            // Drink all current full bottles
            drinkedBottles += numBottles;

            // Update empty bottles
            emptyBottles += numBottles;

            // Exchange empty bottles for new ones
            numBottles = emptyBottles / numExchange;

            // Remaining empty bottles after exchange
            emptyBottles = emptyBottles % numExchange;
        }

        return drinkedBottles;
    }
}
