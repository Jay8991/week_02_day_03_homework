
class Cart():
    def __init__(self):
        # empty dict
        self.shopping_dict = {}

    # adding new cart to dict
    def add_new(self, name, item_name):
        self.shopping_dict.update({name : [item_name]})
    # adding items to existing cart
    def add_exist(self, name, item_name):
        self.shopping_dict[name].append(item_name)
    # deleting items from a specific cart
    def delete(self, name, item_name):
        self.shopping_dict[name].remove(item_name)
    # showing what's inside of my dict
    def show(self):
        # if the length of the dict keys is 0 means its empty
        if len(self.shopping_dict.keys()) == 0:
            print("There are no items in your cart")
        else:
            print(self.shopping_dict)

def show_instructions():
    print("""Welcome to Shopping Cart Application
========================================
Type 'add' to add items to your shopping list.
Type 'show' to list all the items in your shopping list.
Type 'delete' to delete items in your shopping list.
Type 'quit' to exit the program. """)
    print("*" * 40)

def shopping_cart():
    done = False
    # instance of Cart
    cart1 = Cart()
    while not done:
        print("\n")
        print("*" * 40)
        show_instructions()

        choice = input("What is your choice? Add | Delete | Show | Quit? ").lower()
        if choice == 'add':
            # ask user if there a cart already there or want to create a new one 
            user_choice = int(input("Are you adding to existing cart(Press 1) or a new one(Press 2)? "))
            if(user_choice == 1):
                cart_name = input("What is your cart name? ").lower() 
                # check if cart actaully is in the dict or no 
                if cart_name in cart1.shopping_dict:
                    shopping_item = input("Which item do you want to add to your shopping list? ").lower()  
                    # add to exisiting cart
                    cart1.add_exist(cart_name, shopping_item)
                else:
                    print("Does not exist! Thank you")
            elif (user_choice == 2):
                cart_name = input("What do you want the name of your cart to be? ").lower()  
                shopping_item = input("Which item do you want to add to your shopping list? ").lower()  
                # create a new cart
                cart1.add_new(cart_name, shopping_item)
            else:
                print("Wrong Option Selected!!")

        elif choice == 'delete':
            user_choice = int(input("Do you want to delete the whole cart(Press 1) or item from one of your cart(Press 2)? "))
            if(user_choice == 1):
                name_of_cart = input("What is the name of your cart? ").lower()
                if name_of_cart in cart1.shopping_dict:
                    del cart1.shopping_dict[name_of_cart]
                else:
                    print("Cart doesn't exist!!")
            elif(user_choice == 2):
                name_of_cart = input("Which cart do you want to delete from? ").lower()
                if name_of_cart in cart1.shopping_dict:
                    delete_item = input("Which item do you want to delete? ").lower()
                    # check by looping if the item is inside of the cart before deleting
                    inside_cart = False
                    for i in cart1.shopping_dict.get(name_of_cart):
                        if i == delete_item:
                            inside_cart = True
                            cart1.delete(name_of_cart, delete_item)
                            break
                    if inside_cart:
                        print("Item deleted")
                    else:
                        print("Item doesn't exist")                      

                else:
                    print("Cart doesn't exist!!")
            else:
                print("Wrong Option!!")

        elif choice == 'show':
            cart1.show()

        elif choice == 'quit':
            confirm = input('Are you sure you want to quit? Y/N? ').lower()
            if confirm == 'y':
                done = True
                pass
            elif confirm == 'n':
                continue

        else:
            print("Invalid!! Try Again. ")
    print("Have a good day! Goodbye!")

shopping_cart()