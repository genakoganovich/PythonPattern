# Define the base object
class Pizza:
    def __init__(self):
        self.description = "Plain pizza"

    def get_cost(self):
        return 10.00

    def get_description(self):
        return self.description


# Define the decorator objects
class Cheese(Pizza):
    def __init__(self, pizza):
        self.pizza = pizza
        self.description = pizza.get_description() + ", with cheese"

    def get_cost(self):
        return self.pizza.get_cost() + 1.50


class Pepperoni(Pizza):
    def __init__(self, pizza):
        self.pizza = pizza
        self.description = pizza.get_description() + ", with pepperoni"

    def get_cost(self):
        return self.pizza.get_cost() + 2.00


# Create a plain pizza object
pizza = Pizza()

# Add decorators to the pizza object
pizza = Cheese(pizza)
pizza = Pepperoni(pizza)

# Print the final description and cost of the pizza
print(pizza.get_description())
print("Cost: $", pizza.get_cost())
