#include <iostream>
#include <cmath>
#include <string>
using namespace std;

double g(double x) {
    cout << "g(" << x << ") ";
    if (x==0) {return 0;}
    else if (x==1) {return 1;}
    return pow((g(x-1) + g(x-2)),2);
}

double w(double x) {
    cout << "w(" << x << ") ";
    if (x==0) {return 0;}
    else if (x==1) {return 1;}
    return pow(w(x-1),2) + pow(w(x-2),2);
}

double f(double x) {
    return g(x)-w(x);
}

int main() {
    //int x = f(30);
    double a = g(30);
    double b = w(30);
    cout << endl;
    cout << "g(30):" << a << endl;
    cout << "w(30):" << b << endl;
    double x = a-b;
    cout << "f(30):" << x << endl;
    string s = to_string(x);
    int sum = 0;
    int tmp;
    for (size_t i=0; i < s.length(); ++i) {
	s[i] >> tmp;
	sum += tmp;
    }
    cout << sum << endl;;
}
