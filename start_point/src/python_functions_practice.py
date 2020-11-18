def return_10():
    return 10

def add(num1, num2):
    return num1 + num2

def subtract(num1, num2):
    return num1 - num2

def multiply(num1, num2):
    return num1 * num2
    
def divide(number1, number2):
    return number1 / number2

def length_of_string(test_string):
    return len(test_string)

def join_string(string_1, string_2):
    join_string = ( string_1 + string_2 )
    return join_string

def add_string_as_number(string1, string2):
    return int(string1) + int(string2)

def number_to_full_month_name(month_number):
    month = {1 : "January", 2 : "Febuary", 3 : "March", 4 : "April", 5 : "May", 6 : "June", 7 : "July", 8 : "August", 9 : "September", 10 : "October", 11 : "November", 12 : "December"}
    return month[month_number]

def number_to_short_month_name(month_number):
    full_month_name = number_to_full_month_name(month_number)
    short_month_name = full_month_name[0:3]
    return short_month_name

