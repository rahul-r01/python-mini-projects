menu={
    1:{
        "latte":{
            "ingredients":{
                "water":200,
                "milk":100,
                "coffee":25
            },
            "cost":150,
        },
    },
    2:{
        "espresso":{
            "ingredients":{
                "water":50,
                "coffee":18,
            },
            "cost":100,
        },
    },
    3:{
        "cappuccino":{
            "ingredients":{
                "water":250,
                "milk":150,
                "coffee":28,
            },
            "cost":200,
        },
    },
}

resources={
     "water":500,
     "milk":300,
     "coffee":100
}
profit=0
def check_resources(order_ingredients):
     for item in order_ingredients:
         if order_ingredients[item]>resources[item]:
               print(f"\nsorry there is not enough {item}")
               return False
     return True
def process_coins(coffee_name,coffee_cost):
       total_coins=0
       print(f"\n{coffee_name},COST:{coffee_cost}")
       print("\nmachine accept (5rs,10rs,20rs) coins only!")
       five_coins=int(input("insert no.of 5RS coins: "))
       ten_coins=int(input("insert no.of 10RS coins: "))
       twenty_coins=int(input("insert no.of 20RS coins: "))
       total_coins=(five_coins*5)+(ten_coins*10)+(twenty_coins*20)
       return total_coins
def check_payment(money_received,coffee_cost):
     if money_received>=coffee_cost:
          global profit
          profit+=coffee_cost
          change=money_received-coffee_cost
          print(f"\nHERE {change}RS change for you!")
          return True
     else:
          print(f"\nsorry!...that's not enough money..money refunded!")
          print(f"TAKE YOUR MONEY BACK:{money_received}")
          return False
def make_coffee(coffee_name,coffee_ingredients):
      for item in coffee_ingredients:
            resources[item]-=coffee_ingredients[item]
      print(f"\nHERE YOUR {coffee_name}...ENJOY!")
      print("________________________________")
print("***********COFFEE MACHINE*************")
print("______________________________________")
is_on=True
while is_on:
      print("\nWHAT WOULD YOU LIKE TO HAVE...")
      print("1.LATTE")
      print("2.ESPRESSO")
      print("3.CAPPUCCINO")
      print("4.REPORT")
      print("5.OFF")
      choice=int(input("enter your choice like to have: "))
      if choice==5:
          print("\nTHANK YOU..VISIT AGAIN!")
          is_on=False
      elif choice==4:
          print("\nRESOURCES REPORT...")
          print(f"water={resources["water"]}ml")
          print(f"milk={resources["milk"]}ml")
          print(f"coffee={resources["coffee"]}g")
          print(f"money={profit}")
      elif choice>0 and choice<4:
           coffee_type=menu[choice]
#          print(coffee_type)
           drink_name=list(coffee_type.keys())[0]
           if check_resources(coffee_type[drink_name]["ingredients"]):
                payment=process_coins(drink_name,coffee_type[drink_name]["cost"])
                if check_payment(payment,coffee_type[drink_name]["cost"]):
                     make_coffee(drink_name,coffee_type[drink_name]["ingredients"])
      else:
          print("\nINVALID CHOICE.. PLEASE CHOOSE VALID CHOICE!")            
