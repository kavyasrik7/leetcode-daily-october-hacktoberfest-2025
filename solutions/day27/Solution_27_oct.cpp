class Solution {
    public:
        int numberOfBeams(vector<string>& bank) {
            long long prevCount = 0;  // Stores number of devices in the last non-empty row
            long long beams = 0;      // Stores total number of laser beams
    
            // Traverse each row of the bank
            for (const string &row : bank) {
                long long currCount = 0;  // Count devices ('1') in current row
    
                // Count how many devices are present in this row
                for (char c : row) {
                    if (c == '1') 
                        ++currCount;
                }
    
                // If the row has no devices, skip it
                if (currCount == 0) 
                    continue;
    
                // Beams between previous and current non-empty rows
                beams += prevCount * currCount;
    
                // Update previous row's device count
                prevCount = currCount;
            }
    
            // Return total beams
            return static_cast<int>(beams);
        }
    };
    