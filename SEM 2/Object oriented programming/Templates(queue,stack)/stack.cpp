#include<iostream>
#include<stdlib.h>
using namespace std;

void displaymenu();

template <class T>
class Stack
{
    int top;
    int size;
    T *stack;

public:
    Stack();
    Stack(int);
    void push(T);
    T pop();
    void display_bottom();
    void display_top();
    void count();
    ~Stack();
};

template <class T>
Stack<T>::Stack()
{
    top = -1;
    stack = new T[4]();
}

template <class T>
Stack<T>::~Stack()
{
    delete[] stack;
}

template <class T>
Stack<T>::Stack(int size)
{
    top = -1;
    this->size = size;
    stack = new T[size]();
}

template <class T>
void Stack<T>::push(T element)
{
    if (top == size - 1)
    {
        cout << "Stack full\n";
        return;
    }
    top++;
    stack[top] = element;
}

template <class T>
T Stack<T>::pop()
{
    T element;
    if (top == -1)
    {
        cout << "Stack is empty\n";
        return 0;
    }
    element = stack[top];
    top--;
    return element;
}

template <class T>
void Stack<T>::display_bottom()
{
    if (top == -1)
    {
        cout << "Stack is empty\n";
        return;
    }
    Stack<T> S1(size);
    T element;
    int top1 = top;
    while (top != -1)
    {
        element = pop();
        S1.push(element);
    }

    cout << "Stack elements from bottom : \n";

    for (int i = 0; i <= top1; i++)
    {
        element = S1.pop();
        cout << element << "\t";
        push(element);
    }
    cout << endl;
}

template <class T>
void Stack<T>::display_top()
{
    if (top == -1)
    {
        cout << "Stack is empty\n";
        return;
    }
    Stack<T> S1(size);
    T element;
    int top1 = top;
    cout << "Stack elements from top:\n";
    while (top != -1)
    {
        element = pop();
        cout << element << "\t";
        S1.push(element);
    }
    cout << endl;
    for (int i = 0; i <= top1; i++)
    {
        element = S1.pop();
        push(element);
    }
}

template <class T>
void Stack<T>::count()
{
    if (top == -1)
        cout<<"\nStack empty\n";
    cout<<"\nNumber of elements in the Stack :  "<<top+1<<endl;
}

int main()
{
    int choice, size;
    char ch;
    do
    {
                        cout << "Enter the datatype of stack elements : \n";
                        cout << "1. Integer\n";
                        cout << "2. Decimal\n";
                        cout << "3. Character\n";
                        cout << "4. String\n";
                        cout << "5. Exit\n";
                        cout << "Choice : ";
                        cin >> choice;
                        if(choice==5)
                            exit(0);
                        cout << "Enter size of the stack: ";
                        cin >> size;
                        switch(choice)
                        {
                        case 1 :
                                {
                                        Stack<int> S(size);
                                        int element;
                                        do{
                                                displaymenu();
                                                cin >> choice;
                                                switch(choice)
                                                {
                                                    case 1: cout << "Enter element to insert: ";
                                                            cin.sync();
                                                            cin >> element;
                                                            S.push(element);
                                                            break;
                                                    case 2: cout<<"\nThe deleted element is : "<<S.pop()<<endl;
                                                            break;
                                                    case 3: S.display_top();
                                                            break;
                                                    case 4: S.display_bottom();
                                                            break;
                                                    case 5: S.count();
                                                            break;
                                                }
                                                cout << "Do you want to continue?(y/n): ";
                                                cin >> ch;
                                            }while(ch == 'y' || ch == 'Y');
                                            break;
                                }
                         case 2 :
                                {
                                                Stack<float> S(size);
                                                float element;
                                                do{
                                                    displaymenu();
                                                    cin >> choice;
                                                    switch(choice)
                                                    {
                                                        case 1: cout << "Enter element to insert: ";
                                                                cin.sync();
                                                                cin >> element;
                                                                S.push(element);
                                                                break;
                                                        case 2: cout<<"\nThe deleted element is : "<<S.pop()<<endl;
                                                                break;
                                                        case 3: S.display_top();
                                                                break;
                                                        case 4: S.display_bottom();
                                                                break;
                                                        case 5: S.count();
                                                                break;
                                                    }
                                                    cout << "Do you want to continue?(y/n): ";
                                                    cin >> ch;
                                                }while(ch == 'y' || ch == 'Y');
                                                break;
                                }
                        case 3 :
                                {
                                                Stack<char> S(size);
                                                char element;
                                                do{
                                                    displaymenu();
                                                    cin >> choice;
                                                    switch(choice)
                                                    {
                                                        case 1: cout << "Enter element to insert: ";
                                                                cin.sync();
                                                                cin >> element;
                                                                S.push(element);
                                                                break;
                                                        case 2: cout<<"\nThe deleted element is : "<<S.pop()<<endl;
                                                                break;
                                                        case 3: S.display_top();
                                                                break;
                                                        case 4: S.display_bottom();
                                                                break;
                                                        case 5: S.count();
                                                                break;
                                                    }
                                                    cout << "Do you want to continue?(y/n): ";
                                                    cin >> ch;
                                                }while(ch == 'y' || ch == 'Y');
                                                break;
                                }
                        case 4 :
                                {
                                            Stack<string> S(size);
                                            string element;
                                            do{
                                                displaymenu();
                                                cin >> choice;
                                                switch(choice)
                                                {
                                                    case 1: cout << "Enter element to insert : ";
                                                            cin.sync();
                                                            cin >> element;
                                                            S.push(element);
                                                            break;
                                                    case 2: cout<<"\nThe deleted element is : "<<S.pop()<<endl;
                                                            break;
                                                    case 3: S.display_top();
                                                            break;
                                                    case 4: S.display_bottom();
                                                            break;
                                                    case 5: S.count();
                                                            break;
                                                }
                                                cout << "Do you want to continue?(y/n): ";
                                                cin >> ch;
                                            }while(ch == 'y' || ch == 'Y');
                                            break;
                                }
                        default :
                                {
                                            cout << "Invalid input\n";
                                            exit(0);
                                }
                        }
    }while(choice!=5);
}

void displaymenu()
{
            cout << "Choose the operation to perform :\n";
            cout << "1. Push\n";
            cout << "2. Pop\n";
            cout << "3. Display stack from top\n";
            cout << "4. Display stack from bottom\n";
            cout << "5. Display number of elements in the stack\n";
            cout << "Choice ::  ";
}
