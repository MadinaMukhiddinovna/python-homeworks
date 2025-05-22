#1Circle Class
import math
class Circle:
    def __init__(self, radius):
        self.radius = radius  # radius of the circle
    def area(self):
        # Calculate area of the circle: π * r^2
        return math.pi * (self.radius ** 2)

    def perimeter(self):
        # Calculate perimeter (circumference): 2 * π * r
        return 2 * math.pi * self.radius
#example
c = Circle(5)
print("Area:", c.area())
print("Perimeter:", c.perimeter())

#Person Class
            from datetime import datetime
class Person:
    def __init__(self, name, country, birth_date):
        self.name = name
        self.country = country
        self.birth_date = datetime.strptime(birth_date, "%Y-%m-%d")

    def get_age(self):
        # Calculate age in years from birth_date till today
        today = datetime.today()
        age = today.year - self.birth_date.year - ((today.month, today.day) < (self.birth_date.month, self.birth_date.day))
        return age
#example
p = Person("Alice", "USA", "1990-04-25")
print(f"{p.name} is {p.get_age()} years old.")

#3. Calculator Classclass Calculator:
    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

    def multiply(self, a, b):
        return a * b

    def divide(self, a, b):
        if b == 0:
            raise ValueError("Cannot divide by zero")
        return a / b
#example
calc = Calculator()
print("Add:", calc.add(10, 5))
print("Divide:", calc.divide(10, 2))

#4Shape and Subclasses
import math
class Shape:
    def area(self):
        pass

    def perimeter(self):
        pass
      
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    def area(self):
        return math.pi * self.radius ** 2

    def perimeter(self):
        return 2 * math.pi * self.radius
class Square(Shape):
    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side ** 2

    def perimeter(self):
        return 4 * self.side
class Triangle(Shape):
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def perimeter(self):
        return self.a + self.b + self.c

    def area(self):
        # Heron's formula
        s = self.perimeter() / 2
        return math.sqrt(s * (s - self.a) * (s - self.b) * (s - self.c))
#example
shapes = [Circle(3), Square(4), Triangle(3, 4, 5)]
for shape in shapes:
    print(f"Area: {shape.area()}, Perimeter: {shape.perimeter()}")
  
#5 Binary Search Tree Class
class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        if not self.root:
            self.root = Node(value)
        else:
            self._insert_recursive(self.root, value)

    def _insert_recursive(self, current, value):
        if value < current.value:
            if current.left:
                self._insert_recursive(current.left, value)
            else:
                current.left = Node(value)
        else:
            if current.right:
                self._insert_recursive(current.right, value)
            else:
                current.right = Node(value)

    def search(self, value):
        return self._search_recursive(self.root, value)

    def _search_recursive(self, current, value):
        if not current:
            return False
        if value == current.value:
            return True
        elif value < current.value:
            return self._search_recursive(current.left, value)
        else:
            return self._search_recursive(current.right, value)
#example
bst = BinarySearchTree()
bst.insert(10)
bst.insert(5)
bst.insert(15)
print("Search 5:", bst.search(5))
print("Search 20:", bst.search(20))

#6 Stack Data Structure
class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)  # Add item to stack

    def pop(self):
        if not self.items:
            return None  # Or raise exception
        return self.items.pop()  # Remove and return last item
#example usage
stack = Stack()
stack.push(1)
stack.push(2)
print(stack.pop())  # Output: 2
print(stack.pop())  # Output: 1

#7 linked List Data Structure
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def display(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")
    def insert(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node

    def delete(self, key):
        current = self.head
        prev = None
        while current and current.data != key:
            prev = current
            current = current.next
        if not current:
            return  # Key not found
        if not prev:
            self.head = current.next
        else:
            prev.next = current.next
#example usage
ll = LinkedList()
ll.insert(1)
ll.insert(2)
ll.insert(3)
ll.display()  # Output: 1 -> 2 -> 3 -> None
ll.delete(2)
ll.display()  # Output: 1 -> None -> 3 -> None 

#8 Shopping Cart Class
class ShoppingCart:
    def __init__(self):
        self.items = {}

    def add_item(self, item, price, quantity=1):
        if item in self.items:
            self.items[item]['quantity'] += quantity
        else:
            self.items[item] = {'price': price, 'quantity': quantity}

    def remove_item(self, item, quantity=1):
        if item in self.items:
            self.items[item]['quantity'] -= quantity
            if self.items[item]['quantity'] <= 0:
                del self.items[item]

    def total_price(self):
        total = 0
        for item in self.items.values():
            total += item['price'] * item['quantity']
        return total
#example
cart = ShoppingCart()
cart.add_item("Apple", 1.5, 3)
cart.add_item("Banana", 2, 2)
print("Total price:", cart.total_price())
cart.remove_item("Apple", 1)
print("Total price after removal:", cart.total_price())

#9 Stack with Display
class StackWithDisplay:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.items:
            return None
        return self.items.pop()

    def display(self):
        print("Stack contents:", self.items)
#example
stack = StackWithDisplay()
stack.push(10)
stack.push(20)
stack.display()
stack.pop()
stack.display()

##10. Queue Data Structure

class Queue:
    def __init__(self):
        self.items = []

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        if not self.items:
            return None
        return self.items.pop(0)
#example
q = Queue()
q.enqueue(1)
q.enqueue(2)
print(q.dequeue())  # Output: 1
print(q.dequeue())  # Output: 2

#11 Bank Class

class Bank:
    def __init__(self):
        self.customers = {}  # key: customer name, value: balance
    def add_customer(self, name, initial_deposit=0):
        self.customers[name] = initial_deposit
    def deposit(self, name, amount):
        if name in self.customers:
            self.customers[name] += amount
        else:
            print("Customer not found")
    def withdraw(self, name, amount):
        if name in self.customers:
            if self.customers[name] >= amount:
                self.customers[name] -= amount
            else:
                print("Insufficient funds")
        else:
            print("Customer not found")
    def get_balance(self, name):
        return self.customers.get(name, "Customer not found")
#example
bank = Bank()
bank.add_customer("John", 1000)
bank.deposit("John", 500)
bank.withdraw("John", 300)
print("John's balance:", bank.get_balance("John"))
