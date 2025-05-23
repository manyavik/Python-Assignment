import math

# 1: Prime Number Generator (find_primes)
def find_primes(x, y):
    primes = []
    for num in range(min(x, y), max(x, y) + 1):
        if is_prime(num):
            primes.append(num)
    return primes
    
def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(math.sqrt(num)) + 1): #the factor of n would be less than sqrt(n)
        if num % i == 0:
            return False
    return True

print(find_primes(10, 30))

# 2: Number to Words Converter

def toWord(x):
    ones = ["","one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    teens = ["ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]
    tens = ["", "", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]
    if (x == 0):
        word = "zero"
    if (x > 0 and x < 10):
        word = ones[x]
    if (x > 9 and x < 20):
        word = teens[x - 10]
    if (x>=20 and x<=99):
        onesVal = int(x % 10)
        tensVal = int((x - onesVal)/10)
        word = tens[tensVal] + "-" + ones[onesVal]
    if (x>=100 and x<=999):
        onesVal = int(x%10)
        tensVal = int(((x-onesVal)/10)%10)
        hundredsVal = int(x / 100)
        word = ones[hundredsVal] + " hundred " + tens[tensVal] + "-" + ones[onesVal]
    return word

print(toWord(999))

# 3: Tic-Tac-Toe Board Printer

def print_board(board=None):
    if board == None:
        # make empty nested list for empty board
        board = [[" " for _ in range(3)] for _ in range(3)]
    for row in board:
        print(" | ".join(str(cell) for cell in row))
        print("-" * 9)

#example board:
board = [
    [" ", 'X', " "],
    ['O', " ", " "],
    [" ", " ", 'X']
]

print_board()

#5: Anagram Checker
def isAnagram(x, y):
    return sorted(x.lower()) == sorted(y.lower())

#6: Password Strength Checker
import string
def isStrong(password):
    lower = any(char.islower() for char in password)
    upper = any(char.isupper() for char in password)
    digit = any(char.isdigit() for char in password)
    special = any(char in string.punctuation for char in password)

    return upper and lower and digit and special

#7: Longest Word Finder
def longestWord(sentence):
    longest = ""
    words = sentence.split()
    for word in words:
        if len(word) > len(longest):
            longest = word
    return longest

#8: List Flatteninig
def flatten(nestedList):
    newList = []
    for i in nestedList:
        if isinstance(i, list): #check if i is list object
            newList.extend(flatten(i))
        else:
            newList.append(i)
    return newList

#9: Frequency Counter
def wordFrequency(paragraph):
    words = paragraph.split()
    dict = {}
    for word in words:
        word = word.lower()
        if word in dict:
            dict[word] += 1
        else:
            dict[word] = 1
    return dict

#10: Character Counter
def countCharacter(word):
    dict = {}
    for i in word:
        if i == " ":
            continue
        if i in dict:
            dict[i] += 1
        else:
            dict[i] = 1
    return dict

#11: Student Gradebook
def lookupStudentMarks():
    grades = {
        "Manya": 90,
        "Jack": 80,
        "Bob": 100
    }

    name = input("Enter a student's name ")

    if name in grades:
        print(grades[name])
    else:
        print("Student doesn't exist")


#12: Read and Count Words
def getStats(fileName):
    with open(fileName, 'r') as file:
        lines = file.readlines()
        linecount = len(lines)
        wordcount = sum(len(line.split()) for line in lines)
        charcount = sum(len(line) for line in lines)

#13: Simple Log Writer
from datetime import datetime

def writeLog(message, fileName="file.txt"):
    with open(fileName, "a") as file:
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M")
        file.write(timestamp + " " + message + '\n') #f"[{timestamp}] {message}\n"

#14: CSV Reader
import csv

def readMarks(fileName):
    with open(fileName, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            mark = float(row("marks")) #assuming column named "marks"
            if mark > 75:
                print(row["name"] + ": " + mark) #assuming column named "name"

#15: Bank Account Simulation
class Bank:
    def __init__(self):
        self.balance = 0
    
    def deposit(self, amount):
        self.balance += amount
    
    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
        else:
            print("Insufficient funds.")
    
    def getBalance(self):
        return self.balance

#16: Library Management System
class Book:
    def __init__(self, title, isAvailable=True):
        self.title = title
        self.isAvailable = isAvailable

class Library:
    def __init__(self, books):
        self.books = books
    
    def borrow(self, title):
        for book in self.books:
            if(book.title == title):
                if (book.isAvailable):
                    book.isAvailable = False
                    print("You borrowed " + book.title)
                    return
                else:
                    print("Book is not available.")
                    return
        print("We don't carry that book.")

    def returnBook(self, title):
        for book in self.books:
            if book.title == title:
                if book.isAvailable == False:
                    book.isAvailable = True
                    print("Book returned!")
                    return
#17: Employee Management
class Employee:
    def __init__(self, name, age):
        self.name = name
        self.age = age

class Department:
    def __init__(self, title, employees):
        self.title = title
        self.employees = employees
    def findEmployee(self, name):
        for employee in self.employees:
            if employee.name == name:
                print(name + " is in this department.")
                print("Their age is " + str(employee.age) + ".")
                return
        print("This employee doesn't exist in this department.")

#18: Simple Quiz App
def multipleChoice():
    questions = {"What color is a tomato?": ["a) Orange", "b) yellow", "c) red"],
         "What planet are we on?": ["a) Earth", "b) Venus", "c) Mercury"]
    }

    correct = {
        "What color is a tomato?": "c",
        "What planet are we on?": "a"
    }

    for question, options in questions.items():
        print("\n" + question)
        for option in options:
            print(option)
        userAnswer = input("Answer: ").lower()
        if userAnswer == correct[question]:
            print("Correct!")
        else:
            print("WRONG")
    
    print("strating quiz")
    multipleChoice()

#19: Expense Tracker
def expenseTracker():
    expenses = {}
    for i in range(7):
        day = input("Enter the day: ")
        amount = float(input("How much expense today? "))
        expenses[day] = amount
    print("Weekly Summary:")
    for day, amount in expenses.items():
        print(day + ": $" + str(amount))

#20: To-Do App
#def todoApp(fileName="list.txt"):