orinum =eval(input("enter a positive number: "))
digsum = 0;
num= orinum;
             
while num !=0 :
    digsum = digsum + num %10;
    num = num // 10;
    
if digsum % 2 ==0:
    print("sum of "+str(orinum)+" is "+str(digsum)+" which is even ")
else :
    print("sum of "+str(orinum)+" is "+str(digsum)+" which is old ")
