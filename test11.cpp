#include <iostream>
// write your code here......
#include<map>
using namespace std;
#include<string>
 
int main() {
 
	string str;
	getline(cin,str);
	
	// write your code here......
	map<char, int>m;
	int i = 0;
	while (str[i] != '\0')
	{
		if (isalpha(str[i]))
		{
			m[str[i]]++;
			i++;
		}
		else
		{
			i++;
		}
		
	}
	for (auto i = m.begin(); i != m.end(); i++)
	{
		cout << i->first << ":" << i->second << endl;
	}
 
	return 0;
}