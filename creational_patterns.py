""" 
Factory Pattern

The factory pattern wraps a constructor for different types of objects and returns instances of the objects via a simple API. It makes it easy to create different objects by exposing a simple API that return the specified object type.

"Define an interface for creating an object, but let subclasses decide which class to instantiate. The Factory method lets a class defer instantiation it uses to subclasses.

"""

class Burger:
    def __init__(self, ingredients):
        self.ingredients = ingredients

    def print(self):
        print(self.ingredients)

class BurgerFactory:
    def createCheeseBurger(self):
        ingredients = ["bun", "cheese", "beef-patty"]
        return Burger(ingredients)
    
    def createDeluxeCheeseBurger(self):
        ingredients = ["bun", "tomatoe", "lettuce", "cheese", "beef-patty"]
        return Burger(ingredients)

    def createVeganBurger(self):
        ingredients = ["bun", "special-sauce", "veggie-patty"]
        return Burger(ingredients)

burgerFactory = BurgerFactory()
burgerFactory.createCheeseBurger().print()
burgerFactory.createDeluxeCheeseBurger().print()
burgerFactory.createVeganBurger().print()


""" 
Builder Pattern
Wikipedia says:

The builder pattern is a design pattern designed to provide a flexible solution to various object creation problems in object-oriented programming.

Refactoring Guru says:

Builder is a creational design pattern that lets you construct complex objects step by step. The pattern allows you to produce different types and representations of an object using the same construction code.

 """
class Burger:
    def __init__(self):
        self.buns = None
        self.patty = None
        self.cheese = None

    def setBuns(self, bunStyle):
        self.buns = bunStyle

    def setPatty(self, pattyStyle):
        self.patty = pattyStyle

    def setCheese(self, cheeseStyle):
        self.cheese = cheeseStyle

class BurgerBuilder:
    def __init__(self):
        self.burger = Burger()

    def addBuns(self, bunStyle):
        self.burger.setBuns(bunStyle)
        return self
    
    def addPatty(self, pattyStyle):
        self.burger.setPatty(pattyStyle)
        return self
    
    def addCheese(self, cheeseStyle):
        self.burger.setCheese(cheeseStyle)
        return self
    
    def build(self):
        return self.burger
burger = BurgerBuilder() \
            .addBuns("sesame") \
            .addPatty("fish-patty") \
            .addCheese("swiss cheese") \
            .build()


""" 
Singleton Pattern

Singleton is a design pattern that tells us that we can create only one instance of a class and that instance can be accessed globally.

This is one of the basic types of design pattern. It makes sure that the class acts as a single source of entry for all the consumer components that want to access this state. In other words, it provides a common entry point for using global state.

So a singleton class should be one which:

Ensures that it creates only one instance of the class
Provides a global access point to the state.
Makes sure that the instance is only created the first time.

 """

