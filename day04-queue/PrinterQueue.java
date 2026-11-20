import java.util.ArrayDeque;
import java.util.Queue;

/**
 * DSA Day 4 - Queue (FIFO) | CodewithTanvir
 * offer() = enqueue, poll() = dequeue, peek() = front. All O(1) with ArrayDeque.
 * Run: java PrinterQueue.java
 */
public class PrinterQueue {
    public static void main(String[] args) {
        Queue<String> prints = new ArrayDeque<>();
        prints.offer("Rahul.pdf");
        prints.offer("Priya.pdf");
        prints.offer("Aman.pdf");

        System.out.println(prints.poll()); // Rahul.pdf (first in, first out)
        System.out.println(prints);        // [Priya.pdf, Aman.pdf]
        System.out.println("Next: " + prints.peek());
    }
}
