#include<iostream>
#include<string>
using namespace std;

void swap(int *a, int *b) {
  int t = *a;
  *a = *b;
  *b = t;
}
int partition(int array[], int low, int high, int ind[]) {
  int pivot = array[high];
  int i = (low - 1);
  for (int j = low; j < high; j++) {
    if (array[j] <= pivot) {
      i++;
      swap(&array[i], &array[j]);
      swap(&ind[i], &ind[j]);
    }
  }
  swap(&array[i + 1], &array[high]);
  swap(&ind[i+1], &ind[high]);
  return (i + 1);
}
void quickSort(int array[], int low, int high, int ind[]) {
  if (low < high) {
    int pi = partition(array, low, high, ind);
    quickSort(array, low, pi - 1, ind);
    quickSort(array, pi + 1, high, ind);
  }
}

int getSum(int n)
{
    int sum=10;
    while(sum>9){
        sum=0;
        while (n != 0)
        {
            sum = sum + n % 10;
            n = n/10;
        }
        n=sum;
    }
    return sum;
 }

int main(){
    int n,m;
    cout<<"Enter n: ";
    cin>>n;
    int a[n],b[n],ind[n];
    cout<<"Enter the array: ";
    for(int i=0;i<n;i++){
        cin>>a[i];
        b[i]=getSum(a[i]);
        ind[i]=i;
    }

    quickSort(b,0,n-1,ind);
    int k,ch;

    while(1){
        cout<<"Enter k: ";
        cin>>k;
        cout<<"Enter 1 for min k, Enter 2 for max k, Enter 3 to exit:  ";
        cin>>ch;
        if(ch==1){
            for(int i=0;i<k;i++){
                cout<<a[ind[i]]<<" ";
            }
            cout<<endl;
        }

        else if(ch==2){
            int j=0;
            for(int i=n-1;j<k;i--){
                cout<<a[ind[i]]<<" ";
                j+=1;
            }
            cout<<endl;
        }
        else if (ch==3){
            cout<<"Thank you! "<<endl;
            break;
        }

        else{
            cout<<"Choose properly"<<endl<<endl;
        }
    }

}
