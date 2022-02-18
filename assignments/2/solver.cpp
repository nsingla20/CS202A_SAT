#include <bits/stdc++.h>
#include "cnf_reader.h"
using namespace std;

// vector<int> pure(int n,const vector<vector<int>> &v,const int mark[]){
//     vector<int> ans;
//     for(auto l:v){
//         int count=0,x;
//         for(auto i:l){
//             if(mark[abs(i)]==-1){
//                 count++;x=i;
//             }else if(mark[abs(i)]!=signbit(i)){
//                 count=0;
//                 break;
//             }
//         }
//         if(count==1){
//             ans.push_back(x);
//         }
//     }
//     return ans;
// }

vector<int> single(int n,const vector<vector<int>> &v,const int mark[]){
    vector<int> ans;
    int num[n+1];
    for(int i=1;i<n+1;++i){
        num[i]=-1;
    }
    for(auto l:v){
        int count=0,x;
        for(auto i:l){
            if(mark[abs(i)]==-1){
                count++;x=i;
            }else if(mark[abs(i)]!=signbit(i)){
                count=0;
                break;
            }
        }
        if(count>1){
            for(auto i:l){
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
            ans.push_back(x);
        }
    }
    for(int i=1;i<n+1;++i){
        if(num[i]>=0){
            ans.push_back(num[i]==0?-i:i);
        }
    }
    sort(ans.begin(),ans.end());
    ans.resize(distance(ans.begin(), unique(ans.begin(), ans.end())));
    return ans;
}
bool check(vector<vector<int>> &v, int mark[]){
    for(auto l:v){
        bool b=false;
        for(auto i:l){
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

bool correct(vector<vector<int>> &v, int mark[]){
    for(auto l:v){
        bool b=false;
        for(auto i:l){
            b=(mark[abs(i)]!=-1)&&(mark[abs(i)]!=signbit(i));
            if(b){
                break;
            }
        }
        if(!b){
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

void unset(int x, int mark[], vector<int> m[]){
    for(auto i:m[x]){
        mark[i]=-1;
    }
    m[x].clear();
}

int decide(int n,int mark[]){
    for(int i=1;i<n+1;++i){
        if(mark[i]==-1){
            return i;
        }
    }
    return -1;
}

bool solve(int n, vector<vector<int>> &v, int mark[], vector<int> &guess, vector<int> m[]){
    vector<int> singles=single(n,v,mark);
    while(singles.size()!=0){
        for(auto i:singles){
            if(guess.size()>0){
                m[abs(guess.back())].push_back(abs(i));
            }
            mark[abs(i)]=!signbit(i);
        }
        singles=single(n,v,mark);
    }
    if(correct(v,mark)){
        return true;
    }
    if(!check(v,mark)){
        learn(v,guess);
        unset(guess.back(),mark,m);
        // mark[guess.back()]=!mark[guess.back()];
        // return solve();
        return false;
    }
    int x=decide(n,mark);
    guess.push_back(x);
    mark[x]=1;
    if(solve(n,v,mark,guess,m)){
        return true;
    }
    guess.back()=-x;
    mark[x]=0;
    if(solve(n,v,mark,guess,m)){
        return true;
    }
    mark[x]=-1;
    guess.pop_back();

    learn(v,guess);
    if(guess.size()>0){
        unset(guess.back(),mark,m);
    }
    return false;

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

    int mark[p.first+1];
    for(int i=0;i<p.first+1;++i){
        mark[i]=-1;
    }
    vector<int> m[p.first+1];
    // for(int i=0;i<p.first+1;++i){
    //     m.push_back(*(new vector<int>()));
    // }
    time_t start,end;
    time(&start);
    if(solve(p.first,p.second,mark,*(new vector<int>()),m)){
        cout<<"Given clauses are SAT with following model : "<<endl;
        for(int i=1;i<p.first+1;++i){
            cout<<(mark[i]==0?-i:i)<<" ";
        }
    }else{
        cout<<"Given clauses are UNSAT"<<endl;
    }
    time(&end);
    cout<<"\nTime Taken : "<<(end-start)<<"s";
}
