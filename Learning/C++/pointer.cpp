#include <iostream>

using namespace std;

// Call by value
void f(int x) {
    x = 200; // x is only locally modified
    cout << "in func, x = " << x << endl;
}

// Call by reference
void f(int *x) {
    *x = 200; // The thing pointing to x = 100 changes to x = 200
    // This permanently affects to value of x outside this function
    cout << "in func, x = " << x << endl;
}

int main() 
{
    // References and Pointers
    int a = 5;
    cout << &a << endl; // &a has type int*
    int *b = &a;
    *b += 1; // Changing the value of *b changes a too
    cout << *b << " " << a << endl;

    // NULL POINTER
    int *var = NULL;
    cout << var << endl; // Output: 0. The address of nothing is nothing!
    // printing *var will lead to a segmentation error. Why is this?

    // VOID/GENERIC POINTER
    void *c = &a;
    cout << *(int *)c << endl; // Output: 6
    // Explanation: We cast c to convert it to an int*, then deference it with another *
    // Use case: Passing pointers to functions that take unknown data types

    // WILD POINTER - simply refers to an uninitialized/deleted/freed/invalid object

    // DANGLING POINTER
    int *d = (int *)malloc(sizeof(int));
    d = &a;
    // free(d); --> doing this gives us an Abort trap (whatever that is)

    // POINTER ARITHMETIC
    int arr[7] = {2, 3, 5, 7, 11, 13, 17};
    int *tr = &arr[6];
    int m = 2;
    for (int i = 0; i < 7; i++) {
        cout << *tr << " ";
        tr -= m;
    } cout << endl;
    // notice that after 4 iterations, tr no longer points to an element
    // in the array, so we get random numbers

    // POINTER TO POINTER
    int *ptr1, **ptr2;
    ptr1 = &a;
    ptr2 = &ptr1;
    cout << "a = " << a << endl;
    cout << "ptr1 = " << *ptr1 << endl;
    // **ptr2 = *ptr1 = a = 5
    cout << "ptr2 = " << **ptr2 << endl;

    // ARRAY OF POINTERS
    int arr2[3] = {2, 3, 5};
    int *parr[3];
    for(int i = 0; i < 3; i++) {
        parr[i] = &arr2[i];
        cout << *parr[i] << " ";
    } cout << endl;

    // CALL BY VALUE
    int x = 100;
    f(x);
    cout << "in main, x = " << x << endl;

    // CALL BY REFERENCE
    f(&x);
    cout << "in main, x = " << x << endl;

    // INSERTION/DELETION
    // Objective: insert 3 in the 3rd position, then remove the element in the 4th position
    int arr3[6] = {1, 2, 0, 4, 5};
    // Insertion
    int n = 3;
    for(int i = 5; i >= n; i--) {
        arr3[i] = arr3[i-1];
    }
    arr3[n-1] = 3;
    for(int i = 0; i < 6; i++) {
        cout << arr3[i] << " ";
    } cout << endl;
    // Deletion
    n = 4;
    for(int i = n-1; i < 6; i++) {
        arr3[i] = arr3[i+1];
    }
    for(int i = 0; i < 6; i++) {
        cout << arr3[i] << " ";
    }

    return 0;
}