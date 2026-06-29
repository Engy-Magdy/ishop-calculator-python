#Greeting to inshop calculator
print("""
      ******Welcome to ishop calculator******
      """)
#Saving the names of items and their prices
all_items=[]
total_price=[]
#Asking about number of items
n=int(input("How many items are there in your basket today?\n"))
print("\nLet's get to counting them........")
#loops of the number of items
for i in range(1,n+1):
    name=input(f"Please tell me the name of the item number {i}:\n")
    all_items.append(name)
    price=int(input(f"What is the price of {name} $ ?\n"))
    total_price.append(price)
 #List of all items
list_items=input("Would you like to see your entire basket items ?").lower()
if list_items=="yes":
    print(all_items)
#List of total price
list_price=input("Would you like to see how much it will cost?\n").upper()
if list_price=="YES":
    print(f"Buying these items will cost:\n{sum(total_price)}")
else:
    input("Press enter to exit......")           


