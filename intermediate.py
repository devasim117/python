# ------------------------------------------------ Comprehensions

arr = [1,4,5,6,3,4,0,3,1]

# 1 List
# for y in [x*x for x in arr]:
#     print(f"{y}")

# for y in [x*x for x in arr if x%2==0]:
#     print(f"{y}")


# 2 Dictionaries
squar_dict = {x:x*x for x in range(10)}
# squar_dict={}
# for x in range(10):
#     squar_dict[x] = x*x
# print(squar_dict)

# 3 Set 
sq_set = {x*x for x in range(10)}

# 4 Generator
# Uses parentheses (). It does not build the whole list in memory at once. Instead, it yields items one by one on demand, making it highly memory-efficient for huge datasets
sq_gen = (x for x in [77,6,98,8,7])
# print(sq_gen)

# print(next(sq_gen))
# print(next(sq_gen))

# ----------------------------------------------------------- Iterator
# fruits = ["apple", "banana"]

# fruits_iterator = iter(fruits)

# print(fruits_iterator)
# print(next(fruits_iterator))
# print(next(fruits_iterator))
# print(next(fruits_iterator))

# ------------------------------------------------------------ Generator yield/yield from
def getValueFromGen(arr):
    # for x in arr:
    #     yield x
    yield from arr


getValueFromArr = getValueFromGen(arr)
# for item in arr:
#     print(next(getValueFromArr))

# ------------------------------------------------------------ Decorators
from functools import wraps

def demoDecorators(func):
    @wraps(func)
    def wrapper(*args,**kargs):
        print("Wrapper starting")
        func(*args, **kargs)
        print("Wrapper closed")
    return wrapper

@demoDecorators
def sayHello(name):
    print(f"Hello {name}")

# sayHello("Asim")

# ----------------------------------------------------------- Context
# ===> with class
class FileManager:
    def __init__(self, filename, mode):
        self.filename = filename
        self.mode = mode
        self.file = None

    def __enter__(self):
        self.file = open(self.filename, self.mode)
        return self.file

    def __exit__(self, exc_type, exc, tb):
        if self.file:
            self.file.close()
        return False

# with FileManager("test.txt","w") as f:
    # f.write("Hello, World")


# ===> with generator and decorator
from contextlib import contextmanager

@contextmanager
def writeFile(filename, mode):
    f = open(filename, mode)
    try:
        yield f
    finally:
        f.close()

# with writeFile("test.txt", "w") as f:
#     f.write("Testing with decorator")
#     f.close()


# ------------------------------------------------------- Dataclass
from dataclasses import dataclass, field

@dataclass
class Car:
    id: int
    name: str
    fuelType: str

# @dataclass(frozen=True)
@dataclass()
class Nexa(Car):
    items: list[str] = field(default_factory=list)
    totalCars: int = field(init=False)

    def __post_init__(self):
        self.totalCars = self.items.__len__()


# sedan = Nexa(1,"Sedan", "Petrol", ["Baleno","Fronx"])
# print(sedan)    

# -------------------------------- Enum
from enum import Enum

class OrderStatus(Enum):
    PENDING = "pending"
    PROCESSING = "processing"
    DONE = "done"

status = OrderStatus.PENDING

# print(status)
# print(status.name)
# print(status.value)


# ------------------------------------------- Collections
# 1. Counter (The Counter)Counter is a dictionary subclass specifically designed for counting hashable objects. It automatically maps elements to their respective counts.Best For: Tallying items, finding frequencies, or detecting duplicates.Key Feature: Does not throw a KeyError for missing items; it simply returns 0.python
from collections import Counter

# Create a counter from an iterable
words = ["apple", "banana", "apple", "cherry", "banana", "apple"]
word_counts = Counter(words)

# print(word_counts)  # Output: Counter({'apple': 3, 'banana': 2, 'cherry': 1})
# print(word_counts["mango"])  # Output: 0 (No KeyError!)

# # Find the most common elements
# print(word_counts.most_common(2))  # Output: [('apple', 3), ('banana', 2)]



# 2. defaultdict (The Default Dictionary)defaultdict is a dictionary subclass that calls a factory function (like list, set, or int) to supply a default value when a requested key does not exist.Best For: Grouping data or building nested collections without writing manual if key not in dict: checks.Key 
# Feature: Automatically initializes missing keys on the fly.python
from collections import defaultdict

