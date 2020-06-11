#include <iostream>
#include <string>

using namespace std;

int main()
{

    string prompt("Hello, enter your name below: \n");
    string name;
    string msg = "";

    cout << prompt;
    cin >> name;

    msg += "Hello " + name;
    cout << msg;
    return 0;
}
