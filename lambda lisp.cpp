#include <iostream>
#include <string>
#include <fstream>
#include <windows.h>
using namespace std;
char code[5000]={0};
int ptr;
int result=0;
void deletblank();
int getnum();
int interpret();
void rorw();
void open();
int main()
{
	open();
	result=interpret();
	return 0;
}



void open()
{
	cout<<"lambda lisp"<<endl;
	ifstream fin("D:\\lisp.txt");
	cout<<"正在打开文档中。。。。"<<endl;
	if( ! fin )
	{
		cerr<<"打开失败！！！"<<endl;
		getchar();
	}
	cout<<"打开成功！！！"<<endl;
	int i=0;
	fin>>noskipws;
	while( ! fin.eof() )
	{
		fin>>code[i];
		i++;
	}
	fin.close();  
	cout<<code<<endl;
	rorw();
	cout<<"开始执行："<<endl;
}
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
	int n;
	if(code[ptr]>='0'&&code[ptr]<='9')
	{
	while(code[ptr]>='0'&&code[ptr]<='9')
	{
		num[i]=code[ptr];
		ptr++;
		i++;
	}
	n=atoi(num);
    }
    else if(code[ptr]=='(')
    {
    	n=interpret(); 
    	ptr++;
	}
	//cout<<num<<endl;
	return n;
}
int interpret()
{
	deletblank();
	if(code[ptr]=='(')
	{
		ptr+=1;
		if(code[ptr]=='+')
		{
			ptr++;
			deletblank();
			int x,num=0;
			while(code[ptr]!=')')
			{
				x=getnum();
				num+=x;
				deletblank();
		   }
			return num;
		}
		else if(code[ptr]=='-')
		{
			ptr++;
			deletblank();
			int x,num=getnum();
			deletblank();
			while(code[ptr]!=')')
			{
				x=getnum();
				num-=x;
				deletblank();
		   }
			return num;
		}
		else if(code[ptr]=='*')
		{
			ptr++;
			deletblank();
			int x,num=getnum();
			deletblank();
			while(code[ptr]!=')')
			{
				x=getnum();
				num*=x;
				deletblank();
		   }
			return num;
		}
		else if(code[ptr]=='/')
		{
			ptr++;
			deletblank();
			int x,num=getnum();
			deletblank();
			while(code[ptr]!=')')
			{
				x=getnum();
				num/=x;
				deletblank();
		   }
			return num;
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
				cout<<endl; 
			}
			else if (code[ptr]=='(')
			{
				cout<<interpret()<<endl;
			}	
		}
	}
}
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
	}
	if(a==0)
	{
		cout<<"Right"<<endl;
	}
	else if(a>0)
	{
		cout<<"Wrong! The'('is more or the ')' is less."<<endl;
	}
	else if(a<0)
	{
		cout<<"Wrong! The')'is more or the '(' is less."<<endl;
	}
	ptr=0;
	/////////////////////////////////////////////////////////////////////////////////////
}
