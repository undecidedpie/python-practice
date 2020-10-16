#include <iostream>
#include <vector>
#include <string>

using namespace std;

int main()
{
    vector<string> msg {"Hello", "C++", "World", "from", "VS Code", "and the C++ extension!"};
    
    for (const string& word : msg)
    {
        cout << word << " ";
         do {
            cout << '\n' << "Press a key to continue...";
        } while (cin.get() != '\n');
    }
    cout << endl;
}