#a python package  must contain __init__.py file even it is empty

class SimpleMaths:
    clsAttribute="this is a class attribute"

    def __init__(self,x,y):
        self.op1=x
        self.op2=y

    def addition(self):
        print(f"this result of addition is: {self.op1+self.op2}")
    
    def subtraction(self):
        print(f"this result of subtraction is: {self.op1-self.op2}")

def sampleFunction(a,b):#it is a normal function
    print(f"a={a} and b={b}")
    
if __name__=="__main__":
    a=SimpleMaths(2,3)
    a.addition()
    a.subtraction()