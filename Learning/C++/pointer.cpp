#include <iostream>

using namespace std;

// // Call by value
// void func(int x) {
//     x = 200;
//     cout << "in func, x = " << x << endl;
// }

// Call by reference
void func (int *x) {
    *x = 200;
    cout << "in func, x = " << x << endl;
}

int main() 
{
    // int a = 5;
    // // ptr points to the address of a
    // int* ptr = &a;
    // // my guess is the * fetches the value of the variable stored at the address of ptr
    // cout << *ptr;

    // // NULL POINTER
    // int *var = NULL;
    // // Not working, should output nothing?
    // cout << *var;

    // // VOID POINTER
    // int a = 5;
    // void *ptr = &a;
    // cout << *(int *)ptr;

    // // WILD POINTER
    // int *ptr;
    // cout << *ptr;

    // // DANGLING POINTER
    // int *ptr = (int *)malloc(sizeof(int));
    // int a = 5;
    // ptr = &a;
    // free(ptr);
    // cout << *ptr;

    // // POINTER ARITHMETIC
    // int arr[7] = {2, 3, 5, 7, 11, 13, 17};
    // int *tr = &arr[6];
    // int n = 2;
    // for (int i = 0; i < 7; i++) {
    //     cout << *tr << endl;
    //     tr -= n;
    // }

    // // POINTER TO POINTER
    // int var, *ptr1, **ptr2;
    // var = 5;
    // ptr1 = &var;
    // ptr2 = &ptr1;
    // cout << "var = " << var << endl;
    // cout << "ptr1 = " << *ptr1 << endl;
    // // **ptr2 = *ptr1 = var = 5
    // cout << "ptr2 = " << **ptr2 << endl;

    // // ARRAY OF POINTERS
    // int a[3] = {2, 3, 5};
    // int *ptr[3];
    // for(int i = 0; i < 3; i++) {
    //     ptr[i] = &a[i];
    //     cout << *ptr[i] << endl;
    // }

    // // CALL BY VALUE
    // // Basically just local vs global scope right?
    // int x = 100;
    // func(x);
    // cout << "in main, x = " << x << endl;

    // // CALL BY REFERENCE
    // // Important! Addresses modified anywhere are global in scope (that's my guess at least)
    // int x = 100;
    // func(&x);
    // cout << "in main, x = " << x << endl;

    // return 0;

    // INSERTION/DELETION
    // Objective: insert 3 in the 3rd position, then remove the element in the 4th position
    int arr[6] = {1, 2, 0, 4, 5};
    // Insertion
    int n = 3;
    for(int i = 5; i >= n; i--) {
        arr[i] = arr[i-1];
    }
    arr[n-1] = 3;
    for(int i = 0; i < 6; i++) {
        cout << arr[i] << " ";
    }
    cout << endl;
    // Deletion
    n = 4;
    for(int i = n-1; i < 6; i++) {
        arr[i] = arr[i+1];
    }
    for(int i = 0; i < 6; i++) {
        cout << arr[i] << " ";
    }

}