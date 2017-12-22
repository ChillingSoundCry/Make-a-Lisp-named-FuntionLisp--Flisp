#coding=UTF-8
ptr=0
def delblank(code):
	global ptr
	while(code[ptr]==" "):
              ptr+=1
def getnum(code):
	global ptr
	delblank(code)
	x=0
	if(code[ptr]=='('):
		x=interpret(code)
	else:
		p=ptr
		while(code[p]<="9" and code[p]>="0"):
			p+=1
		x=int(code[ptr:p])
		ptr=p
	return x
def interpret(code):
	global ptr
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
			
		else:
			print("!!!")	
def main():
	global ptr
	ptr=0
	code=input('->')
	print(code)
	result=interpret(code)
	print(result)
	main()
if __name__ == '__main__':
	print('---------------Flisp------------------')
	print('A Lisp Like Funtion Program Lungrauge!')
	print('--------------v 0.5-------------------')
	main()
