//finding maximum value of binary digits
#include<iostream>
using namespace std;
int main()
{
    int n,m,i;
    cout<<"\n enter no. of rows:";
    cin>>n;
    cout<<"\n enter no. of columns:";
    cin>>m;
    cout<<"\n enter the binary digits:\n";
    string s1[n],s2[n];
    for(int i=0;i<n;i++)
    {
        cin>>s1[i];
        s2[i] = s1[i];
    }
    int j;
    string temp;
    //sorting using selection sort
    for(i=0;i<n-1;i++)
        for(j=i+1;j<n;j++)
            if(s1[i]>s1[j])
            {
                temp=s1[i];
                s1[i]=s1[j];
                s1[j]=temp;
            }
    cout<<"\n Minimum index of row with maximum value:";
    for(i=0;i<n;i++)
        if(s2[i]==s1[n-1])
            break;
    cout<<i+1;

}
