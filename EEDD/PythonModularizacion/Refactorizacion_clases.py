class Store:
    def __init__(self, name):
        self.name = name
        self.products = []
        self.customers = []

class product:
    def add_product(self, product):
            self.products.append(product)

class customer:
    def add_customer(self, customer):
            self.customers.append(customer)

class products:
    def print_products(self):
            for product in self.products:
                print(product)

class customers:
    def print_customers(self):
            for customer in self.customers:
                print(customer)