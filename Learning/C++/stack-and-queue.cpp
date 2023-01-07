#include <iostream>
using namespace std;

// Array implementation of an integer stack
const int MAX = 1000; // Arbitrary max size of stack

class Stack {
public:
    int top;
    int a[MAX];
    Stack() : top(-1) {}

    void push(int x) {
        if (top >= MAX-1) cout << "Stack overflow" << endl;
        else {
            top++;
            a[top] = x;
        }   
    }
    int pop() {
        if (top < 0) {
            cout << "Stack underflow" << endl;
            return 0;
        }
        else {
            top--;
            return a[top];
        }
    }
    int peek() {
        if (top == -1) {
            cout << "Stack is empty" << endl;
            return 0;
        }
        else return a[top];
    }
    bool empty() {
        return (top < 0);
    }
    void print() {
        if (top == -1) cout << "Stack is empty" << endl;
        for(int i = 0; i < top+1; i++) {
            cout << a[i] << " ";
        } cout << endl;
    }
};

// Linked list implementation of an integer queue
class Node {
public:
    int val;
    Node* next;
    Node(int val, Node* next) : val(val), next(next) {}
};

class Queue {
public:
    Node* front;
    Node* back;
    Queue() {
        front = nullptr;
        back = nullptr;
    }

    void enqueue(int x) {
        Node* temp = new Node(x, nullptr);
        if (front == nullptr && back == nullptr) {
            front = back = temp;
        }
        else {
            back->next = temp;
            back = temp;
        }
    }
    void dequeue() {
        if (front == nullptr) {
            cout << "Queue is empty" << endl;
        }
        else {
            Node* temp = front;
            front = front->next;
            if (front == nullptr) back = nullptr;
            delete temp;
        }
    }
    int peek() {
        if (front == nullptr) {
            cout << "Queue is empty" << endl;
            return 0;
        }
        else return front->val;
    }
    bool empty() {
        return (front == nullptr && back == nullptr);
    }
    void print() {
        Node* itr = front;
        while (itr != nullptr) {
            cout << itr->val << " ";
            itr = itr->next;
        } cout << endl;
    }
};

int main() {
    // Testing Stack
    Stack s;
    s.push(1);
    s.push(3);
    s.push(2);
    cout << s.peek() << endl;
    s.pop();
    s.print();
    cout << s.empty() << endl;
    s.pop();
    s.pop();
    cout << s.empty() << endl;

    // Testing Queue
    Queue q;
    q.enqueue(1);
    q.enqueue(3);
    q.enqueue(2);
    cout << q.peek() << endl;
    q.dequeue();
    q.print();
    cout << q.empty() << endl;
    q.dequeue();
    q.dequeue();
    cout << q.empty() << endl;

    return 0;
}