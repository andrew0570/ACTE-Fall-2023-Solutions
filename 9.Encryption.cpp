#include <bits/stdc++.h>

using namespace std;

int main(){
    int n;
    cin>>n;
    string s;
    cin.ignore();
    getline(cin, s);
    for(auto i:s){
        cout<<int(i)-n<<" ";
    }
    cout<<endl;
    return 0;
}