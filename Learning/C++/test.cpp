#include <iostream>

using namespace std;

int main() 
{
    int a = 5;
    int *ptr = &a;
    cout << "ptr = " << ptr << endl;
    cout << "*ptr = " << *ptr << endl;
    return 0;
}