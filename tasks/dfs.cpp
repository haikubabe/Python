/*
Sourav Goswami
Handle: gosour
*/

#include<iostream>
#include<sstream>
#include<stdio.h>
#include<vector>
#include<string>
#include<string.h>
#include<queue>
#include<stack>
#include<iomanip>
#include<cmath>
#include<list>
#include<set>
#include<map>
#include<algorithm>
#include<limits>

using namespace std;

#define pb push_back
#define rep(i,m) for(int i=0;i<(int)(m);i++)
#define rep2(i,n,m) for(int i=n;i<(int)(m);i++)
#define mem(a,b) memset(a,b,sizeof(a))
#define mp make_pair
#define ss stringstream
#define iss istringstream
#define ii pair<int,int>
#define vii vector<ii>

const int MAX_INT = numeric_limits<int>::max(); //2147483647 (>pow(10,9))
//It takes MAX_INT/6>pow(10,8) calculations a little less than 1 sec
const int MIN_INT = numeric_limits<int>::min(); //-2147483648
const int MAX_FLOAT = numeric_limits<float>::min(); 

enum class dir_t {left,right,up,down};

class Board{
	public:
	int values[9];
	int goal[9] = {1,2,3,8,0,4,7,6,5};
	Board();
	Board(int in[]);
	bool operator==(const Board &b){
		bool f = true;
		rep(i,9){
			if(this->values[i] != b.values[i])
				f = false;
			
		}
		return f;
	}
	bool isfinal();
	void print();
	vector<dir_t> action();	
	void takeaction(dir_t D);
};

Board::Board(){
	rep(i,9)
		values[i] = i;
}
Board::Board(int in[]){
	rep(i,9)
		values[i] = in[i];
}

bool Board::isfinal(){
	bool f = true;
	rep(i,9){
		if(values[i] != goal[i])
			f = false;
	}
	return f;
}

void Board::print(){
	cout<<values[0]<<" "<<values[1]<<" "<<values[2]<<endl;
	cout<<values[3]<<" "<<values[4]<<" "<<values[5]<<endl;
	cout<<values[6]<<" "<<values[7]<<" "<<values[8]<<endl;
}

vector<dir_t> Board::action(){
	int index;
	vector<dir_t> results;
	rep(i,9){
		if(values[i] == 0){
			index = i; break;
		}
	}
	if(index % 3 != 0)
	   results.pb(dir_t::left);
	if(index % 3 != 2)
		results.pb(dir_t::right);
	if(index > 2)
		results.pb(dir_t::up);
	if(index < 6)
		results.pb(dir_t::down);

	return results;
}

void Board::takeaction(dir_t D){
	int index,tmp;
	rep(i,9){
		if(values[i] == 0){
			index = i; break;
		}
	}
	if(D == dir_t::left){
		tmp = values[index-1];
		values[index-1] = values[index];
		values[index] = tmp;
	}
	else if(D == dir_t::right){
		tmp = values[index+1];
		values[index+1] = values[index];
		values[index] = tmp;
	}
	else if(D == dir_t::up){
		tmp = values[index-3];
		values[index-3] = values[index];
		values[index] = tmp;
	}
	else if(D == dir_t::down){
		tmp = values[index+3];
		values[index+3] = values[index];
		values[index] = tmp;
	}

}

struct node{
	struct node * prev;
	int d;
	Board b;
};

typedef struct node *N;

N bfs(Board s){
	queue<N> q;
	N start = new struct node;
	start->prev = NULL;
	start->d = 0;
	start->b = s;

	q.push(start);
	int count = 0;
	vector<Board> uniq;
	uniq.pb(s);
	
	while(!q.empty()){
		N temp = q.front();
		if(temp->b.isfinal()){
			return temp;
		}
		vector<dir_t> actions = temp->b.action();
		rep(i,actions.size()){
			Board new_temp = temp->b;
			new_temp.takeaction(actions[i]);
			if(find(uniq.begin(),uniq.end(),new_temp) == uniq.end()){
				uniq.pb(new_temp);
				N n = new struct node;
				n->prev = temp;
				n->b = new_temp;
				n->d = temp->d+1;
				q.push(n);
			}
		}
		q.pop();
		count++;
	}
}

N dfs(Board s){
	stack<N> q;
	N start = new struct node;
	start->prev = NULL;
	start->d = 0;
	start->b = s;

	q.push(start);
	int count = 0;
	vector<Board> uniq;
	uniq.pb(s);
	
	while(!q.empty()){
		N temp = q.top();
		q.pop();
		if(temp->b.isfinal()){
			return temp;
		}
		vector<dir_t> actions = temp->b.action();
		rep(i,actions.size()){
			Board new_temp = temp->b;
			new_temp.takeaction(actions[i]);
			if(find(uniq.begin(),uniq.end(),new_temp) == uniq.end()){
				uniq.pb(new_temp);
				N n = new struct node;
				n->prev = temp;
				n->b = new_temp;
				n->d = temp->d+1;
				q.push(n);
			}
		}
		count++;
	}
}

void printpath(N n){
	if (n->d == 0){
		n->b.print();
		cout<<endl;
	}
	else{
		printpath(n->prev);
		n->b.print();
		cout<<endl;
	}
}
		
int main(){
	
	int input[] = {2,0,3,1,8,4,7,6,5};
	Board newboard(input);
	N bfsans = bfs(newboard);
	N dfsans = dfs(newboard);
	cout<<"BFS: "<<endl;
	printpath(bfsans);
	cout<<"DFS: "<<endl;
	printpath(dfsans);
	
	return 0;

}

