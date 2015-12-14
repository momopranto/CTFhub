#include <iostream>
#include <cmath>
#include <string>
#include <vector>
using namespace std;

long double g(int x, vector<long double>& list) {
    if (x < list.size()) {
	return list[x];
    }
    long double n = pow((g(x-1,list) + g(x-2,list)),2);
    list.push_back(n);
    return n;
}

long double w(int x, vector<long double>& list) {
    if (x < list.size()) {
	return list[x];
    }
    double n = pow(w(x-1,list),2) + pow(w(x-2,list),2);
    list.push_back(n);
    return n;
}

int main() {
    vector<long double> glist = {0,1};
    vector<long double> wlist = {0,1};
    long double a = g(15,glist);
    long double b = w(15,wlist);
    long double c = a-b;
    cout << endl;
    cout << "g(10):" << a << endl;
    cout << "w(10):" << b << endl;
    cout << "f(10):" << c << endl;
    
    long double sum = 0;
    long double tmp = c;
    int digit;
    while (tmp > 0) {
	digit = fmod(tmp,10);
	sum += digit;
	tmp /= 10;
    }
    cout << endl<< "sum: " << sum << endl;
}
