#include <iostream>
using namespace std;

class Node{

    int data;
    Node* leftChild;
    Node* rightChild;
public:
    Node(int);
    friend class Tree;
};

Node:: Node(int value){
    data = value;
    leftChild = NULL;
    rightChild = NULL;
}

class Tree{

public:
    Node* root;
    Tree() { root = NULL; }
    void insert(Node*&,int);
    bool getElement(Node*&,int);
};

void Tree:: insert(Node*& node, int value){

    if(node == NULL){
        node = new Node(value);
        return;
    }

    else if(value < node->data){
        insert(node->leftChild, value);
    }
    else{
        insert(node->rightChild,value);
    }
}

bool Tree::getElement(Node*& node,int value){

    if(node->data == value)
        return true;
    if(node->rightChild == NULL && node->leftChild == NULL)
        return false;
    if (value < node->data)
        return getElement(node->leftChild,value);
    if (value > node->data)
        return getElement(node->rightChild,value);

    return false;

}

int main(){

    Tree tree;
    int N;
    cout << "Enter the number of students in the class  :  ";
    cin >> N;
    cout << "\nEnter the number of students yet to come  : ";
    int M;
    cin >> M;

    int i = 1;
    int value;
    do{
        cout << "\nEnter the number of candies " << i++ << " st/nd/th student have " << endl;
        cin >> value;
        tree.insert(tree.root,value);
    }while(i <= N);

    i = 0;

    while(++i <= M){
        cout << "\nEnter the number of candies the student going to enter has  :  ";
        cin >> value;
        if(tree.getElement(tree.root,value)){
            cout << "YES" << endl;
        }
        else{
            cout << "NO" << endl;
        }
    }

    return 0;
}
