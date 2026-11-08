/**
 * DSA Day 1 - Array access is O(1) | CodewithTanvir
 * address = start + index * size  (contiguous memory)
 *
 * Run: java ArrayAccess.java
 */
public class ArrayAccess {

    static long addressOf(long start, long index, int size) {
        return start + index * size;
    }

    public static void main(String[] args) {
        long start = 1000;
        int size = 4; // an int is 4 bytes
        System.out.println("Address formula: start + index * size");
        System.out.println("index 7      -> " + addressOf(start, 7, size));       // 1028
        System.out.println("index 700000 -> " + addressOf(start, 700_000, size)); // 2801000

        int[] arr = new int[1_000_000];
        for (int i = 0; i < arr.length; i++) arr[i] = i;

        int steps = 0;
        for (int i = 0; i < arr.length; i++) { // the slow way: O(n)
            steps++;
            if (i == 700_000) break;
        }
        System.out.println("\nCounting one by one: " + steps + " steps");
        System.out.println("Direct access arr[700000] = " + arr[700_000] + "  ->  1 step, O(1)");
    }
}
