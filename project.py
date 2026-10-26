# MODULE 1: Menu Management

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

    def calculate_price(self_,qty):
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
    "Chicken Biryani" : MainCourse(104 ,"Chicken Biryani", 200),
    "Coke" : Beverage(201 ,"Coke", 70),
    "Coffee" : Beverage(202 , "Coffee" , 100),
    "Tea" : Beverage(203, "Tea" , 50),
    "Brownie" : Dessert(301 , "Brownie", 120),
    "Gulab Jamun" : Dessert(302 , "Gulab Jamun" ,50)
}

def show_menu():
    print("\nAvailable Categories:",categories)
    print("-" * 48)
    print("ID | Item Name | Category | Base Price")
    print("_" * 48)
    for name , item in menu.items():
        print(f"{item.info[0]} | {item.info[1]:<16} | {item.category:<11} | Rs.{item.price}")
    print("-" * 48)
show_menu()