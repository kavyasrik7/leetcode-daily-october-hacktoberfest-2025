// Time complexity: O(n^2)
// Space complexity: O(n^2)
// Using BFS
class Solution {
public:
    void rotate(string &s, int b){
           reverse(s.begin(),s.end());
           reverse(s.begin(),s.begin()+b);
           reverse(s.begin()+b,s.end()); 
        }
    string findLexSmallestString(string s, int a, int b) {
        unordered_set<string>visited;
        queue<string>q;
        string smallest=s;
        q.push(s);
        visited.insert(s);

        while(!q.empty()){
            string curr= q.front();
            q.pop();

            if(curr<smallest)
            smallest=curr;

            string temp=curr; //since we want to do both operation on same
            //add to odd places
            for(int i=1;i<temp.length();i+=2){
                temp[i]=((temp[i]-'0'+a)%10)+'0'; // Note that -"0" and +"0" is to convert char to int and int to char 
            }
            if(!visited.count(temp)){
            visited.insert(temp);
            q.push(temp);
            }

            //rotate by b to right
            rotate(curr,b);
            if(!visited.count(curr)){
            visited.insert(curr);
            q.push(curr);
            }
        }
        return smallest;
    }
};