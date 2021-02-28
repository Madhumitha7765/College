#include <iostream>
using namespace std;

void Merge(int arr[], int l, int m, int h)
{
    int n1 = m - l + 1;
    int n2 = h - m;

    // Create temp arrays
    int L[n1], R[n2];

    // Copy data to temp arrays L[] and R[]
    for(int i = 0; i < n1; i++)
        L[i] = arr[l + i];
    for(int j = 0; j < n2; j++)
        R[j] = arr[m + 1 + j];

    // Merge the temp arrays back into arr[l..r]

    // Initial index of first subarray
    int i = 0;

    // Initial index of second subarray
    int j = 0;

    // Initial index of merged subarray
    int k = l;

    while (i < n1 && j < n2)
    {
        if (L[i] <= R[j])
        {
            arr[k] = L[i];
            i++;
        }
        else
        {
            arr[k] = R[j];
            j++;
        }
        k++;
    }

    // Copy the remaining elements of L[], if there are any
    while (i < n1)
    {
        arr[k] = L[i];
        i++;
        k++;
    }

    // Copy the remaining elements of  R[], if there are any
    while (j < n2)
    {
        arr[k] = R[j];
        j++;
        k++;
    }
}


void Merge_sort(int arr[], int low, int high)
{
    if (low < high)
    {
        int mid = (low+high) / 2;

        // Sort first and second halves
        Merge_sort(arr, low, mid);
        Merge_sort(arr, mid+ 1, high);

        Merge(arr, low, mid, high);
    }

}

int main()
{
	int A[30],n,k,i,specialty=0;
	cout<<"\nEnter the size of Array : ";
	cin>>n;
	cout<<"\nEnter the Value of K : ";
	cin>>k;
    cout<<"\nEnter elements of the Array : "<< endl;
    for(i=0;i<n;i++)
	{
	    cin>>A[i];
    }
	Merge_sort(A,0,n-1);
    /* HERE CONTIGUOUS SUBARRAY IS INTERPRETED AS SUBARRAY WHOSE ELEMENTS SHARE COMMON BORDER*/

	for(i=0;i<n-k;i++)
	{
	    cout<<"\n"<<A[i];
    }
	for(i=0;i<n-k;i++)
	{
		specialty+=A[i];
	}
	cout<<"\nSpecialty of the sequence is : "<<specialty;
}
