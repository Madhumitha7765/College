#include<iostream>
using namespace std;

int Merge(int A[], int low, int mid, int high)
{
    int C[30];
    int index = low;
    int v = 0;
    int i = low;
    int j = (mid + 1);

    while(i<=mid && j<=high)
    {
        if(A[i]<=A[j])
        {
            C[index]=A[i];
            i++;
        }
        else
        {
            C[index]=A[j];
            j++;
            v+=(mid-i+1);
        }
        index++;
    }

    if(i>mid)
    {
        for(int p=j; p<=high; p++)
        {
            C[index]=A[p];
            index++;
        }
    }
    else
    {
        for(int q=j; q<=mid; q++)
        {
            C[index]=A[q];
            index++;
        }
    }

    for(int k=low; k<=high; k++)
    {
        A[k]=C[k];
    }
    return v;
}

int icount(int A[], int low, int high)
{
    int mid, c1, c2, c3;

    if(low<high)
    {
        mid = (low + high)/2;
        c1 = icount(A, low, mid);
        c2 = icount(A, mid+1, high);
        c3 = Merge(A, low, mid, high);
        return(c1+c2+c3);
    }
    else
    return 0;

}

int main()
{
    int A[40];
    int n, i;

    cout<<"\nEnter size of array : ";
    cin>>n;

    cout<<"\nEnter elements of array : "<<endl;
    for(i=0; i<n; i++)
    {
        cin>>A[i];
    }
    cout<<"\nNumber of inversions :  "<<icount(A, 0, n-1);
}
