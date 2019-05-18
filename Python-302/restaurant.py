

class Restaurant(object):
    
    def __init__(self, name, address):
        
        self.name = name
        self.address = address
        
class Category(object):
    
    def __init__(self, id, type):
        
        self.id = id
        self.type = type


class Food(object):
    
    def __init__(self, id, cat, name, price, quantity=None):
        
        self.id = id
        self.cat = cat
        self.name = name
        self.price = price
        self.quantity = quantity
        
        
    def getTotal(self):
        
        return self.price * self.quantity
    
    def setQuantity(self, quantity):
        
        self.quantity = quantity
    
    
class Customer(object):
    
    def __init__(self, id, name, phone, address):
        
        self.id = id
        self.name = name
        self.phone = phone
        self.address = address
        
class Order(object):
    
    def __init__(self, id, customer, food):
        
        self.id = id
        self.customer = customer
        self.food = food
        
        
class Payment(object):
    
    def __init__(self, id, order, bill, received):
        
        self.id = id
        self.order = order
        self.bill = bill
        self.received = received
        self.change = 0
    
    def getChange(self):
        
        return (self.received - self.bill)
    

class PayType(object):
    
    def __init__(self, flag):
        
        self.flag = flag
    
    def getFlag(self):
        
        return self.flag
    

r1 = Restaurant('KFC', 'Dhanmondi')
r2 = Restaurant('Gloria Jeans Coffee', 'Dhanmondi')
r3 = Restaurant('Pizza Hut', 'Gulshan')

restaurant = [r1, r2, r3]
    
c1 = Category('101', 'Beverage')
c2 = Category('102', 'Starter')
c3 = Category('103', 'Dish')
categories = [c1, c2, c3]


f1 = Food('201', '101', 'Tea', 10)
f2 = Food('202', '101', 'Coffee', 20)
f3 = Food('203', '101', 'Pepsi', 15)
f4 = Food('204', '102', 'Soup', 110)
f5 = Food('205', '102', 'Momo', 200)
f6 = Food('206', '102', 'French Fry', 60)
f7 = Food('207', '103', 'Rice', 120)
f8 = Food('208', '103', 'Nuddle', 160)
f9 = Food('209', '103', 'Pasta', 130)

foods = [f1, f2, f3, f4, f5, f6, f7, f8, f9]

foodD = {'201':f1, '202': f2, '203':f3, '204':f4, '205':f5, '206': f6, '207':f7, '208':f8, '209':f9}


cus1 = Customer('11', 'Rafsan', '01705571619', 'Mirpur')
cus2 = Customer('12', 'Nayeem', '01705571619', 'Mirpur')
customers = [cus1, cus2]
    
flag = True

while(flag):
    
    print("[1] Restaurant")
    print("[2] Exit")
    choice = int(input("Choose: "))
        
    if(choice == 1):
        
        for i in range(len(restaurant)):
            print("[" , i+1 ,"] ", restaurant[i].name, " " , restaurant[i].address)
            
        choice = int(input("Choose Restaurant: "))
        
        print(" -------------- ", restaurant[choice-1].name, " -------------- \n")
        print("------------------ Menu ------------------\n\n")
        
        for i in range(len(categories)):
            print("[" , categories[i].id ,"] ", categories[i].type)
            
        cat = int(input("Choose Category: "))
        
        
        for i in range(len(foods)):
            
            if(foods[i].cat == str(cat)):
            
                print("[" , foods[i].id ,"] ", foods[i].name, " ", foods[i].price)
            
        choice = int(input("Choose Food: "))
        
        food = foodD.get(str(choice))
        price = food.price
        quantity = int(input("Quantity: "))
        
        food.setQuantity(quantity)
        
        total = food.getTotal()
        print("Total: $", total)
        
        received = float(input("Received: "))
        order = Order('101', cus1, food)
        payment = Payment('101', order, total, received)
        change = payment.getChange()
        print("Change: $", change, "\n\n")
        
        print("------------------------------------\n\n")
        
    else:
        print("Thank You for Being with Us!")
        flag = False



