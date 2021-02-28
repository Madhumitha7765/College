// C++ program to find minimum sum of two numbers
// formed from digits of the array.
#include <bits/stdc++.h>
using namespace std;


void Merge(int arr[], int l, int m, int h)
{
    int n1 = m - l + 1;
    int n2 = h - m;
    int L[n1], R[n2];

    for(int i = 0; i < n1; i++)
        L[i] = arr[l + i];
    for(int j = 0; j < n2; j++)
        R[j] = arr[m + 1 + j];

    int i = 0;
    int j = 0;
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

    while (i < n1)
    {
        arr[k] = L[i];
        i++;
        k++;
    }
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
        int mid = (low + high )/ 2;

        Merge_sort(arr, low, mid);
        Merge_sort(arr, mid + 1, low);
        Merge(arr, low, mid, high);
    }
}


// Function to find and return minimum sum of
// two numbers formed from digits of the array.
int solve(int arr[], int n)
{

     // sort the array
    Merge_sort(arr, 0, n);
    // let two numbers be a and b
    int a = 0, b = 0;
    for (int i = 0; i < n; i++)
    {
        // fill a and b with every alternate digit
        // of input array
        if (i & 1)
            a = a*10 + arr[i];
        else
            b = b*10 + arr[i];
    }

    // return the sum
    return a + b;
}

// Driver code
int main()
{
    int A[100];
    int n;
    cout << "Enter the size of array : " << endl;
	cin >> n;
	cout<<"\nEnter data : "<<endl;
	for(int i=0;i<n;i++)
		{
			cin >> A[i];
		}
    Merge_sort(A, 0, n-1);

    cout << "Sum is " << solve(A, n);
    return 0;
}
