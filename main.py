#Greeting to inshop calculator
print("""
      
      ******Welcome to ishop calculator******
      """)
#Saving the names of items and their prices
all_items=[]
total_price=[]
#Asking about number of items
n=int(input("How many items are there in your basket today?\n"))
if n>0:
  print("\nLet's get to counting them........")
#loops of the number of items and their prices
  for i in range(1,n+1):
    name=input(f"Please tell me the name of the item number {i}:\n")
    all_items.append(name)
    price=float(input(f"What is the price of {name} $ ?\n"))
    total_price.append(price)
 #List of all items
  list_items=input("Would you like to see your entire basket items ?\n").lower()
  if list_items=="yes":
      print(all_items)
#List of all prices      
  list_total_price=input("Would you to see how much it will cost?").upper()
  if  list_total_price=="YES":
      print(f"Buying these items will cost:\n{sum(total_price)}")
  else:
      input("Press enter to exit......")
else:
    input("It seems that you do not want to buy something.Press enter to exit.....")        

   

