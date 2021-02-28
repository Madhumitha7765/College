#include<bits/stdc++.h>
#include<cmath>

using namespace std;

int A[10000];

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

int maxSum(int arr[], int n, int k)
{
    // k must be greater
    if (n < k)
    {
       cout << "Invalid";
       return -1;
    }

    // Compute sum of first window of size k
    int res = 0;
    for (int i=0; i<k; i++)
       res += arr[i];

    // Compute sums of remaining windows by
    // removing first element of previous
    // window and adding last element of
    // current window.
    int curr_sum = res;
    for (int i=k; i<n; i++)
    {
       curr_sum += arr[i] - arr[i-k];
       res = max(res, curr_sum);
    }

    return res;
}

int minSum(int arr[], int n, int k)
{
    // k must be greater
    if (n < k)
    {
       cout << "Invalid";
       return -1;
    }

    // Compute sum of first window of size k
    int res = 0;
    for (int i=0; i<k; i++)
       res += arr[i];

    // Compute sums of remaining windows by
    // removing first element of previous
    // window and adding last element of
    // current window.
    int curr_sum = res;
    for (int i=k; i<n; i++)
    {
       curr_sum += arr[i] - arr[i-k];
       res = min(res, curr_sum);
    }

    return res;
}



int main()
{
	int n;
    cout << "Enter the size of array : " << endl;
	cin >> n;
	cout<<"\nEnter data : "<<endl;
	for(int i=0;i<n;i++)
		{
			cin >> A[i];
		}
    Merge_sort(A, 0, n-1);
/*        	for(int i=0;i<n;i++)
		{
			cout<<A[i]<<endl;
		}*/

    cout<<"\nEnter k value : ";
    int k;
    cin>>k;
    cout<<endl;
    cout<<"\nThe maximum sum is : ";
    cout << maxSum(A, n, k);

      cout<<"\nThe minimum sum is : ";
       cout << minSum(A, n, k);

    return 0;
}
