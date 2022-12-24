#include <iostream>
using namespace std;

// A Node is a (Int Node*)
struct Node {
  Node(int value, Node* next = nullptr) : value(value), next(next) {}
  int value;
	Node* next;
};

class MyLinkedList {
public:
  MyLinkedList() = default;
}

//wtf is this
// typedef Node* nodePtr;

int main()
{
  

}