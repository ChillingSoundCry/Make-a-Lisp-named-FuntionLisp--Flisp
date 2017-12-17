# Make-a-Lisp-named-Fucklisp--Flis
//至于我为什么弃坑c++，而用python来写，是因为c++得字符串处理能力太操蛋了，所以我用python已经实现
//了一个只有运算能力的脚本
//There needed to be solved a problem so show abandoned pit
//Find the solution and continue
#include <iostream>
#include <string>
#include <windows.h>
using namespace std;
char code[5000];
int ptr;

void deletblank()
{
	while(code[ptr]==' ')
	{
		ptr++;
	}
}
int getnum()
{
	char num[200];
	int i=0;
	while(code[ptr]>='0'&&code[ptr]<='9')
	{
		num[i]=code[ptr];
		ptr++;
	}
	
	cout<<num<<endl;
	int Num=*(int*)num;;
	return Num;
}
void interpret()
{
	ptr=0;
	deletblank();
	if(code[ptr]=='(')
	{
		ptr+=1;
		if(code[ptr]=='h'&&code[ptr+1]=='e'&&code[ptr+2]=='l'&&code[ptr+3]=='p')
		{
			ptr+=4;
			deletblank();
			if(code[ptr]==')'&&code[ptr+1]=='\0')
			{
				cout<<"flisp 1.0 I think I will make a good lisp that better than Scheme and Common lisp."<<endl;
			}
		}
		else if(code[ptr]=='+')
		{
			ptr++;
			deletblank();
			int x,y,z;
			if(code[ptr]>='0' && code[ptr]<='9')
			{
				 x=getnum();
			}
			deletblank();
			if(code[ptr]>='0' && code[ptr]<='9')
			{
				 y=getnum();
			}
			z=x+y;
			cout<<z<<endl;
		}
		else if(code[ptr]=='p'&&code[ptr+1]=='r'&&code[ptr+2]=='i'&&code[ptr+3]=='n'&&code[ptr+4]=='t')
		{
			ptr+=5;
			deletblank();
			if(code[ptr]=='"')
			{
				while(code[ptr]!='"')
				{
					cout<<code[ptr];
					ptr++;
				}
			}	
		}
	}
}/*
void rorw()
{
	////////////////////////////////////////////////////////////	
	ptr=0;
	int a=0;
    while(code[ptr]!='\0')
	{
		if(code[ptr]=='(')
		{
			a++;
		}
		else if(code[ptr]==')')
		{
			a--;
		}
		else if(code[ptr]==' ')
		{
			a+=2;
			a-=2;
		}
		ptr++;	
	}cout<<a<<endl;
	if(a==0)
	{
		
	}
	else if(a>0)
	{
		cout<<"Wrong! The'('is more or the ')' is less."<<endl;
	}
	else if(a<0)
	{
		cout<<"Wrong! The')'is more or the '(' is less."<<endl;
	}
	/////////////////////////////////////////////////////////////////////////////////////
}*/
int main()
{
	cout<<"fucklisp 1.0"<<endl;
	cout<<"I thing you need '(help)'"<<endl;
	while(1)
	{
	
		cout<<"->";
		cin>>code;
		interpret();
	}
	return 0;
}
