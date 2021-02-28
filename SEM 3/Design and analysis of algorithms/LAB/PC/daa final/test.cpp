#include<bits/stdc++.h>
using namespace std;
int main()
{
    int n,k;
    cin>>n>>k;
    int cnt[10]={0};
    while(n>0)
    {
    	int x=n%10;
    	//cout<<x<<endl;
    	n/=10;
    	cnt[x]+=1;
    }
    int mi=0;
    int kk=k;
    for(int i=1;i<10;i++)
    {
    	if(k)
    	{
    		int now=min(k,cnt[i]);
    		mi+=(now*i);
    		k-=now;
    	}
    	else
    		break;
    }
    int mx=0;
	for(int i=9;i>=1;i--)
    {

    	int now=min(kk,cnt[i]);
    	mx+=(now*i);
    	kk-=now;
    }
    cout<<mi<<" "<<mx<<endl;


    return 0;
}
