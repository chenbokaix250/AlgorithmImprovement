#include<iostream>;
using namespace std;
int main() 
{
	int a[99][99], k;
	k = 1; 
	int n; 
	cin >> n;
	for (int i = 1; i <= 2 * n - 1; ++i)
		if (i <= n)//上三角
			if (i % 2 == 0)
				for (int j = i; j >= 1; --j) a[i - j + 1][j] = k, k++;
			else
				for (int j = 1; j <= i; ++j) a[i - j + 1][j] = k, k++;
		else if (i % 2 == 0)//下三角
			for (int j = n; j >= i - n + 1; --j) a[i - j + 1][j] = k, k++;
		else//下三角
			for (int j = i - n + 1; j <= n; ++j) a[i - j + 1][j] = k, k++;
	for (int i = 1; i <= n; ++i)
	{
		for (int j = 1; j < n; ++j) 
			cout<< a[i][j]<<" ";
		cout<<a[i][n] << endl;
	}
	return 0;
}
