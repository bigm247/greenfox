# - Create an array variable named `animals`

animals = ["koal", "pand", "zebr", "anacond", "bo", "chinchill", "cobr", "gorill", "hyen", "hydr", "iguan", "impal", "pum", "tarantul", "piranh"]
for i in range(len(animals)):
    animals[i] = animals[i]+ "a"
    print(animals)

# - Create an array variable named `numbers`
# - Change the value of the fourth element (8) to 4
numbers = [1, 2, 3, 8, 5, 6]
numbers [3] = 4
print(numbers[3])

# - Create a two dimensional list (of strings)
#   which can contain the different shades of specified colors
colors= [["lime", "forest green", "olive", "pale green", "spring green"],["orange red", "red", "tomato"],["orchid", "violet", "pink", "hot pink"]]
for i in range(len(colors)):
    print(", ".join(colors[i]))


# - Create a variable named `firstArrayOfNumbers` has more element than`secondArrayOfNumbers`

firstArrayOfNumbers = [1, 2, 3]
secondArrayOfNumbers = [4,5]
if len(secondArrayOfNumbers) > len(firstArrayOfNumbers):
    print("secondArrayOfNumbers")
else:
    print("firstArrayOfNumbers is the longer one")

    #Create a variable named `numbers` and # - Increment the third element
    numbers = [1, 2, 3, 4, 5]
    numbers[2] +=1
    print(numbers[2])

    # - Create an array variable named `numbers` and # - Double all the values in the array and print the modified
numbers = [3, 4, 5, 6, 7]
for i in range(len(numbers)):
    numbers[i] *=2
    print(numbers)

# - Create a variable named `numbers` and print all the element
numbers = [4, 5, 6, 7]
print(numbers)

# - Create a variable named `numbers` and # - Reverse the order of the elements of `numbers` programmatically
numbers = [3, 4, 5, 6, 7]
numbers_reverse = numbers[::-1]
print(numbers_reverse)

# - Create a variable named `numbers` and # - Print the third element of `numbers`
numbers = [4, 5, 6, 7]
print(numbers[2])

# - Create an array variable named `orders` and Swap the first and the third element of `orders` programmatically
orders = ["first", "second", "third"]
orders[0], orders[2] = orders[2], orders[0]
print(orders)

# - Create a variable named `numbers` and sum the numbers
numbers = [3, 4, 5, 6, 7]
sum_of_numbers = sum(numbers)
print(sum_of_numbers)

# - Create a variable named `numbers` and sum the second and third numbers
numbers = {54, 23, 66, 12}
sum_of_second_third_numbers = numbers[1] + numbers[2]
print(sum_of_second_third_numbers)
