# MODULE 1: Menu management

class FoodItem:
    def __init__(self , item_id, name, price, category):
        self.info = (item_id ,name)
        self.price = price
        self.category = category

    def calculate_price(self,qty):
        return self.price * qty

class MainCourse(FoodItem):
    def __init__(self, item_id, name,price):
        super().__init__(item_id , name ,price ,"Main Course")

    def calculate_price(self,qty):
        return (self.price *qty) * 1.05

class Beverage(FoodItem):
    def __init__(self, item_id,name,price):
        super().__init__(item_id,name ,price, "Beverage")

    def calculate_price(self, qty):
        return (self.price + 10) *qty

class Dessert(FoodItem):
    def __init__(self,item_id, name , price):
        super().__init__(item_id, name, price , "Dessert")


categories = {"Main Course", "Beverage", "Dessert"}
menu = {
    "Butter Paneer": MainCourse(101, "Butter Paneer", 250),
    "Butter Chicken" : MainCourse(102 , "Butter Chicken" , 350),
    "Garlic Naan" : MainCourse(103 ,"Garlic Naan",70),
    "Coke" : Beverage(201 ,"Coke", 70),
    "Coffee" : Beverage(202 , "Coffee" , 100),
    "Tea" : Beverage(203, "Tea" , 50),
    "Brownie" : Dessert(301 , "Brownie", 120),
    "Gulab Jamun" : Dessert(302 , "Gulab Jamun" ,50)
}

def show_menu():
    print("\n            --- RESTAURANT MENU ---")
    print("Categories:", categories)
    print("ID - Item Name (Category) : Price")
    for name, item in menu.items():
        print(f"{item.info[0]} - {item.info[1]} ({item.category}) : Rs. {item.price}")

# MODULE 2 : order and billing

def take_order():
    order_list = []
    show_menu()

    while True :
        try:
            item_name= input("\nEnter food item name or done to finish): ").strip().title()

            if item_name.lower() == "done":
                break

            if item_name not in menu:
                raise KeyError(f"'{item_name}' is not available on the menu.")

            qty = int(input(f"Enter quantity for {item_name}: "))
            if qty <= 0:
                raise ValueError("Quantity must be at least 1.")

            order_list.append((item_name ,qty))
            print(f"Added: {qty} x {item_name}")

        except KeyError as e:
            print(f"Item Error: {e}")
        except ValueError as e:
            print(f"Quantity Error: {e}")

    return order_list

def generate_bill(order_list):
    if not order_list:
        print("\nNo items ordered.")
        return None,0

    bill_details ={}
    grand_total =0.0

    for item_name, qty in order_list:
        food_obj = menu[item_name]
        cost = food_obj.calculate_price(qty)

        if item_name in bill_details:
            bill_details[item_name]["qty"] += qty
            bill_details[item_name]["cost"] += cost 

    
        else:
            bill_details[item_name] = {
                "category" : food_obj.category,
                "qty" :qty ,
                "cost" : cost
            }
        grand_total += cost

    print("\n     --- CUSTOMER BILL ---")
    for name, data in bill_details.items():
        print(f"{name} (x{data['qty']}) - {data['category']} : Rs. {round(data['cost'], 2)}")
            
    print("Grand Total: Rs.", round(grand_total, 2))
    print("Note: Main Course has 5% GST, Beverage has Rs. 10 cooling charge per item.")

    return bill_details, grand_total

while True:
    print("\n---WELCOME TO THE RESTAURANT---")
    print("1. Show Menu")
    print("2. Take Order & generate bill " )
    print("3. Exit")
    
    choice = int(input("Enter your choice (1-3): "))
    
    if choice == 1:
        show_menu()
    elif choice == 2:
        current_order = take_order()
        generate_bill(current_order)
    elif choice == 3:
        print("Thank you! Exiting program.")
        break
    else:
        print("Invalid choice. Please enter 1, 2, or 3.")