class Solution {
public:
    
    bool isValid(string s) {
        bool ans = true;
        int n = s.size();
        stack<char> st;
        for(int i = 0 ; i < n; i++){
            if (s[i] == '{' || s[i] == '(' || s[i] == '[') {
                st.push(s[i]);
            } 
            else if (!st.empty() && s[i] == ')') {
                if (st.top() == '(') {
                    st.pop();
                } else {
                    ans = false;
                    break;
                }
            } else if (!st.empty() && s[i] == '}') {
                if (st.top() == '{') {
                    st.pop();
                } else {
                    ans = false;
                    break;
                }
            } else if (!st.empty() && s[i] == ']') {
                if (st.top() == '[') {
                    st.pop();
                } else {
                    ans = false;
                    break;
                }
            } 
            
            else{
                ans = false;
                    break;
            }
            
        }
        if(!st.empty()){
            ans = false;
        }
        
         return ans;
        
    }
};