#include <bits/stdc++.h>

using namespace std;

class order{
    public:
        int num;
        int date;
        string color;
        char size;
        int amnt;
        order(int n, int d, string c, char s, int a){num=n;date=d;color=c;size=s;amnt=a;}
};
class cnt{
    public: 
        string color;
        char size;
        int amnt;
        cnt(string c, char s,int a){color=c;size=s;amnt=a;}
};

bool sortDate(order a, order b){return a.date<b.date;}
bool sortColor(order a, order b){return a.color<b.color;}
bool sortNum(order a, order b){return a.num<b.num;}
bool sortSize(order a, order b){
    if(b.size=='X') return true;
    else if(a.size=='X') return false;
    else return a.size>b.size;
}
bool cmpSize(cnt a, cnt b){
    if(b.size=='X') return true;
    else if(a.size=='X') return false;
    else return a.size>b.size;
}
bool cmpColor(cnt a, cnt b){return a.color<b.color;}

int main(){
    vector<order> v;
    int n;
    cin>>n;
    for(int i=0;i<n;i++){
        int n, d, a;
        string c;
        char s;
        cin>>n>>d>>c>>s>>a;
        v.push_back(order(n, d, c, s, a));}
    sort(v.begin(),v.end(),sortSize);
    sort(v.begin(),v.end(),sortColor);
    stable_sort(v.begin(), v.end(), sortNum);
    stable_sort(v.begin(), v.end(), sortDate);
    for(auto i:v){cout<<i.num<<" "<<i.date<<" "<<i.color<<" "<<i.size<<" "<<i.amnt<<endl;}
    vector<cnt> out;
    for(auto i:v){
        if(find_if(out.begin(),out.end(),[=](cnt a){return a.color==i.color && a.size==i.size;})!=out.end()){out[find_if(out.begin(),out.end(),[=](cnt a){return a.color==i.color && a.size==i.size;})-out.begin()].amnt+=i.amnt;}   
        else{out.push_back(cnt(i.color, i.size, i.amnt));}}
    sort(out.begin(),out.end(), cmpSize);
    stable_sort(out.begin(),out.end(), cmpColor);
    for(auto i:out){
        cout<<i.color<<" "<<i.size<<" "<<i.amnt<<endl;
    }
    return 0;
}