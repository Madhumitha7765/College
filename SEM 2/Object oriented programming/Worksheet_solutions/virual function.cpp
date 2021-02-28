#include<iostream>
using namespace std;
class Animal
{
    int i;
    public:
    virtual void eat()
    {
        cout<<"Generic Food\n";
    }
};
class Cat:public Animal
{
    int j;
    public:
    void eat()
    {
        cout<<"I eat rat\n";
    }
};
int main()
{
    Animal *a=new Animal;
    Cat *c=new Cat;
    cout<<sizeof(Animal)<<endl<<sizeof(Cat)<<endl;
    a=c;
    a->eat();
    c->eat();
}
