#include <iostream>
using namespace std;

int check_gcd(int x, int y){
    if(x == y)
        return x;

    else if(x > y)
        return check_gcd(x-y , y);

    else
        return check_gcd(x , y-x);
}

int main()
{
    int n;
    cout<<"\nEnter the value of N : ";
    cin >> n;
    int a = n-2;

    while(check_gcd(a,n) != 1)
        a = a - 1;

    cout <<"\nThe largest co-prime less than n-1 is : "<<a<<endl;
}















/* C++ implementation of the above approacdh
#include <bits/stdc++.h>
#define ll long long int
using namespace std;

// Function to calculate gcd of two number
ll gcd(ll a, ll b)
{
    if (b == 0)
        return a;
    else
        return gcd(b, a % b);
}

// Function to check if two numbers are coprime or not
bool coPrime(ll n1, ll n2)
{
    // two numbers are coprime if their gcd is 1
    if (gcd(n1, n2) == 1)
        return true;
    else
        return false;
}

// Function to find largest integer less
// than or equal to N/2 and coprime with N
ll largestCoprime(ll N)
{
    ll half = floor(N / 2);

    // Check one by one all numbers
    // less than or equal to N/2
    while (coPrime(N, half) == false)
        half--;

    return half;
}

// Driver code
int main()
{

    int n;
    cin>>n;
    cout << largestCoprime(n);

    return 0;
}*/
