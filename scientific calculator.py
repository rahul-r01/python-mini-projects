import math

def calculator(op,n):
   if op=='+':
       result=0
       for i in n:
           result+=i
       return result
   elif op=='-':
       result=n[0]
       for i in n[1:]:
          result-=i
       return result
   elif op=='*':
       result=1
       for i in n:
          result*=i
       return result
   elif op=='/':
       result=n[0]
       for i in n[1:]:
           if i == 0:
                return "Error: Division by zero"
           result/=i
       return result  
   elif op=='//':
       result=n[0]
       for i in n[1:]:
           if i == 0:
                return "Error: Floor by zero"
           result//=i
       return result 
   elif op=='%':
       result=n[0]
       for i in n[1:]:
          if i == 0:
                return "Error: modulo Division by zero"
          result%=i
       return result  
   elif op=='^':
       result=n[0]
       for i in n[1:]:
           if result==0 and i<0:
               return "ZeroDovisionError: 0 cannot be raised to negative power!"
           result**=i
       return result        
   elif op=='√':
       result=n[0]
       if result<0:
           return "Error: cannot find square root of negative number"
       return result**0.5   
   elif op=='log':
       result=n[0]
       if result<=0:
           return "Error: log is defined only for positive numbers!"
       return math.log10(result)
   elif op=='sin':
       rad=math.radians(n[0])
       return math.sin(rad)
   elif op=='cos':
       rad=math.radians(n[0])
       cos_val=math.cos(rad)
       if abs(cos_val)<1e-10:
            return 0
       return math.cos(rad)
   elif op=='tan':
       rad=math.radians(n[0])
       cos_val=math.cos(rad)
       if abs(cos_val)<1e-10:
           return "Error:cos tan is undefined for this angle(infinity)!"
       return math.tan(rad)
               

def information():
    while True:
        operator=input("\nPICK A OPERATOR(+,-,*,/,%,//,^,√,log,sin,cos,tan): ")
        if operator not in ['+','-','*','/','//','%','^','√','log','sin','cos','tan']:
            print("Invalid operator..please enter correct operator!")
            continue
        try:
            nums=list(map(float,input("enter a numbers separated by space: ").split()))
        except ValueError:
            print("please enter valid integers only!")
            continue
        if len(nums)==0:
            print("No Numbers are provided..please enter a numbers!")
            continue
        if operator in ['√','log','sin','cos','tan'] and len(nums)!=1:
            print("please enter only one number for this operation!")
            continue
        if operator in ['√','log','sin','cos','tan']:
            expression=f"{operator}{nums[0]}={calculator(operator,nums)}"
        else:
            expression=f"{operator.join(map(str,nums))}={calculator(operator,nums)}"
        print(expression)
        history_list.append(expression)
        again=input("\nDo you want to calculate again! Enter (Y/N): ").lower()
        if again!='y':
           print("THANK YOU!\n")
           break
def history(h):
    if not history_list:
        print("\nNO CALCULATION history available!")
    else:
        print("\n---CALCULATION HISTORY---")
        for item in h:
            print(item)
def clear_history(h):
    if h:
       h.clear()
       print("\nCLACULATION HISTORY IS CLEARED SUCCESSFULLY!") 
    else:
        print("\nNO HISTORY IS AVAILABLE TO CLEAR!")
            
                   
history_list=[]       
print("**********SCIENTIFIC CALCULATOR**********")
print("_________________________________________")
while True:
    print("\nDESCRIPTION:")
    choice=int(input("1.CALCULATION \n2.HISTORY \n3.CLEAR HISTORY \n4.QUIT \nenter your choice: "))
    if choice==1:
       information()
    elif choice==2:
       history(history_list)  
    elif choice==3:
        clear_history(history_list)
    elif choice==4:
        print("\nTHANK YOU!")
        break   
    else:
        print("\ninvalid choice...please enter correct choice!")