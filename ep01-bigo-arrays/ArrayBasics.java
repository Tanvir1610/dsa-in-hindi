/**
 * Episode 1 - Arrays in Java (code shown in the video) | CodewithTanvir
 * Java arrays have a FIXED size. Use ArrayList if you need it to grow.
 * Run: java ArrayBasics.java
 */
public class ArrayBasics {
    public static void main(String[] args) {
        int[] arr = {10, 20, 30, 40};

        System.out.println(arr[2]);      // 30
        System.out.println(arr.length);  // 4

        for (int x : arr) {              // traverse O(n)
            System.out.print(x + " ");
        }
        System.out.println();
        // arr[4] = 50;  -> ArrayIndexOutOfBoundsException (common mistake from the video!)
    }
}
