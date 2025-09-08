report={"water": 400, 
        "milk": 300,
        "coffee":100,
        "cost": 0 } 

def coin_cal():
    quarter=int(input("how many quarters? ")) 
    dimes=int(input("how many dimes? ")) 
    nickles= int(input("how many nickels? ")) 
    penny= int(input("how many pennies? " )) 
    total_bill= (quarter *0.25) + (dimes* 0.10)+ (nickles*0.05)+ (penny*0.01)
    return total_bill



coffee_flavour={"latte":{"water": 150, "milk": 100,"coffee": 30}, 
                "cappuccino":{"water": 100, "milk": 150, "coffee": 40}, 
                "espresso":{"water": 200, "milk": 70,"coffee": 60}}

machine_is_on = True
while machine_is_on: #while true do the following 
    user_choice= input("what would you like? (espresso/latte/cappuccino): ")
    
    if user_choice == "latte":
        if report["water"]>= coffee_flavour["latte"]["water"] and\
            report["milk"]>= coffee_flavour["latte"]["milk"] and\
            report ["coffee"]>= coffee_flavour["latte"]["coffee"]:
                report["water"]-=coffee_flavour["latte"]["water"]
                report["milk"]-=coffee_flavour["latte"]["milk"]
                report["coffe"]-=coffee_flavour["latte"]["coffee"]
                print("please insert some coin:")
                total_amount= coin_cal()
                if total_amount>= 6:
                    offer_change= total_amount-6
                    print(f"Your change is ${offer_change:.2f} Enjoy your coffee")
                    report["cost"]+=6
                else:
                     print("sorry! that is not enough money to buy a coffe. Money refunded")         
        else:
            print("Sorry! we dont have enough ingredients to make your coffee. ")

    elif user_choice == "espresso":
        if report["water"]>= coffee_flavour["espresso"]["water"]and\
            report["milk"]>= coffee_flavour["espresso"]["milk"] and\
            report["coffee"]>= coffee_flavour["espresso"]["coffee"]:
                report["water"]-=coffee_flavour["espresso"]["water"]
                report["milk"]-=coffee_flavour["espresso"]["milk"]
                report["coffe"]-=coffee_flavour["espresso"]["coffee"]
                print("please insert some coin:")
                total_amount= coin_cal()
                if total_amount>= 3:
                    offer_change= total_amount-3
                    print(f"your change is ${offer_change:.2f} Enjoy your coffee")
                    report["cost"]+=3
                else:
                     print("sorry! that is not enough money to buy a coffe. Money refunded")
        else:
            print("Sorry! we dont have enough ingredients to make your coffee. ")

    elif user_choice == "cappuccino":
        if report["water"]>= coffee_flavour["cappuccino"]["water"] and \
            report["milk"]>= coffee_flavour["cappuccino"]["milk"] and \
            report["coffee"]>= coffee_flavour["cappuccino"]["coffee"]:
                report["water"]-=coffee_flavour["cappuccino"]["water"]
                report["milk"]-=coffee_flavour["cappuccino"]["milk"]
                report["coffee"]-=coffee_flavour["cappuccino"]["coffee"]
                print("please insert some coin:")
                total_amount= coin_cal()
                if total_amount>= 8:
                    offer_change= total_amount-8
                    print(f"your change is ${offer_change:.2f} Enjoy your coffee")
                    report["cost"]+=8
                else:
                     print("sorry! that is not enough money to buy a coffe. Money refunded")
        else:
            print("Sorry! we dont have enough ingredients to make your coffee. ")

    elif user_choice=="report":
        print(report)
    else:
        user_choice == "off"
        machine_is_on = False
