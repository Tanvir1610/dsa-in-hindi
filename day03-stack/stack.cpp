// DSA Day 3 - Stack (LIFO) | CodewithTanvir
// Compile & run:  g++ stack.cpp -o stack && ./stack
#include <iostream>
#include <stack>
#include <string>
using namespace std;

bool isBalanced(const string& s) {
    stack<char> st;
    for (char ch : s) {
        if (ch == '(' || ch == '[' || ch == '{') st.push(ch);
        else if (ch == ')' || ch == ']' || ch == '}') {
            if (st.empty()) return false;
            char open = st.top(); st.pop();
            if ((ch == ')' && open != '(') || (ch == ']' && open != '[') || (ch == '}' && open != '{')) return false;
        }
    }
    return st.empty();
}

int main() {
    stack<string> undo;
    undo.push("H"); undo.push("i"); undo.push("!");
    cout << "Top: " << undo.top() << "\n";          // !
    undo.pop();                                       // Ctrl+Z
    cout << "After Ctrl+Z, top: " << undo.top() << "\n";  // i

    cout << boolalpha;
    cout << "isBalanced(\"{[()]}\") = " << isBalanced("{[()]}") << "\n";  // true
    cout << "isBalanced(\"([)]\")   = " << isBalanced("([)]") << "\n";    // false
    return 0;
}
