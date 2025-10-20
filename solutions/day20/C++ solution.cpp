// Time complexity: O(n)
// Space complexity: O(n)
// Using string traversal to check for operations
class Solution {
public:
    int finalValueAfterOperations(vector<string>& a) {
        int x=0; // to store the final value
        for(int i=0;i<a.size();i++) // iterating through the array of operations
        {
            if(a[i][0]=='-' || a[i][2]=='-') // check for decrement
            {
                x--;
            }
            else{ // else increment
                x++;
            }
        }
        return x;   // return the final value
    }
};