# Grouping names by their starting letter using a list factory
names = ["Alice", "Bob", "Charlie", "Anna"]
grouped_names = defaultdict(list)

for name in names:
    first_letter = name[0]
    grouped_names[first_letter].append(name)  # Automatically creates [] if letter is missing

print(grouped_names)  # Output: defaultdict(<class 'list'>, {'A': ['Alice', 'Anna'], 'B': ['Bob'], 'C': ['Charlie']})


# 3. deque (The Double-Ended Queue)deque (pronounced "deck") is a list-like container designed for fast, O(1) insertions and removals from both the front and back ends. Standard Python lists take O(n) time to insert/delete items at the beginning.
# Best For: Storing recent history, implementing queues/stacks, or maintaining a sliding window.Key 
# Feature: Can specify a maximum size (maxlen) to automatically drop old items when new ones arrive.python
from collections import deque

# Create a queue with a maximum capacity of 3
recent_actions = deque(maxlen=3)

recent_actions.append("login")
recent_actions.append("click_home")
recent_actions.append("view_item")
print(recent_actions)  # Output: deque(['login', 'click_home', 'view_item'], maxlen=3)

# Adding a 4th item forces the oldest item ('login') out automatically
recent_actions.append("checkout")
print(recent_actions)  # Output: deque(['click_home', 'view_item', 'checkout'], maxlen=3)

# Fast append/pop from left side
recent_actions.appendleft("admin_override")
print(recent_actions.popleft())  # Output: 'admin_override'


# 4. namedtuple (The Readable Tuple)namedtuple creates tuple subclasses with named fields. It gives you the lightweight, immutable nature of a regular tuple, but lets you access data using dot-notation (obj.field) instead of rigid index positions (obj[0]).
# Best For: Clean, lightweight, read-only data structures.Key Feature: Zero performance overhead compared to regular tuples.Note: If you need default values, mutability, or advanced validation, use the @dataclass decorator instead.python
from collections import namedtuple

# Define the structure/blueprint
Point = namedtuple("Point", ["x", "y"])

# Instantiate the object
pt = Point(x=10, y=20)

print(pt.x)  # Output: 10
print(pt[1])  # Output: 20 (Still accessible via index!)


# --------------------------------------------------------- itertools
# 1. product (The Cartesian Product)product() computes the Cartesian product of input iterables. It is the direct equivalent of nesting multiple for loops inside each other, but condensed into a single clean line.Best For: Finding every possible combination between separate lists or repeating a sequence against itself.Key Feature: Accepts a repeat argument to find the product of an iterable with itself.python
from itertools import product

# Combining two separate lists
colors = ["Red", "Blue"]
sizes = ["S", "M"]
grid = list(product(colors, sizes))
print(grid)
# Output: [('Red', 'S'), ('Red', 'M'), ('Blue', 'S'), ('Blue', 'M')]

# Simulating two coin flips (repeating a sequence)
coin_flips = list(product(["H", "T"], repeat=2))
print(coin_flips)
# Output: [('H', 'H'), ('H', 'T'), ('T', 'H'), ('T', 'T')]


# 2. permutations (Order Matters)permutations() returns all possible arrangements of an iterable for a given length. In permutations, the order of elements matters—so (A, B) and (B, A) are treated as completely different outcomes.
# Best For: Rearranging elements, routing problems, or scheduling tasks.Key Feature: Does not pair an element with itself unless that element appears twice in the input collection.python
from itertools import permutations

letters = ["A", "B", "C"]

# All unique orderings of length 2
perms = list(permutations(letters, 2))
print(perms)
# Output: [('A', 'B'), ('A', 'C'), ('B', 'A'), ('B', 'C'), ('C', 'A'), ('C', 'B')]
# Notice that ('A', 'B') and ('B', 'A') are both included.

# 3. combinations (Order Does Not Matter)combinations() returns all possible subsets of an iterable for a given length. Unlike permutations, order does not matter—so if (A, B) is picked, (B, A) is discarded as a duplicate combination.
# Best For: Creating match ups, grouping items, or selecting items where sequence is irrelevant.Key Feature: Elements are treated as unique based on their position index, not their actual value.python
from itertools import combinations

players = ["Alice", "Bob", "Charlie"]

