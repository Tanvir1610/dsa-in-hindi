import java.util.ArrayDeque;
import java.util.Deque;

/**
 * DSA Day 3 - Stack (LIFO) | CodewithTanvir
 * Use ArrayDeque (faster than the old java.util.Stack class).
 * Run: java StackDemo.java
 */
public class StackDemo {

    static boolean isBalanced(String s) {
        Deque<Character> stack = new ArrayDeque<>();
        for (char ch : s.toCharArray()) {
            if (ch == '(' || ch == '[' || ch == '{') stack.push(ch);
            else if (ch == ')' || ch == ']' || ch == '}') {
                if (stack.isEmpty()) return false;
                char open = stack.pop();
                if ((ch == ')' && open != '(') || (ch == ']' && open != '[') || (ch == '}' && open != '{')) return false;
            }
        }
        return stack.isEmpty();
    }

    public static void main(String[] args) {
        Deque<String> undo = new ArrayDeque<>();
        undo.push("H");
        undo.push("i");
        undo.push("!");
        System.out.println("Top (peek): " + undo.peek());        // !
        System.out.println("Ctrl+Z -> pop(): " + undo.pop());    // !
        System.out.println("Top now: " + undo.peek());           // i

        System.out.println("isBalanced(\"{[()]}\") = " + isBalanced("{[()]}")); // true
        System.out.println("isBalanced(\"([)]\")   = " + isBalanced("([)]"));   // false
    }
}
