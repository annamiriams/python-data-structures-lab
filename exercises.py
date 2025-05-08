# Exercise 0: Example
#
# This is a practice exercise to familiarize you with basic Python data structures.
#
# Create a list called `example_list` and append three elements to it. Print each element using a loop.
#
# Requirements:
# - The list should contain any three elements of your choice.
# - Use a loop to print each element.

def example_list_function():
  example_list = ['element1', 'element2', 'element3']
  for element in example_list:
      print(element)

# Call the function and print each element
example_list_function()

# --------------------------------------------------------------------------------------------------------------

# Exercise 1: List and Indexing
#
# Create a list named students containing at least three student names (strings).
# Assign the second student’s name to a variable named first_student.
# Assign the last student’s name to a variable named last_student.

def manage_students():
    # your code here
    students = ['Adie', 'Remy', 'Maya']
    first_student = students[1]
    last_student = students[-1]
    
    return (first_student, last_student)

# Call the function and print the result
print('Exercise 1:', manage_students())

# --------------------------------------------------------------------------------------------------------------

# Exercise 2: Loop and String Concatenation
#
# Create a tuple named foods containing the same number of foods (strings) as there are names in the students list.
# Create a variable named meal and assign an empty string to it.
# Use a for loop to iterate over the strings in foods and append each string to meal.

def combine_foods():
    foods = ('Peanut Butter', 'Mac and Cheese', 'Candy')
    # your code here
    meal = ''
    
    for food in foods:
        # the result is ugly but whatever
        meal += food + ' '
    
    return meal

# Call the function and print the result
print('Exercise 2:', combine_foods())

# --------------------------------------------------------------------------------------------------------------

# Exercise 3: Slicing Tuples
#
# Using the slice operator, assign a new tuple containing only the last two food strings in the foods to a variable named last_two_foods.

def slice_foods():
    # your code here
    # i supposed i could have established foods as a global variable in the last exercise so i could reuse it here, but i didn't...
    foods = ('Peanut Butter', 'Mac and Cheese', 'Candy')
    last_two_foods = foods[-2:]
    return last_two_foods

# Call the function and print the result
print('Exercise 3:', slice_foods())

# https://www.geeksforgeeks.org/tuple-slicing-python/?utm_source=chatgpt.com
# slice = tuple[start:stop]
# Left out stop item (but kept the colon) so it would return items at -2 to the end

# --------------------------------------------------------------------------------------------------------------

# Exercise 4: Dictionaries and String Formatting
#
# Create a dictionary named home_town containing the keys of city, state, and population.
# Using the home_town dictionary, assign to a variable named home_town_message a string with this format: “I was born in <city>, <state> - population of <population>”

def hometown_info():
    # your code here
    home_town = {
        'city': 'Portland',
        'state': 'Oregon',
        'population': 630498,
    }
    
    home_town_message = f"I was born in {home_town['city']}, {home_town['state']} - population of {home_town['population']}."
    return home_town_message
# Call the function and print the result
print('Exercise 4:', hometown_info())

# --------------------------------------------------------------------------------------------------------------
