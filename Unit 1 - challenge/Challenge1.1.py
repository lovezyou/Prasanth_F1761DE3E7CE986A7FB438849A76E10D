'''creating a recursive function to find the factorial of the given number'''

def fact(num):                      #implementing recursive function
	if(num ==0 or num ==1):
		return(1)
	else :
		return(num*fact(num-1))     #it is equivalent to n*(n-1)

num=int(input("Enter number : "))   #the number is given by the user here

result=fact(num)                    #calculated factorial of the given number is stored in variable
print("factorial of number {} is {} .".format(num,result))  #displaying the fainal result