# All unique pairings for a match
pairings = list(combinations(players, 2))
print(pairings)
# Output: [('Alice', 'Bob'), ('Alice', 'Charlie'), ('Bob', 'Charlie')]
# Notice that ('Bob', 'Alice') is excluded because Alice & Bob are already paired.


# 4. cycle (The Infinite Loop)cycle() takes an iterable and repeats its elements indefinitely. When the end of the iterable is reached, it jumps straight back to the first item.
# Best For: Round-robin task scheduling, alternating game turns, or creating repeating UI loading sequences.Key Feature: Runs forever. You must use a break condition or a tracking counter to stop it.python

from itertools import cycle

turns = cycle(["Player 1", "Player 2"])

# Simulate the first 4 turns of a game
for _ in range(4):
    current_player = next(turns)
    print(f"It is {current_player}'s turn.")

# Output:
# It is Player 1's turn.
# It is Player 2's turn.
# It is Player 1's turn.
# It is Player 2's turn.


# ----------------------------------------------------------------- functiontools
# 1. lru_cache (The Performance Booster)lru_cache (Least Recently Used Cache) is a decorator that memorizes a function's results based on the arguments you pass to it. If the function is called again with the same arguments, it skips execution and instantly returns the cached result.
# Best For: Optimizing recursive algorithms, heavy math computations, or slow, repetitive database/API reads.Key Feature: You can limit the cache size using maxsize to manage memory footprint.python

from functools import lru_cache
import time

# maxsize=None allows the cache to grow without bound
@lru_cache(maxsize=128)
def heavy_calculation(n):
    time.sleep(1)  # Simulate a slow network or CPU task
    return n * 2

# First execution takes 1 second
print(heavy_calculation(10)) 

# Second execution is instantaneous because the result is cached!
print(heavy_calculation(10)) 

# Clear the cache manually if data changes
heavy_calculation.cache_clear()


# 2. partial (The Function Customizer)partial() lets you take an existing function and freeze or pre-fill some of its arguments, returning a new, simpler function callable.Best For: Simplifying callback handlers, reusing complex configuration functions, or adapting functions to fit APIs that expect fewer parameters.Key Feature: Works seamlessly with both positional arguments (*args) and keyword arguments (**kwargs).python

from functools import partial

def send_email(smtp_server, sender, recipient, subject, body):
    print(f"Sending via {smtp_server} from {sender} to {recipient}: {subject}")

# Freeze the infrastructure parameters (server and sender)
send_system_alert = partial(
    send_email, 
    smtp_server="://company.com", 
    sender="system@company.com"
)

# Use the customized function by only providing the missing unique fields
send_system_alert(recipient="admin@company.com", subject="Disk Full", body="Clear logs!")


# 3. reduce (The Sequence Aggregator)reduce() applies a function of two arguments cumulatively to the items of an iterable, from left to right, to reduce the sequence down to a single total value.
# Best For: Performing running calculations across an entire collection where each step depends on the previous outcome.Key Feature: Always provide the optional initializer third argument to prevent exceptions on empty lists.python

from functools import reduce

numbers = [1, 2, 3, 4, 5]

# Example: Compute the running product (factorial) of a list
# Step 1: 1 * 2 = 2
# Step 2: 2 * 3 = 6
# Step 3: 6 * 4 = 24...
product = reduce(lambda x, y: x * y, numbers)
print(product)  # Output: 120

# Safe usage with an initializer (starts the accumulation loop at 0)
total_sum = reduce(lambda x, y: x + y, numbers, 0)
print(total_sum)  # Output: 15
# Note: For simple addition or multiplication, prioritize built-in functions like sum() or math.prod() over reduce() for optimal readability.Functionality MatrixToolInputPrimary BenefitCommon Counterpartlru_cacheAny pure functionAvoids recalculating identical computations [1]Manual dictionary cachingpartialMulti-argument functionCreates specialized, simpler variants [1]Custom lambda wrappersreduceFunction + ListDistills a sequence down to a single entity [1]Standard for loop accumulator


# -------------------------------------------------------------------- Type hint
# Breaking Down Your Syntaxa: int and b: int: These specify that both input parameters must be integers.-> int: This specifies that the function will return an integer value.python
def add(a: int, b: int) -> int:
    return a + b

