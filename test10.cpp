#include <iostream>    
using namespace std;  
int main( )  
{  
	double dSalary,dTax = 0,dNetIncome = 0;  //请欣符合匈牙利命名法的变量名
	double dValue;   //在模板基础上加一个变量，表示超出起征点的收入
	double dRate, dOffset;  //分别表示税率和速算扣除数
	int iStep;       //用于确定交税的“档次”
	cout<<"请输入您本月的收入总额（元）：";  
	cin>>dSalary;  
	dValue = dSalary - 3500;   //在起征点基础上考虑纳税 
	if(dValue <= 0.0)  
		dTax = 0.0;  //不需要交税
	else  
	{  
		//这一组if语句确定交税的档次
		if(dValue <= 1500)
			iStep = 1;
		else if(dValue <= 4500)
			iStep = 2;
		else if(dValue <= 9000)
			iStep = 3;
		else if(dValue <= 35000)
			iStep = 4;
		else if(dValue <= 55000) 
			iStep = 5;
		else if(dValue <= 80000)
			iStep = 6;
		else 
			iStep = 7;

		//根据确定的档次，得到税率和速算扣除数，这样处理和问题中给出的列表形式有较好的对应
		//如果按照教材中的例子，通过类似c=s/n（n最大取500）的形式得到switch的<表达式>，下面的清单得列的很长
		switch(iStep)
		{
		case 1:
			dRate = 0.03, dOffset = 0.0;  break; 
		case 2:
			dRate = 0.1, dOffset = 105.0;  break;
		case 3:
			dRate = 0.2, dOffset = 555.0;   break;
		case 4:
			dRate = 0.25, dOffset = 1005.0;  break;
		case 5:
			dRate = 0.3, dOffset = 2755.0;   break;
		case 6:
			dRate = 0.35, dOffset = 5505.0;   break;
		case 7:
			dRate = 0.45, dOffset = 13505.0;  
		}
		dTax = dValue * dRate - dOffset;  //计算所得税，体会将“确定参数”与“计算”分开的好处：思路更明晰，不易在计算公式上犯大错
	}  
	dNetIncome = dSalary-dTax;        //计算税后收入
	cout<<"您本月应缴个人所得税 "<<dTax<<" 元，税后收入是 "<<dNetIncome<<" 元。\n";  
	cout<<"依法纳税，共享繁荣。谢谢使用！\n";  
	return 0;  
} 
