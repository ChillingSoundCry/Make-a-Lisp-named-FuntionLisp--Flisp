#coding=UTF-8
import random as rd
import msvcrt
ptr=0
gcptr=0
name=[1]*100
gc=[1]*100
def delblank(code):
	global ptr
	while(code[ptr]==" "):
              ptr+=1
def getnum(code):
	global ptr
	global gcptr
	global name
	global gc
	delblank(code)
	x=0
	y=0
	for i in range(0,gcptr):
		y=len(name[i])
		if(code[ptr:ptr+y]==name[i]):
			ptr+=y
			return gc[i]
	if(code[ptr]=='('):
		x=interpret(code)
	else:
		p=ptr
		while(code[p]<="9" and code[p]>="0"):
			p+=1
		x=int(code[ptr:p].encode("utf-8"))
		ptr=p
	return x
def gconstant(code):
	global ptr
	global gcptr
	global name
	global gc
	delblank(code)
	p=ptr
	while(code[p]!=' '):
		p+=1
	n=code[ptr:p]
	ptr=p
	print(n)
	c=getnum(code)
	name[gcptr]=n
	gc[gcptr]=c
	gcptr+=1
def interpret(code):
	global ptr
	global gcptr
	global name
	global gc
	for i in range(0,gcptr):
		if(code==name[i]):
			return gc[i]
	if(code[ptr]=='('):
		ptr+=1
		delblank(code)
		if(code[ptr]=='+'):
		    ptr+=1
		    num=0
		    while(code[ptr]!=')'):
		    	x=getnum(code)
		    	num+=x
		    delblank(code)
		    return num
		elif(code[ptr]=='-'):
			ptr+=1
			num=getnum(code)
			while(code[ptr]!=')'):
				x=getnum(code)
				num-=x
			delblank(code)
			return num
		elif(code[ptr]=='*'):
			ptr+=1
			num=getnum(code)
			while(code[ptr]!=')'):
				x=getnum(code)
				num*=x
			delblank(code)
			return num
		elif(code[ptr]=='/'):
		    ptr+=1
		    num=getnum(code)
		    while(code[ptr]!=')'):
		    	x=getnum(code)
		    	num/=x
		    delblank(code)
		    return num
		elif(code[ptr:ptr+3]=='def'):
			ptr+=3
			gconstant(code)
		elif(code[ptr:ptr+6]=='random'):
			ptr+=6
			delblank(code)
			if(code[ptr]==')'):
				return rd.random()
			elif(code[ptr]!=')'):
				a=getnum(code)
				delblank(code)
				if(code[ptr]==','):
					ptr+=1
					b=getnum(code)
					delblank(code)
					if(code[ptr]==')'):
						return rd.randint(a,b)
		elif(code[ptr:ptr+5]=='print'):
			ptr+=5
			delblank(code)
			if(code[ptr]=='"'):
				ptr+=1
				while(code[ptr]!='"'):
					print(code[ptr],end='')
					ptr+=1
				if(code[ptr+1]=='.'):
					print(end='\n')
			elif(code[ptr]=='.'):
				print(end='\n')
			else:
				for i in range(0,gcptr):
					y=len(name[i])
					if(code[ptr:ptr+y]==name[i]):
						ptr+=y
						print(gc[i],end='')
			if(code[ptr]=='.'):
				print(end='\n')
		elif(code[ptr:ptr+4]=='help' or code[ptr]=='?'):
			print('暂时只有加减乘除和定义常量')
			print('方法为def 输出为print 输入为getLine 随机数为random')
		else:
			print("!!!")		
def main():
	global ptr
	ptr=0
	code=input('->')
	#print(code)
	result=interpret(code)
	if(result!=None):
		print(result)
	main()
if __name__ == '__main__':
	print('---------------Flisp------------------')
	print('A Lisp Like Funtion Program Lungrauge!')
	print('------This is only a Interpreter------')
	print('--------------v 0.1-------------------')
	main()
