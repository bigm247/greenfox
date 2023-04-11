#variable base_number with value 123
base_number = 123
#function called double_number that doubles it's input parameter and returns the doubled value
def double_number(num):
   return num * 2
print(double_number(base_number))

#creating a variable al with value green fox
al = "greenfox"
#define greet function
def greet(name):
   print("Greetings dear greenfox", name)
#call greet function to greet al
greet(al)

#assign a value churchil to variable called typo
typo = "churchill"
#define append_a function
def append_a(string):
#appends an 'a' character to its end and returns with a string
    return string + "a"
print(append_a(typo))

#write function called sum that returns the sum of numbers from zero to the given parameter
def sum(n):
   #sum of number from giving paremeters
   sum = 0
   for i in range (n+1):
    sum +=i
   return sum
print(sum(10))

# create a function called calculatefactorial() that retuns the factorial of its input
def fact(n):
   factorialvalue = 1
   for i in range (1, n+1):
    factorialvalue *= i
    return factorialvalue
   
#Create a function called print_params which prints the input parameters (can have multiple number of arguments)
def print_params(*args):
   for arg in args:
    print(arg)

#function of matching indexes
    def find_matching_indexes( number, listofnumbers):
     arrayofindexes = []
     for i in range(len(listofnumbers)):
        if str(number) in str(listofnumbers[i]):
             arrayofindexes.append(i)
     return arrayofindexes
    print(find_matching_indexes(1, [1, 11, 34, 52, 61]))
    
# function for find Unique_number
def unique(arr):
    unique_numbers = []
    for num in arr:
        if arr.count(num) == 1:
            unique_numbers.append(num)
    return unique_numbers
print(unique([1, 11, 34, 11, 52, 61, 1, 34])) 
   