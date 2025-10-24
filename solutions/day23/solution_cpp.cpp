#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    bool hasSameDigits(string s) {
        // Iterate on the string until it is of size 2
        while(s.size() != 2)
        {
            string temp = "";
            // Iterate on the string and add the digits and store in temp
            for(int i = 0; i < s.size() - 1; i++)
            {
                int a = ((s[i] - '0') + (s[i + 1] - '0')) % 10;
                temp.push_back(a + '0');
            }
            s = temp;
        }
        // Base Condition
        return s[0] == s[1];
    }
};