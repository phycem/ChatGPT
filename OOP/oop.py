import csv 



class Item:
    pay_rate = 0.8 #  class level, the pay rate after 20% discount
    all = []
    def __init__(self, name:str,price:float,quantity=0): # instance level
        #print(f"An instance created:{name}")

        #Run validations to the recieved arguments
        assert price >= 0, f"Price {price} is not greater than or equal to zero!" 
        assert quantity >= 0, f"Quantity {quantity} is not greater than or equal to 0 zero!"
        
        #Assign to self object 
        self.name = name
        self.price = price
        self.quantity = quantity
        
        #Actions to execute
        Item.all.append(self)

    def calculate_total_price(self):
        return self.price * self.quantity
    
    def apply_discount(self):
        self.price = self.price * self.pay_rate

    @classmethod
    def instantiate_from_csv(cls):
        with open( 'items.csv','r') as f:
            reader = csv.DictReader(f)
            items = list(reader)

        for item in items:
            print(item)
            Item(
                name=int(item.get('name')),
                price=float(item.get('price')),
                quantity=int(item.get('quantity'))
            )
        
    def __repr__(self):
        return f"Item('{self.name}', {self.price},{self.quantity})"
    
#print(item1.calculate_total_price(item1.price, item1.quantity))

#print(item2.calculate_total_price(item2.price, item2.quantity))

#print(Item.__dict__) # All the attributes for class level
#print(item1.__dict__) #All the attributes for instance level

item1 = Item("Phone", 100, 1)
item2 = Item("Laptop", 1000, 3)
item3 = Item("Cable", 10, 5)
item4 = Item("Mouse", 50, 5)
item5 = Item("Keyboard", 75, 5)


Item.instantiate_from_csv()
print(Item.all)
#for instance in Item.all:
#    print(instance.name)