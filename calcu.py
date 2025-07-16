
class calculator:

    def add(self,a,b):
        return int(a+b)
    
    def subtract(self,a,b):
        return int(a-b)
    
    def multiply(self,a,b):
        return int(a*b)
    
    def division(self,a,b):
        if b==0 :
            return "Error: Division by zero"
        return int(a/b)
    
    
    def calculate(self,s):
        parts=s.split()
        n=len(parts)
        result=0
        current=0
        i=0
        while i<n-2 :
                try:
                    first=int(parts[i])
                    i+=1
                    sign=parts[i]
                    i+=1
                    second=int(parts[i])
                except ValueError:
                    return "Invalid Number" 
               
                if(sign=='+'):
                   parts[i]=self.add(first,second)
                elif (sign=='-'):
                   parts[i]=self.subtract(first,second) 
                elif (sign=='*'):
                   parts[i]=self.multiply(first,second)
                elif (sign=='/'):
                   parts[i]=self.division(first,second)

                current=parts[i]
                result=current

        return result   
    


c=calculator()
print("launching the calculator")
s=""
user_input={"stop","exit","close","quit"}
while s not in user_input:
    print("Please Enter The Expression (Example :"," 2 + 3  ) Not This (Example :","2+3)")
    s=input("->") 
    output=c.calculate(s)
    print(output)
