#include <iostream>

using namespace std;

//unsigned int is used because number of times cannot be negative

unsigned int times_divisible_by_5(unsigned int n)
{
    return (n % 5 == 0) ? 1 + times_divisible_by_5(n / 5) : 0;
}

int min_num(int p, int sum, int val)
{
    if (sum >= val)
        return p - 1;
    else
    {
        sum += times_divisible_by_5(p);
        return min_num(p + 1, sum, val);
    }
}

int main()
{
    int val;
    cout << "\nEnter the value: ";
    cin >> val;
    cout << "\nMinimum number  is " <<min_num(1, 0, val)<<endl;
}
