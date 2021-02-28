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

long double f(long long int x1, long long int y1, long long int x2, long long int y2)
{
 return sqrtl(powl(x1-x2,2) + powl(y1-y2,2));
}



int main()
{
	int n,k,t;
    cout << "Enter the total number of test cases " << endl;
	cin >> t;
	while(t--)
	{
        cout << "\nEnter the values of N and K " << endl;
		cin >> n >> k;


		cout<<"\nEnter data : "<<endl;
		for(int i=0;i<n;i++)
		{
			cin >> A[i];
		}
		Merge_sort(A, 0, n-1);
		long double sum = 0.0;

          sum+=f(A[0],A[1],A[0],A[n-1]);
          sum+=f(A[0],A[n-1],A[n-2],A[n-1]);
          sum+=f(A[n-2],A[n-1],A[n-1],A[n-2]);
          sum+=f(A[n-1],A[n-2],A[n-1],A[0]);
          sum+=f(A[n-1],A[0],A[1],A[0]);
          sum+=f(A[1],A[0],A[0],A[1]);

        long  long int  rounded=ceil(sum);
        cout << "\nThe minimum cost is " << endl;
        cout << rounded * k << endl;
	}


    return 0;
}
