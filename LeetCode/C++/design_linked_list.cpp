#include <iostream>

using namespace std;

class Node {
    public:
    int data;
    Node* next;
    Node(int data, Node* next) : data(data), next(next) {}
};

void push(Node*& head, int data) {
    head = new Node(data, head);
}

void append(Node*& head, int data) {
    if (head == nullptr) {
        push(head, data);
        return;
    }
    Node* temp = head;
    while (temp->next != nullptr) {
        temp = temp->next;
    }
    temp->next = new Node(data, nullptr);
}

void insert_at(Node*& head, int index, int data) {
    if (index < 0) {
        cout << "Index out of bounds" << endl; 
        return;
    }
    if (index == 0) {
        push(head, data);
        return;
    }
    Node* temp = head;
    for (int i = 0; i < index-1; i++) {
        temp = temp->next;
        if (temp->next == nullptr && i != index-2) {
            cout << "Index out of bounds" << endl;
            return;
        }
    }
    if (temp == nullptr) {
        cout << "Index out of bounds" << endl;
        return;
    }
    temp->next = new Node(data, temp->next);
}

void remove(Node*& head) {
    if (head == nullptr) return;
    Node* temp = head;
    head = head->next;
    delete temp;
}

void remove_at_end(Node*& head) {
    if (head == nullptr) return;
    if (head->next == nullptr){
        remove(head);
        return;
    }
    Node* temp = head;
    while (temp->next->next != nullptr) {
        temp = temp->next;
    }
    temp->next = nullptr;
}

void remove_at(Node*& head, int index) {
    if (index < 0) {
        cout << "Index out of bounds" << endl; 
        return;
    }
    if (index == 0) {
        remove(head);
        return;
    }
    Node* temp = head;
    for (int i = 0; i < index-1; i++) {
        temp = temp->next;
        if (temp->next == nullptr) {
            cout << "Index out of bounds" << endl;
            return;
        }
    }
    if (temp->next == nullptr) {
        cout << "Index out of bounds" << endl;
        return;
    }
    temp->next = temp->next->next;
}

int get(Node*& head, int index) {
    if (index < 0 || head == nullptr) return -1;
    Node* temp = head;
    while (index > 0) {
        temp = temp->next;
        if (temp == nullptr) return -1;
        index--;
    }
    return temp->data;
}

void print(Node* head) {
    for (Node* temp = head; temp != nullptr; temp = temp->next) {
        cout << temp->data << "-->";
    }
    cout << endl;
}

int main() {
    Node* head = nullptr;
    insert_at(head, 1, 0);
    cout << get(head, 0) << endl;

    return 0;
}