# Key Rules of Python Type Hinting
# 1. Type Hints Do Not Enforce Anything at RuntimePython is a dynamically typed language. If you pass strings into your function, it will still execute and concatenate them instead of crashing.python
# # Python will still run this and return "510" without raising an error!
add("5", "10") 
# To catch these mistakes, you must run a static type checker like Mypy or Pyright in your terminal or IDE.2. Handling Multiple Allowed Types (Union or |)If your function can accept or return more than one type (e.g., both integers and floats), use the pipe operator | (Python 3.10+).python# Accepts integers or floats, and returns an integer or float

def add_flexible(a: int | float, b: int | float) -> int | float:
    return a + b

# 3. Handling Optional Values (None)If an argument can either be a specific type or None, explicitly label it as optional.python# Python 3.10+ syntax
def greet(name: str | None = None) -> str:
    if name is None:
        return "Hello, Guest!"
    return f"Hello, {name}!"
# Advanced Typing Tools to KnowAs your application grows, you will need to type hint more complex structures using the built-in typing ecosystem.Collections: list[int], dict[str, float], set[str]Any: Use Any when a variable can be absolutely anything (turns off type checking for that variable).Callable: Use this when a function accepts another function as an argument (like the decorators we discussed).


# ---------------------Typing examples
# 1. Union (Multiple Allowed Types)Union specifies that a variable or argument can accept more than one specific type.Modern Syntax (Python 3.10+): Use the pipe operator (|). It replaces the old, wordy Union[int, float] import.python# Accepts either an int or a float, and returns either an int or a float
def process_payment(amount: int | float) -> int | float:
    return amount * 1.05

# 2. Optional (Type or None)Optional means a value can either be a specific type or it can be None. It is structurally identical to a Union containing None.Modern Syntax (Python 3.10+): Use Type | None instead of importing Optional.python# The argument defaults to None if not provided
def fetch_user_profile(user_id: int, auth_token: str | None = None) -> dict:
    if auth_token is None:
        print("Fetching public profile only.")
    return {"id": user_id}

# 3. Any (Turn Off Type Checking)Any is a wildcard. It matches absolutely any type. When you use Any, the type checker completely stops analyzing that variable, allowing any operation on it.Best For: Migrating old legacy code, handling completely unpredictable data (like raw JSON from a chaotic API), or fallback scenarios.Warning: Use it sparingly; overusing Any defeats the whole purpose of static type checking.from typing import Any
def log_debug_info(data: Any) -> None:
    # The type checker will not flag an error no matter what methods we call here
    print(f"Type: {type(data)}, Value: {data}")

# 4. Literal (Restricting to Specific Exact Values)Literal allows you to restrict a variable not just to a broad data type (like str), but to specific, exact, hardcoded values.Best For: Restricting mode flags, configuration strings, or specific HTTP methods.vs Enum: Use Literal for simple, lightweight inline string restrictions. Use Enum if you need to attach extra behavior or loop through options.python
from typing import Literal

# This function strictly rejects any string other than "r", "w", or "a"
def open_connection(mode: Literal["r", "w", "a"]) -> None:
    print(f"Connection opened in {mode} mode.")

open_connection("r")       # Valid
# open_connection("delete") <-- Mypy/Pyright type checkers will flag this as a bug!

# 5. TypedDict (Fixed-Key Dictionaries)A standard Python dictionary (dict[str, int]) assumes every single key matches that type. TypedDict allows you to specify exact type hints for individual, named keys in a dictionary.Best For: Validating fixed shapes of dictionary configurations or JSON objects where you do not want to incur the overhead of writing a full object class or dataclass.python
from typing import TypedDict

# Define the precise schema/blueprint of your dictionary
class UserPayload(TypedDict):
    username: str
    age: int
    is_premium: bool

# Usage
new_user: UserPayload = {
    "username": "coder123",
    "age": 28,
    "is_premium": False
}
# Tip: By default, all keys in a TypedDict are mandatory. If you want some keys to be optional without throwing a type error, you can pass total=False to the class declaration (e.g., class UserPayload(TypedDict, total=False):).


# Typing Cheat Sheet
# Tool      Core Use Case                                       Modern Python 3.10+ Alternative
# Union     Value can be Type A or Type B                       TypeA | TypeB
# Optional  Value can be Type A or None                         TypeA | None
# Any       Wildcard escape hatch (stops checking)              None (Use sparingly)
# Literal   Restricts to specific static string/int choices     Literal["option1", "option2"]
# TypedDict Declares structured schemas for dictionary keys     from typing import TypedDict