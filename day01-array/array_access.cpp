// DSA Day 1 - Array access is O(1) | CodewithTanvir
// C++ lets us SEE the real memory addresses: each int is exactly 4 bytes apart.
//
// Compile & run:  g++ array_access.cpp -o array_access && ./array_access
#include <iostream>
#include <cstdint>
using namespace std;

int main() {
    int arr[10] = {10, 20, 30, 40, 50, 60, 70, 80, 90, 100};

    cout << "Real addresses (contiguous, " << sizeof(int) << " bytes apart):\n";
    for (int i = 0; i < 10; i++) {
        cout << "arr[" << i << "] = " << arr[i] << "  at  " << (void*)&arr[i] << "\n";
    }

    // The formula the CPU uses: address = start + index * size
    uintptr_t start = (uintptr_t)&arr[0];
    int index = 7;
    uintptr_t computed = start + index * sizeof(int);
    cout << "\nFormula for index 7: start + 7 * " << sizeof(int)
         << " = " << (void*)computed
         << (computed == (uintptr_t)&arr[7] ? "  (matches &arr[7]!)" : "") << "\n";
    cout << "So arr[7] is found in 1 step -> O(1)\n";
    return 0;
}
