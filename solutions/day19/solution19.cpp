#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    void dfs(string s, int a, int b, set<string>& store) {
        if (store.count(s)) return; 
        store.insert(s);      
        int n = s.size();

        string addStr = s;
        for (int i = 1; i < n; i += 2) {
            addStr[i] = ((addStr[i] - '0' + a) % 10) + '0';
        }
        dfs(addStr, a, b, store);
        
        string rotStr = s.substr(n - b) + s.substr(0, n - b);
        dfs(rotStr, a, b, store);
    }
    
    string findLexSmallestString(string s, int a, int b) {
        set<string> store; 
        dfs(s, a, b, store);
        
        string ans = *store.begin();
        for (auto &str : store) {
            if (str < ans) ans = str;
        }
        return ans;
    }
};
