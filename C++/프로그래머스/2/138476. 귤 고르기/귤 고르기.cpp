#include <bits/stdc++.h>

using namespace std;

int solution(int k, vector<int> tangerine) {
    int answer = 0;
    vector<int> count(10000001);
    for (int i = 0; i < tangerine.size(); i++){
        count[tangerine[i]]++;
    }
    sort(count.begin(), count.end(), greater<int>());
    for (int i = 0; i < count.size(); i++){
        k -= count[i];
        answer++;
        if(k <= 0)
            break;
    }
    return answer;
}