class Customer():
    name = ""
    age = ""

    def addCart(self):
        print(self.name,"(",self.age,")","has added item to the cart")

customer1 = Customer()
customer1.name = "Anawat"
customer1.age = 23
customer1.addCart()

customer2 = Customer()
customer2.name ="Theethut"
customer2.age = 22
customer2.addCart()

customer3 = Customer()
customer3.name = "Beat"
customer3.age = 22
customer3.addCart()

customer4 = Customer()
customer4.name = "Junior"
customer4.age = 24
customer4.addCart()
