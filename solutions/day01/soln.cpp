class Solution {
public:
    int numWaterBottles(int numBottles, int numExchange) {
        int totalDrunk = 0;
        int empty = 0;

        while (numBottles > 0) {
            totalDrunk += numBottles;
            empty += numBottles;

            // Exchange empty bottles for new full bottles
            numBottles = empty / numExchange;
            empty = empty % numExchange;
        }

        return totalDrunk;
    }
};
