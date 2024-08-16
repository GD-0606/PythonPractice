"""
 -->what type a coffee do you need?
    1.Cappuccino
    2.Espresso
    3.Latte
 -->Insert coins 
"""
"""
    Menu Display:

    Show available coffee options (e.g., Espresso, Latte, Cappuccino).
    Display prices for each option.
"""
"""
Let's assume the following hypothetical costs:

Coffee beans: ₹1 per gram
Milk: ₹0.10 per milliliter
Water: ₹0.02 per milliliter

For a Latte:

    Coffee Beans: 18 grams = 18 * ₹1 = ₹18
    Milk: 150 ml = 150 * ₹0.10 = ₹15
    Water: 50 ml = 50 * ₹0.02 = ₹1
    Total Ingredient Cost: ₹18 + ₹15 + ₹1 = ₹34

    Now, add operational costs and a profit margin:

        Operational Costs: ₹5 (arbitrary estimate)
        Total Cost: ₹34 + ₹5 = ₹39
        Profit Margin: 50% of ₹39 = ₹19.5
        Final Price: ₹39 + ₹19.5 = ₹58.5
        Rounded Price: ₹59

"""
# water in ml , milk in ml and coffee_beans in gms
coffee_recipes = {
    "Espresso": {
        "water": 50,
        "coffee_beans": 18,
        "milk": 0
    },
    "Latte": {
        "water": 50,  
        "coffee_beans": 18,  
        "milk": 150 
    },
    "Cappuccino": {
        "water": 50,  
        "coffee_beans": 18, 
        "milk": 100,  
        "foam": 50  
    }
}

available_quanities={
    "water":350,
    "milk":500,
    "coffee_beans":450
}
recipes_prizes={
    "Latte":59,
    "Espresso":29,
    "Cappuccino":54
}

balance=100
print("Menu Display")
print("Available Coffee Options")
print("\t1. Espresso (Rs.29/-) \n\t2. Latte (Rs.59/-) \n\t3. Cappuccino (Rs.54/-)")





"""
 Order Processing

"""
def check_resource(type):
      print(type)
      avail_water,avail_milk,avail_coffee_beans=available_quanities.values()
    # print(avail_water,avail_milk,avail_coffee_beans)
      isResourcesAvailable=None

      match(type):
        case "Latte":
            water_quanity,coffee_beans_quanity,milk_quanity=coffee_recipes[type].values()
            # print(water_quanity,coffee_beans_quanity,milk_quanity)
            if((avail_water-water_quanity > 0) and (avail_milk-milk_quanity > 0) and (avail_coffee_beans-coffee_beans_quanity > 0)):
                 available_quanities["water"]=avail_water-water_quanity
                 available_quanities["milk"]=avail_milk-milk_quanity
                 available_quanities["coffee_beans"]=avail_coffee_beans-coffee_beans_quanity
                 isResourcesAvailable=True
            else:
                 print("Resources are Completed.")
                 isResourcesAvailable=False
            print(available_quanities)


        case "Espresso":
            water_quanity,coffee_beans_quanity,milk_quanity=coffee_recipes[type].values()
            # print(water_quanity,coffee_beans_quanity,milk_quanity)
            if((avail_water-water_quanity > 0) and (avail_milk-milk_quanity > 0) and (avail_coffee_beans-coffee_beans_quanity > 0)):
                 available_quanities["water"]=avail_water-water_quanity
                 available_quanities["milk"]=avail_milk-milk_quanity
                 available_quanities["coffee_beans"]=avail_coffee_beans-coffee_beans_quanity
                 isResourcesAvailable=True
            else:
                 print("Resources are Completed.")
                 isResourcesAvailable=False
            print(available_quanities)
        case "Cappuccino":
            water_quanity,coffee_beans_quanity,milk_quanity,foam_quanity=coffee_recipes[type].values()
            #print(water_quanity,coffee_beans_quanity,milk_quanity,foam_quanity)
            if((avail_water-water_quanity > 0) and (avail_milk-milk_quanity+foam_quanity > 0) and (avail_coffee_beans-coffee_beans_quanity > 0)):
                 available_quanities["water"]=avail_water-water_quanity
                 available_quanities["milk"]=avail_milk-milk_quanity+foam_quanity
                 available_quanities["coffee_beans"]=avail_coffee_beans-coffee_beans_quanity
                 isResourcesAvailable=True
            else:
                 print("Resources are Completed.")
                 isResourcesAvailable=False
            print(available_quanities)
        case _:
            print("Not Allowed")
            isResourcesAvailable=False
      return isResourcesAvailable
      
# handling the payments
def handlePayment(**order_details):
    type,five,ten,twoZero=order_details.values()
    print(type,five,ten,twoZero)
    userAmount=five*5+ten*10+twoZero*20
    print(userAmount)
    global balance
    if(userAmount>=recipes_prizes[type] and abs(userAmount-recipes_prizes[type]) <= balance):
        print("Checking the Available Resources")
        isAvail=check_resource(type)
        print(isAvail)
        if(isAvail):
             balance=balance+userAmount-abs(userAmount-recipes_prizes[type])
             print("Collect your coffee.")
             print("Return Amount",abs(userAmount-recipes_prizes[type]))
        
        
    elif(userAmount<recipes_prizes[type]):
            print("=== InSufficient Amount ===")
            required_amount=recipes_prizes[type]-userAmount
            print(f"To Process the Order , You Have to pay {required_amount} more.")
    elif(userAmount>recipes_prizes[type] and abs(userAmount-recipes_prizes[type]) > balance):
            print("=== InSufficient Balance ===")
            insufficient_amount=abs(userAmount-recipes_prizes[type])
            print(f"Sorry , I need  not have enough balance to give the return change {insufficient_amount} for you.")
            print("Available Balance = " , balance)
    


def order_processing():
    coffeeType=input("Please Select one of the Coffee Type = ")
    print(coffeeType)
    print("==== Plaese Insert the Coins ====")
    fiveCoins=int(input("How many 5Rs. conis = "))
    tenCoins=int(input("How many 10Rs. conis = "))
    twoZeroCoins=int(input("How many 20Rs. conis = "))
    print(fiveCoins,tenCoins,twoZeroCoins)
    handlePayment(type=coffeeType,five=fiveCoins,ten=tenCoins,twoZero=twoZeroCoins)
    print("Balance = ",balance)

order_processing()
"""


"""