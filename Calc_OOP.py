# CALCULATOR IN PYTHON USING OBJECT ORIENTED PROGRAMMING

# ALL THE FUNCTIONS
class funcies:
     def add( a , b):
         print(a+b);
     def subtract( a , b):
         print(a-b);
     def multiply( a , b):
         print(a*b);
     def divide( a , b):
         print(a/b);

# SELECTION & EXECUTION
class _XO__Calc:
    def __init__(self, mode, num1, num2) -> None:
        self.mode = mode;
        self.num1 = num1;
        self.num2 = num2;

        obj1 = funcies;
        if(mode == 1 or mode == '1'):
             obj1.add(num1, num2);
        elif(mode == 2 or mode == '2'):
             obj1.subtract(num1, num2);                       
        elif(mode == 3 or mode == '3'):
             obj1.multiply(num1, num2);    
        elif(mode == 4 or mode == '4'):
             obj1.divide(num1, num2);    
        else:
             print("__ERROR__ 469 ( Not valid option)")
             print("EXITING.....")
             exit(0)
        
# MAIN EXECUTION & USE
if __name__ == "__main__":

     md_selt = input("Enter the mode : ");
     n1 = int(input("Enter num1 : "))
     n2 = int(input("Enter num2 : "))

     __cal = _XO__Calc(md_selt, n1 , n2);
