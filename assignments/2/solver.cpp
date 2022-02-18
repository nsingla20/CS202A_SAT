#include <bits/stdc++.h>
#include "cnf_reader.h"
using namespace std;
void print_clau(const vector<int> &v){
    for(auto i:v){
        cout<<i<<" ";
    }
    cout<<endl;
}
void print_model(vector<int> mark){
    for(int i=1;i<mark.size();++i){
        if(mark[i]==0){
            cout<<-i<<" ";
        }else if (mark[i]==1){
            cout<<i<<" ";
        }else{
            cout<<"x"<<i<<" ";
        }
    }
    cout<<endl;
}
vector<int> single(int n,vector<vector<int>> &v,const vector<int> mark){
    vector<int> ans;
    // vector<vector<int>> removed;
    int num[n+1];
    for(int i=1;i<n+1;++i){
        num[i]=-1;
    }
    auto l=v.begin();
    while(l!=v.end()){
        int count=0,x;
        auto i=(*l).begin();
        while(i!=(*l).end()){
            if(mark[abs(*i)]==-1){
                count++;x=*i;
                i++;
            }else if(mark[abs(*i)]!=signbit(*i)){
                // removed.push_back(*l);
                // cout<<"Removed : ";
                // print_clau(*l);
                l=v.erase(l);
                l--;
                count=0;
                break;
            }else{
                i=(*l).erase(i);
            }
        }
        if(count>1){
            for(auto i:*l){
                if(mark[abs(i)]==-1){
                    if(num[abs(i)]==-1){
                        num[abs(i)]=!signbit(i);
                    }else if(num[abs(i)]==signbit(i)){
                        num[abs(i)]=-2;
                    }
                }
            }
        }
        if(count==1){
            // removed.push_back(*l);
            // cout<<"Removed : ";
            // print_clau(*l);
            l=v.erase(l);
            ans.push_back(x);
        }else{
            l++;
        }
    }
    for(int i=1;i<n+1;++i){
        if(num[i]>=0){
            ans.push_back(num[i]==0?-i:i);
        }
    }
    // sort(ans.begin(),ans.end());
    // ans.resize(distance(ans.begin(), unique(ans.begin(), ans.end())));
    return ans;
}
bool check(vector<vector<int>> &v, vector<int> mark){
    for(auto &l:v){
        // if(l.size()==0){
        //     continue;
        // }
        bool b=false;
        for(auto &i:l){
            if(mark[abs(i)]==-1){
                b=true;
                break;
            }else{
                b=(mark[abs(i)]!=signbit(i));
                if(b){
                    break;
                }
            }
        }
        if(!b){
            return false;
        }
    }
    return true;
}

bool correct(vector<vector<int>> &v, vector<int> mark){
    for(auto &l:v){
        // if(l.size()==0){
        //     continue;
        // }
        bool b=false;
        for(auto i:l){
            b=(mark[abs(i)]==!signbit(i));
            if(b){
                break;
            }
        }
        if(!b){
            // cout<<"Wrong : ";
            // print_clau(l);
            // cout<<"Current state : ";
            // print_model(mark);
            return false;
        }
    }
    return true;
}

void learn(vector<vector<int>> &v, vector<int> &guess){
    vector<int> temp;
    for(auto i:guess){
        temp.push_back(-i);
    }
    v.push_back(temp);
}

void unset(int x, vector<int> mark, vector<int> (&m)[]){
    for(auto i:m[x]){
        mark[i]=-1;
    }
    m[abs(x)].clear();
}
void add_clau(vector<vector<int>> &v,vector<vector<int>> &toadd){
    for(auto &i:toadd){
        v.push_back(i);
        cout<<"Added : ";
        print_clau(i);
    }
}

int decide(int n,vector<int> mark){
    for(int i=1;i<n+1;++i){
        if(mark[i]==-1){
            return i;
        }
    }
    return -1;
}

pair<bool,vector<int>> solve(int n, vector<vector<int>> v, vector<int> mark, vector<int> &guess, vector<int> (&m)[]){
    // vector<vector<int>> v_o=v;
    vector<int> singles=single(n,v,mark);
    while(singles.size()!=0){
        for(auto i:singles){
            // if(guess.size()>0){
            //     m[abs(guess.back())].push_back(abs(i));
            // }
            if(mark[abs(i)]!=-1){
                if(mark[abs(i)]==signbit(i)){
                    return {false,mark};
                }
            }else{
                mark[abs(i)]=!signbit(i);
            }
        }
        singles=single(n,v,mark);
    }
    if(correct(v,mark)){
        return {true,mark};
    }
    if(!check(v,mark)){
        // learn(v,guess);
        // unset(abs(guess.back()),mark,m);
        // add_clau(v,singles.second);
        return {false,mark};
    }
    
    int x=decide(n,mark);
    // guess.push_back(x);
    mark[x]=1;
    pair<bool,vector<int>> p=solve(n,v,mark,guess,m);
    if(p.first){
        // mark=p.second;
        return {true,p.second};
    }
    // guess.back()=-x;
    mark[x]=0;
    p=solve(n,v,mark,guess,m);
    if(p.first){
        return {true,p.second};
    }
    mark[x]=-1;
    // guess.pop_back();

    // learn(v,guess);
    // if(guess.size()>0){
    //     unset(abs(guess.back()),mark,m);
    // }
    // add_clau(v,singles.second);
    return {false,mark};

}

int main(){
    cout<<"INPUT CNF filename : ";
    string s;
    cin>>s;
    s="testcases/"+s;

    pair<int,vector<vector<int>>> p=extract(s);
    if(p.first==-1){
        cout<<"ERROR in opening the file";
        return 0;
    }

    vector<int> mark;
    for(int i=0;i<p.first+1;++i){
        mark.push_back(-1);
    }
    vector<int> m[p.first+1];
    
    time_t start,end;
    time(&start);
    pair<bool,vector<int>> b=solve(p.first,*(new vector<vector<int>>(p.second)),mark,*(new vector<int>()),m);
    mark=b.second;
    time(&end);
    if(correct(p.second,mark)){
        cout<<"Given clauses are SAT with following model : "<<endl;
        print_model(mark);
    }else{
        cout<<"Given clauses are UNSAT"<<endl;
    }
    
    cout<<"\nTime Taken : "<<(end-start)<<"s";
}
