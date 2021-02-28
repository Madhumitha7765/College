#include <iostream>

using namespace std;


int binarySearch(int arr[], int l, int h, int val)
{
    if (h>= l) {
        int mid = (l + h) / 2;

        if (arr[mid] == val)
            return mid;

        if (arr[mid] > val)
            return binarySearch(arr, l, mid - 1, val);

        return binarySearch(arr, mid + 1, h, val);
    }
    return -1;
}

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


 int Minimize(int arr[], int Size, int x)
 {
    int m = binarySearch(arr, 0, Size, x+1);
    if(m == -1)
        return x+1;
    while(m != -1)
        m = binarySearch(arr, 0, Size, ++x);
    return x;
 }

int main()
{
    int s,i,x;
    cout << "\nEnter the size of the Array: ";
    cin >> s;
    int A[s];

    cout << "\nEnter the values of the array" << endl;
    for(int i = 0; i < s; i++)
        cin >> A[i];


    cout << "\nEnter the value of X: " << endl;
    cin >> x;
    Merge_sort(A, 0, s-1);
    cout << "Minimized value of z is :" <<Minimize(A, s, x);
}
