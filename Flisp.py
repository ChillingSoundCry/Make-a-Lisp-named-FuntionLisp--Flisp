#coding=UTF-8
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
		if(code[ptr:y]==name[i]):
			ptr+=y
			return gc[i]
	if(code[ptr]=='('):
		x=interpret(code)
	else:
		p=ptr
		while(code[p]<="9" and code[p]>="0"):
			p+=1
		x=int(code[ptr:p])
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
		else:
			print("!!!")		
def main():
	global ptr
	ptr=0
	code=input('->')
	print(code)
	result=interpret(code)
	if(result!=None):
		print(result)
	main()
if __name__ == '__main__':
	print('---------------Flisp------------------')
	print('A Lisp Like Funtion Program Lungrauge!')
	print('--------------v 0.5-------------------')
	main()
