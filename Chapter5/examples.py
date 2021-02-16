#height = 1.95

#if height < 1.7:
   #print("You are too short.")
#elif height < 1.9:
   # print("You are Tall enough to enter.")
#else:
    #print("You are too tall.")


#requested_drinks = ['Coke','Chocolate Milkshake']

#if 'Coke' in requested_drinks:
    #print("Adding a Coke")
#elif 'Fanta' in requested_drinks:
    #print("Adding Fanta")
#elif 'Chocolate Milkshake' in requested_drinks:
    #print("Adding Chocolate Milkshake")

#print("\nEnjoy your drinks.")

available_drinks = ['Coke','Fanta','Sprite','Orange Juice']
requested_drinks =['Fanta','Apple Juice','Stoney']

for requested_drink in requested_drinks:
    if requested_drink in available_drinks:
        print(f"Adding {requested_drink}.")
    else:
        print(f"Sorry we do not have {requested_drink}.")