""" 
Observer Pattern

It's common for different components of an app to respond to events or state changes, but how can we communicate these events?
The Observer pattern is a popular solution. We have a Subject (aka Publisher) which will be the source of events. And we could have multiple Observers (aka Subscribers) which will recieve events from the Subject in realtime.


In software design and engineering, the observer pattern is a software design pattern in which an object, named the subject, maintains a list of its dependents, called observers, and notifies them automatically of any state changes, usually by calling one of their methods.
he observer pattern addresses the following problems:[2]

A one-to-many dependency between objects should be defined without making the objects tightly coupled.
When one object changes state, an open-ended number of dependent objects should be updated automatically.
An object can notify multiple other objects.

 """


class YouTubeChannel:
    def __init__(self, name):
        self.name = name
        self.subscribers = []

    def subscribe(self, sub):
        self.subscribers.append(sub)
    
    def notify(self, event):
        for sub in self.subscribers:
            sub.sendNotification(self.name, event)

from abc import ABC, abstractmethod

class YoutubeSubscriber(ABC):
    @abstractmethod
    def sendNotification(self, event):
        pass

class YoutubeUser(YoutubeSubscriber):
    def __init__(self, name):
        self.name = name

    def sendNotification(self, channel, event):
        print(f"User {self.name} received notification from {channel}: {event}")

channel = YouTubeChannel("sam's World")

channel.subscribe(YoutubeUser("sub1"))
channel.subscribe(YoutubeUser("sub2"))
channel.subscribe(YoutubeUser("sub3"))

channel.notify("A new video released")

""" In this case we have multiple Subscribers listening to a single published. But users could also be subscribed to multiple channels.
Since the Publishers & Subscribers don't have to worry about each others' implementations, they are loosely coupled.
 """


""" 
Iterator is a behavioral design pattern that lets you traverse elements of a collection without exposing its underlying representation (list, stack, tree, etc.).

https://refactoring.guru/design-patterns/iterator

Many objects in python have built-in iterators. That's why we can conveniently iterate through an array using the key word in.

myList = [1, 2, 3]
for n in myList:
    print(n)
Output
1 2 3
For more complex objects, like Linked Lists or Binary Search Trees, we can define our own iterators.


 """

class LinkedNode:
    def __init__(self, head):
        self.head = head
        self.next = None

class LinkedList:
    def __init__(self, head):
        self.head = head
        self.cur = None

    # Define Iterator
    def __init__(self):
        self.cur = self.head
        return self
    
    # Iterate
    def __next__(self):
        if self.cur:
            val = self.cur.val
            self.cur = self.cur.next
            return val
        else:
            raise StopIteration
        


# Initialize LinkedList
head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
myList = LinkedList(head)

# Iterate through LinkedList
for n in myList:
    print(n) 

""" Output

1 2 3
 """


""" 

Strategy Pattern

Strategy is a behavioral design pattern that lets you define a family of algorithms, put each of them into a separate class, and make their objects interchangeable.

https://refactoring.guru/design-patterns/strategy


In computer programming, the strategy pattern (also known as the policy pattern) is a behavioral software design pattern that enables selecting an algorithm at runtime. Instead of implementing a single algorithm directly, code receives runtime instructions as to which in a family of algorithms to use.[1]

A Class may have different behaviour, or invoke a different method based on something we define (i.e. a Strategy). For example, we can filter an array by removing positive values; or we could filter it by removing all odd values. These are two filtering strategies we could implement, but we could add many more.


 """

from abc import ABC, abstractmethod

class FilterStrategy(ABC):

    @abstractmethod
    def removeValue(self, val):
        pass

class RemoveNegativeStrategy(FilterStrategy):

    def removeValue(self, val):
        return val < 0
    
class RemoveOddStrategy(FilterStrategy):

    def removeValue(self, val):
        return abs(val) % 2


class Values():
    def __init__(self, vals):
        self.vals = vals

    def filter(self, strategy):
        res = []
        for n in self.vals:
            if not strategy.removeValue(n):
                res.append(n)
        return res
    

values = Values([-7, -4, -1, 0, 2, 6, 9])

print(values.filter(RemoveNegativeStrategy()))
print(values.filter(RemoveOddStrategy()))

""" Output

[0, 2, 6, 9] [-4, 0, 2, 6]
A common alternative to this pattern is to simply pass in an inline / lambda function, which allows us to extend the behaviour of a method or class. """




""" 
Command Design Pattern

The Command design pattern is a behavioral pattern that encapsulates a request or action as an object, allowing you to parameterize and queue requests. It enables you to decouple the requester of an action from the provider of the action.


 """

class Light:
    def on(self):
        print("Light is on")

    def off(self):
        print("Light is off")

class Command:
    def __init__(self, light):
        self.light = light

    def execute(self):
        pass

class TurnOnCommand(Command):
    def execute(self):
        self.light.on()

class TurnOffCommand(Command):
    def execute(self):
        self.light.off()

class RemoteControl:
    def __init__(self):
        self.commands = {}

    def set_command(self, command_name, command):
        self.commands[command_name] = command

    def execute_command(self, command_name):
        if command_name in self.commands:
            self.commands[command_name].execute()
        else:
            print("Invalid command")

# Usage:
light = Light()
remote = RemoteControl()

turn_on_cmd = TurnOnCommand(light)
turn_off_cmd = TurnOffCommand(light)

remote.set_command("on", turn_on_cmd)
remote.set_command("off", turn_off_cmd)

remote.execute_command("on")  # Output: Light is on
remote.execute_command("off")  # Output: Light is off


""" 



Template Method Design Pattern

The Template Method design pattern is a behavioral pattern that provides a way to define an algorithm's skeleton in a superclass but allows subclasses to override specific steps of the algorithm. It enables you to define a method that provides a way to perform an algorithm, but allows subclasses to customize certain steps of the algorithm.

 """

from abc import ABC, abstractmethod

class Game(ABC):
    def play(self):
        self.initialize()
        self.start_game()
        self.end_game()

    @abstractmethod
    def initialize(self):
        pass

    @abstractmethod
    def start_game(self):
        pass

    @abstractmethod
    def end_game(self):
        pass

class ChessGame(Game):
    def initialize(self):
        print("Setting up the chess board")

    def start_game(self):
        print("Starting the chess game")

    def end_game(self):
        print("Ending the chess game")

class SoccerGame(Game):
    def initialize(self):
        print("Setting up the soccer field")