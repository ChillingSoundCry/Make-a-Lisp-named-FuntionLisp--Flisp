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
                #print(code[ptr:p])
		x=int(code[ptr:p])#!!!
                ptr=p
        return x
def interpret(code):
	global ptr
	if(code[ptr]=='('):
		ptr+=1
		delblank(code)
		if(code[ptr]=='+'):
		    ptr+=1
		    x=getnum(code)
		    y=getnum(code)
                    delblank(code)
                    #print(x," ",y," ",x+y," ",ptr)
		    return x+y
		    #if(code[ptr]==')'):
		    	#main()
                elif(code[ptr]=='-'):
                    ptr+=1
		    x=getnum(code)
		    y=getnum(code)
                    delblank(code)
                    #print(x," ",y," ",x-y)
		    return x-y
		    #if(code[ptr]==')'):
		    	#main()
		elif(code[ptr]=='*'):
		    ptr+=1
		    x=getnum(code)
		    y=getnum(code)
                    delblank(code)
		    return x*y
		    #if(code[ptr]==')'):
		    	#main()
		elif(code[ptr]=='/'):
		    ptr+=1
		    x=getnum(code)
		    y=getnum(code)
		    delblank(code)
		    return x/y
		    #if(code[ptr]==')'):
		    	#main()
		else:
			print("!!!")

			
def main():
        code=raw_input("->")
        #print (code)
	result=interpret(code)
	print(result)
        main()
if __name__ == '__main__':
	main()