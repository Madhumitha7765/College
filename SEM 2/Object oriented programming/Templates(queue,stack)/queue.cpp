#include<iostream>
#include<stdlib.h>
using namespace std;

void displaymenu();

template <class T>
class Queue
{
    int front;
    int rear;
    int size;
    T *queue;

public:
    Queue();
    Queue(int);
    void enqueue(T);
    T dequeue();
    void display();
    void count();
    ~Queue();
};

template <class T>
Queue<T>::Queue()
{
    front = rear = -1;
    queue = new T[4]();
}

template <class T>
Queue<T>::~Queue()
{
    delete[] queue;
}

template <class T>
Queue<T>::Queue(int size)
{
    front = rear = -1;
    this->size = size;
    queue = new T[size]();
}

template <class T>
void Queue<T>::enqueue(T element)
{
    if (rear == size - 1)
    {
        cout << "Queue full\n";
        return;
    }
    else if (rear == -1)
        front = 0;
    rear++;
    queue[rear] = element;
}

template <class T>
T Queue<T>::dequeue()
{
    T element;
    if (rear == -1)
    {
        cout << "Queue is empty\n";
        return 0;
    }
    element = queue[front];
    if (front == rear)
        front = rear = -1;
    else
        front++;
    return element;
}

template <class T>
void Queue<T>::display()
{
    if (rear == -1)
    {
        cout << "Queue is empty\n";
        return;
    }
    Queue<T> Q1(size);
    T element;
    int front1 = front;
    int rear1 = rear;
    cout << "Queue elements : \n";
    while (front != -1)
    {
        element = dequeue();
	cout << element << " ";
        Q1.enqueue(element);
    }
    cout<<"\n";
    for (int i = front1; i <= rear1; i++)
    {
        element = Q1.dequeue();
        enqueue(element);
    }
 }


template <class T>
void Queue<T>::count()
{
    if (rear == -1)
        {
		cout<<"\nQueue empty\n";
    		return;
	}
	cout<<"\nNumber of elements in the Queue :  "<<rear-front+1<<endl;
}

int main()
{
    int choice, size;
    char ch;
    do
    {
                        cout << "Enter the datatype of queue elements : \n";
                        cout << "1. Integer\n";
                        cout << "2. Decimal\n";
                        cout << "3. Character\n";
                        cout << "4. String\n";
                        cout << "5. Exit\n";
                        cout << "Choice : ";
                        cin >> choice;
                        if(choice==5)
                            exit(0);
                        cout << "Enter size of the Queue: ";
                        cin >> size;
                        switch(choice)
                        {
                        case 1 :
                                {
                                        Queue<int> S(size);
                                        int element;
                                        do{
                                                displaymenu();
                                                cin >> choice;
                                                switch(choice)
                                                {
                                                    case 1: cout << "Enter element to insert: ";
                                                            cin.sync();
                                                            cin >> element;
                                                            S.enqueue(element);
                                                            break;
                                                    case 2: cout<<"\nThe deleted element is : "<<S.dequeue()<<endl;
                                                            break;
                                                    case 3: S.display();
                                                            break;
                                                    case 4: S.count();
                                                            break;
                                                }
                                                cout << "Do you want to continue?(y/n): ";
                                                cin >> ch;
                                            }while(ch == 'y' || ch == 'Y');
                                            break;
                                }
                         case 2 :
                                {
                                                Queue<float> S(size);
                                                float element;
                                                do{
                                                    displaymenu();
                                                    cin >> choice;
                                                    switch(choice)
                                                    {
                                                        case 1: cout << "Enter element to insert: ";
                                                                cin.sync();
                                                                cin >> element;
                                                                S.enqueue(element);
                                                                break;
                                                        case 2: cout<<"\nThe deleted element is : "<<S.dequeue()<<endl;
                                                                break;
                                                        case 3: S.display();
                                                                break;
                                                        case 4: S.count();
                                                                break;
                                                    }
                                                    cout << "Do you want to continue?(y/n): ";
                                                    cin >> ch;
                                                }while(ch == 'y' || ch == 'Y');
                                                break;
                                }
                        case 3 :
                                {
                                                Queue<char> S(size);
                                                char element;
                                                int ch1;
                                                do{
                                                    displaymenu();
                                                    cin >> choice;
                                                    switch(choice)
                                                    {
                                                        case 1: cout << "Enter element to insert: ";
                                                                cin.sync();
                                                                cin >> element;
                                                                S.enqueue(element);
                                                                break;
                                                        case 2: cout<<"\nThe deleted element is : "<<S.dequeue()<<endl;
                                                                break;
                                                        case 3: S.display();
                                                                break;
                                                        case 4: S.count();
                                                                break;
                                                    }
                                                    cout << "Do you want to continue?(y/n): ";
                                                    cin >> ch;
                                                }while(ch == 'y' || ch == 'Y');
                                                break;
                                }
                        case 4 :
                                {
                                            Queue<string> S(size);
                                            string element;
                                            do{
                                                displaymenu();
                                                cin >> choice;
                                                switch(choice)
                                                {
                                                    case 1: cout << "Enter element to insert : ";
                                                            cin.sync();
                                                            cin >> element;
                                                            S.enqueue(element);
                                                            break;
                                                    case 2: cout<<"\nThe deleted element is : "<<S.dequeue()<<endl;
                                                            break;
                                                    case 3: S.display();
                                                            break;
                                                    case 4: S.count();
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
            cout << "1. Enqueue\n";
            cout << "2. Dequeue\n";
            cout << "3. Display queue \n";
            cout << "4. Display number of elements in the queue\n";
            cout << "Choice ::  ";
}
