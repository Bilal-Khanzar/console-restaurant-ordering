#define the meno of a resotran 

menu = {
    'pizza':33,
    'burger':12,
    'pasta':12,
    'salad': 21,
    'coffee':[40,50]

}

#greet

print('welcome to B.W.M.K Restorant')

#price
print("pizza : TL 33\n burger: TL12\n pasta : TL12\n salad: TL21 \n coffe: TL[40,50]")


#user order
order_total = 0

while(True):
    item_x = input("enter the items that you want to order ")

    if item_x in menu:
        if item_x == 'coffee':
          
            coffee_type = input("Would you like sugar or normal? ").lower()
            if coffee_type == "sugar":
                order_total += menu["coffee"][0]
            else:
                order_total += menu["coffee"][1]
        else:
            order_total += menu[item_x]
              
        
        
    else:
      print('we dont have this please take help from someones know ')
      item_x
# user will choice if he want it will continue or if he does not project s will done
    second_y_n = input("Would you like to order something else? (yes/no): ").lower()
    if second_y_n != "yes":
        print(f"\nYour total bill is: TL {order_total}. Thank you for ordering!")
        break


























