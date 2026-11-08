/**
 * DSA Day 2 - Binary Search, O(log n) | CodewithTanvir
 * Run: java BinarySearch.java
 */
public class BinarySearch {

    static int binarySearch(int[] arr, int x) {
        int lo = 0, hi = arr.length - 1;
        while (lo <= hi) {
            int mid = lo + (hi - lo) / 2; // same as (lo+hi)/2 but can't overflow
            if (arr[mid] == x) return mid;
            else if (arr[mid] < x) lo = mid + 1;
            else hi = mid - 1;
        }
        return -1;
    }

    public static void main(String[] args) {
        int[] arr = {3, 8, 12, 17, 25, 34, 41, 58, 63, 70};
        System.out.println("Index of 63: " + binarySearch(arr, 63)); // 8
        System.out.println("Index of 5:  " + binarySearch(arr, 5));  // -1

        int n = 10_000_000; // 1 crore
        int steps = 32 - Integer.numberOfLeadingZeros(n); // floor(log2 n) + 1
        System.out.println("1 crore elements -> max " + steps + " steps"); // 24
    }
}
