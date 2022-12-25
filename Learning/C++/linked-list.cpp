#include <iostream>
using namespace std;

class Node {
    public:
        int data;
        Node *next;
};

void printlist(Node* a) {
    while(a != NULL) {
        cout << a->data << endl;
        a = a->next;
    }
}

int main()
{
    Node* head = NULL;
    Node* n1 = NULL;
    Node* n2 = NULL;
    Node* tail = NULL;
    head = new Node();
    n1 = new Node();
    n2 = new Node();
    tail = new Node();
    
    // "to access the member of the node class, we will use the arrow"
    head->data = 2;
    head->next = n1;
    n1->data = 3;
    n1->next = n2;
    n2->data = 5;
    n2->next = tail;
    tail->data = 7;
    tail->next = NULL;
    
    printlist(head);

    return 0;
}