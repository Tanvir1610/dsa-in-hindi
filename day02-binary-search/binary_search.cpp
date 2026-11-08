// DSA Day 2 - Binary Search, O(log n) | CodewithTanvir
// Compile & run:  g++ binary_search.cpp -o binary_search && ./binary_search
#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int binarySearch(const vector<int>& arr, int x) {
    int lo = 0, hi = (int)arr.size() - 1;
    while (lo <= hi) {
        int mid = lo + (hi - lo) / 2;  // avoids overflow for huge arrays
        if (arr[mid] == x) return mid;
        else if (arr[mid] < x) lo = mid + 1;
        else hi = mid - 1;
    }
    return -1;
}

int main() {
    vector<int> arr = {3, 8, 12, 17, 25, 34, 41, 58, 63, 70};
    cout << "Index of 63: " << binarySearch(arr, 63) << "\n";  // 8
    cout << "Index of 5:  " << binarySearch(arr, 5) << "\n";   // -1

    // The STL already has it: lower_bound returns the first position >= x
    auto it = lower_bound(arr.begin(), arr.end(), 63);
    cout << "STL lower_bound(63) -> index " << (it - arr.begin()) << "\n";
    return 0;
}
