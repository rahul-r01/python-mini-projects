class BankSystem:
      def __init__(self,name,balance):
          self.name=name
          self.__balance=balance
          self.__pin=""
          self.__pin_attempts=3
      def amount_deposit(self,amount):
          if amount<=0:
              print("Enter a valid amount!")
          else:    
             self.__balance+=amount
             print(f"\nAmount {amount} is deposited in your bank account successfully!")
      def amount_withdraw(self,amount):
           if amount<=0:
               print("Enter a valid amount!")
           elif amount<=self.__balance:
                 self.__balance-=amount
                 print(f"\namount {amount} withdraw successfully!")
           else:
                 print("\nInsufficient amount!")
      def check_balance(self):
           if self.__pin=="":
               print("\nPLEASE SET PIN FIRST!")
               return
           if self.__pin_attempts == 0:
               print("ACCOUNT LOCKED! Try again after 48 hours.")
               return    
           while True:    
                    pin_no=input("\nEnter a pin number: ")
                    if pin_no==self.__pin:
                        print(f"\n{self.name}'s ACCOUNT DETAILS")
                        print(f"BALANCE: {self.__balance}")
                        self.__pin_attempts=3
                        break
                    else:
                        self.__pin_attempts-=1
                        print(f"\nwrong pin! Attempts left: {self.__pin_attempts}!")
                        if self.__pin_attempts==0:
                           print("Account locked for 48 hours!To many wrong pin attempts!")
                           break
      def set_pin(self):
          if self.__pin=="":
              new_pin=input("\nEnter a pin to set: ")
              if new_pin.isdigit() and len(new_pin)==4:
                  self.__pin=new_pin
                  self.__pin_attempts=3
                  print("PIN SET SUCCESSFULLY!")
              else:
                  print("PIN MUST BE 4 CHARACTERS IN DIGITS!")
          else:
              print("PIN SET ALREADY!")    
      def change_pin(self):
          if self.__pin=="":
              print("\nplease set pin first!")
              return
          if self.__pin_attempts == 0:
                  print("ACCOUNT LOCKED! Cannot change PIN now.")
                  return     
          while True:
                 old_pin=input("\nEnter a old pin: ")
                 if old_pin==self.__pin:
                     new_pin=input("Enter a new pin: ")
                     if new_pin.isdigit() and len(new_pin)==4:
                         self.__pin=new_pin
                         self.__pin_attempts=3
                         print("\nPIN CHANGED SUCCESSFULLY!")
                         break
                     else:
                         print("PIN MUST BE 4 CHARACTERS IN DIGITS!")
                 else:
                     self.__pin_attempts-=1
                     print(f"Incorrect Old pin!Attempts left: {self.__pin_attempts}")  
                     if self.__pin_attempts==0:
                          print("Account locked for 48 hours!Cannot change pin!")
                          break
      def reset_attempts(self):
          self.__pin_attempts=3
   
accounts={
    "1001":BankSystem("Rahul",500),
    "1002":BankSystem("Manisha",700),
    "1003":BankSystem("Sathwika",1000),
    "1004":BankSystem("srujana",2000),
    "1005":BankSystem("chandu",2500),
    "1006":BankSystem("sanjana",3000)
    
}
print("********BANK ATM SYSTEM********")
print("_______________________________")
while True:
      print("\nDESCRIPTION:")
      print("  1.FETCHING ACCOUNT")
      print("  2.LOGOUT")
      try:
         log_in=int(input("Enter your choice: "))
      except ValueError:
          print("VALUE ERROR: ENTER DIGITS ONLY!")
          continue
      if log_in==2:
          print("YOU LOGOUT SUCCESSFULLY!")
          break
      if log_in==1:
          num=True
          while num:
               account_no=input("\nENTER A LAST 4 DIGITS OF ACCONUT NO: ")
               if not account_no.isdigit() or len(account_no)!=4:
                   print("Enter valid 4 digit account number!")
                   continue
               if account_no not in accounts:
                   print("ACCOUNT NOT EXISTS!")
                   continue
               else:     
                   user=accounts[account_no] 
                   while True:    
                     print(f"\nLOGGED IN AS:  {user.name}")
                     print("1.DEPOSIT")
                     print("2.WITHDRAW")
                     print("3.CHECK BALANCE")
                     print("4.SET PIN")
                     print("5.PIN CHANGE")
                     print("6.EXIT")
                     try:
                        choice=int(input("enter a your choice: "))
                     except ValueError:
                        print("ValueError:enter a valid choice!")
                        continue
                     if choice==1:
                        amount=int(input("\nenter a your deposit amount: "))
                        user.amount_deposit(amount)
                     elif choice==2:
                        amount=int(input("\nenter your withdraw amount: "))
                        user.amount_withdraw(amount)
                     elif choice==3:
                        user.check_balance()
                        user.reset_attempts()
                     elif choice==4:
                        user.set_pin()
                     elif choice==5:
                        user.change_pin()
                        user.reset_attempts()
                     elif choice==6:
                        print("\nexiting...Thank you!")
                        print("visit again")
                        num=False
                        break
                     else:
                        print("invalid choice..try again!")   
      else:
          print("\ninvalid choice...enter correct choice!")