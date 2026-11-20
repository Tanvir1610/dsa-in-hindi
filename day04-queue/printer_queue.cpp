// DSA Day 4 - Queue (FIFO) | CodewithTanvir
// Compile & run:  g++ printer_queue.cpp -o printer_queue && ./printer_queue
#include <iostream>
#include <queue>
#include <string>
using namespace std;

int main() {
    queue<string> prints;
    prints.push("Rahul.pdf");   // enqueue at the rear
    prints.push("Priya.pdf");
    prints.push("Aman.pdf");

    cout << prints.front() << "\n";  // Rahul.pdf
    prints.pop();                     // dequeue from the front
    cout << "Next: " << prints.front() << ", size " << prints.size() << "\n";
    return 0;
}
