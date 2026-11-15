# MODULE 1: Menu management

class FoodItem:
    def __init__(self , item_id, name, price, category):
        self.info = (item_id ,name)
        self.price = price
        self.category = category

    def calculate_price(self,qty):
        return self.price * qty


class Indian(FoodItem):
    def __init__(self, item_id, name,price):
        super().__init__(item_id , name ,price ,"Indian")

    def calculate_price(self,qty):
            return (self.price *qty) * 1.05

class Chinese(FoodItem):
    def __init__(self, item_id, name,price):
        super().__init__(item_id , name ,price ,"Chinese")

    def calculate_price(self,qty):
            return (self.price *qty) * 1.05

class Continental(FoodItem):
    def __init__(self, item_id, name,price):
        super().__init__(item_id , name ,price ,"Continental")

    def calculate_price(self,qty):
        return (self.price *qty) * 1.05

class ComboMeal(FoodItem):
    def __init__(self, item_id, name,price):
        super().__init__(item_id , name ,price ,"Combo Meal")

    def calculate_price(self,qty):
        return (self.price *qty) * 1.05


class Breads(FoodItem):
    def __init__(self, item_id, name,price):
        super().__init__(item_id , name ,price ,"Breads")
    
class Beverage(FoodItem):
    def __init__(self, item_id,name,price):
        super().__init__(item_id,name ,price, "Beverage")

    def calculate_price(self, qty):
        return (self.price + 10) *qty

class Dessert(FoodItem):
    def __init__(self,item_id, name , price):
        super().__init__(item_id, name, price , "Dessert")


categories = {"Indian", "Chinese", "Continental", "Breads","Combo Meal" , "Beverage", "Dessert"}
menu = {
    "Butter Chicken": Indian(101, "Butter Chicken", 350),
    "Butter Paneer": Indian(102, "Butter Paneer", 260),
    "Kadhai Paneer": Indian(103, "Kadhai Paneer", 250),
    "Dal Makhani": Indian(104, "Dal Makhani", 220),
    "Chicken Tikka Masala": Indian(105, "Chicken Tikka Masala", 360),
    "Hyderabadi Biryani": Indian(106, "Hyderabadi Biryani", 280),
    
    "Veg Hakka Noodles": Chinese(201, "Veg Hakka Noodles", 180),
    "Chicken Hakka Noodles": Chinese(202, "Chicken Hakka Noodles", 220),
    "Veg Manchurian": Chinese(203, "Veg Manchurian", 190),
    "Chilli Chicken": Chinese(204, "Chilli Chicken", 260),
    "Chilli Paneer": Chinese(205, "Chilli Paneer", 230),
    "Spring Rolls": Chinese(206, "Spring Rolls", 150),

    "White Sauce Pasta": Continental(301, "White Sauce Pasta", 240),
    "Red Sauce Pasta": Continental(302, "Red Sauce Pasta", 220),
    "Margherita Pizza": Continental(303, "Margherita Pizza", 280),
    "Farmhouse Pizza": Continental(304, "Farmhouse Pizza", 340),
    "Grilled Chicken Burger": Continental(305, "Grilled Chicken Burger", 190),

    "Tandoori Roti": Breads(401, "Tandoori Roti", 25),
    "Butter Naan": Breads(402, "Butter Naan", 50),
    "Garlic Naan": Breads(403, "Garlic Naan", 70),
    "Lachha Paratha": Breads(404, "Lachha Paratha", 60),

    "Coke": Beverage(501, "Coke", 60),
    "Cold Coffee": Beverage(502, "Cold Coffee", 120),
    "Fresh Lime Soda": Beverage(503, "Fresh Lime Soda", 80),
    "Masala Chai": Beverage(504, "Masala Chai", 40),

    "Chocolate Brownie": Dessert(601, "Chocolate Brownie", 130),
    "Gulab Jamun": Dessert(602, "Gulab Jamun", 60),
    "Rasmalai": Dessert(603, "Rasmalai", 90),

    "North Indian Thali": ComboMeal(701, "North Indian Thali", 320),
    "Chinese Feast Combo": ComboMeal(702, "Chinese Feast Combo", 290),
    "Student Burger Meal": ComboMeal(703, "Student Burger Meal", 240)
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

    while True:
        try:
            item_name = input("\nEnter food item name or ID (or 'done' to finish): ").strip().title()

            if item_name.lower() == "done":
                break

            if item_name.isdigit():
                search_id = int(item_name)
                for name, item in menu.items():
                    if item.info[0] == search_id:
                        item_name = name
                        break

            if item_name not in menu:
                raise KeyError(f"'{item_name}' is not available on the menu.")

            qty = int(input(f"Enter quantity for {item_name}: "))
            if qty <= 0:
                raise ValueError("Quantity must be at least 1.")

            order_list.append((item_name, qty))
            print(f"Added: {qty} x {item_name}")

        except KeyError as error:
            print(f"Item Error: {error}")
        except ValueError as error:
            print(f"Quantity Error: {error}")

    return order_list

def generate_bill(order_list):
    if not order_list:
        print("\nNo items ordered.")
        return None, 0

    bill_details = {}
    grand_total = 0.0

    for item_name, qty in order_list:
        food_obj = menu[item_name]
        cost = food_obj.calculate_price(qty)

        if item_name in bill_details:
            bill_details[item_name]["qty"] += qty
            bill_details[item_name]["cost"] += cost
        else:
            bill_details[item_name] = {
                "category": food_obj.category,
                "qty": qty,
                "cost": cost
            }
        grand_total += cost

    discount = 0.0
    coupon = input("\nEnter coupon code (or press Enter to skip): ").strip().upper()
    if coupon == "GEU20":
        student_id = input("Enter your University Student ID: ").strip()
        if student_id.isdigit() and len(student_id) >= 5:
            discount = grand_total * 0.20
            grand_total -= discount
            print(f"Student ID verified! 20% discount (Rs. {round(discount, 2)}) applied.")
        else:
            print("Invalid Student ID! Discount not applied.")
    elif coupon != "":
        print("Invalid coupon code! Discount not applied.")

    print("\n     --- CUSTOMER BILL ---")
    for name, data in bill_details.items():
        print(f"{name} (x{data['qty']}) - {data['category']} : Rs. {round(data['cost'], 2)}")

    if discount > 0:
        print("Student Discount (GEU20 - 20% Off): - Rs.", round(discount, 2))

    print("Grand Total: Rs.", round(grand_total, 2))
    print("Note: Indian/Chinese/Continental/Combos have 5% GST, Beverage has Rs. 10 cooling charge.")

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

#phase 3 :

