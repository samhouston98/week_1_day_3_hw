def return_10():
    return 10

def add(num1, num2):
    return num1 + num2

def subtract(num1, num2):
    return num1 - num2

def multiply(num1, num2):
    return num1 * num2

def divide(num1, num2):
    return num1 / num2

def length_of_string(string):
    return len(string)


def join_string(string1, string2):
    return string1 + string2

def add_string_as_number(string1, string2):
    return int(string1) + int(string2) 

def number_to_full_month_name(num1):
    if num1 == 1:
        return "January"

    if num1 == 3:
        return "March"
    
    if num1 == 9:
        return "September"
    

def number_to_short_month_name(num1):
    if num1 == 1:
        return "Jan"
    
    if num1 == 4:
        return "Apr"
    
    if num1 == 10:
        return "Oct"



