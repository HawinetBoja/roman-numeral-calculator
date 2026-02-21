# Author: Hawinet Tadesse
# Date: 08/20/2023
# Description: Changing roman numerals to integer and then passing the integers through an operation choose by the user and then printing the result
# integer in roman numeral. I have used Function to make it easy for people to understand the code and to reduce redundancy.
import sys 

print("*"*50)
print("|  Hawinet Tadesse's Roman Numeral Calculator")
print("-"*50)
print("|  You can use +, -, *, / and ^ operators")
print("*"*50)

# Hence there is no roman numeral less than zero and the maximum roman numeral we can use in this is project is 3999.
#This class is used to exit the program if the final value of the integer is greater than 3000 or less than 1.

def roman_to_int(roman1, roman2): 
       
    index = len(my_integer)-1
    integer = 0
    integer2 = 0
    int_to_roman = ""
    remainder_to_rom = ""

    length = len(roman1)
    length_Second = len(roman2)
    i=0
    while i < length:
   
        if i!= length-1 and roman_dic[roman1[i]] < roman_dic[roman1[i+1]]:
            integer += roman_dic[roman1[i]]*-1
        else:
            integer += roman_dic[roman1[i]]
        i+=1
       
    i=0         

#Since we already used i as the index for the first input it has been incremented,
#therefore, we must set it to 0 again to use it for the second input
    while i < length_Second:
        if i!= length_Second-1 and roman_dic[roman2[i]] < roman_dic[roman2[i+1]]:
            integer2 += roman_dic[roman2[i]]*-1
           
        else:
            integer2 += roman_dic[roman2[i]]
   
        i+=1

    return integer, integer2, index  

#returns the first integer and second integer

def error_check(first_int): 

#This function is used to check if the final value of the integer is below 3999

 # and greater than 0 prior printing the final roman numeral.
 #The max integer for this code is 3999 and any number above that and less than 0 is considered and labeld as an error by this function.

    if first_int > 3999:
        sys.exit("The final result after operation is greater than the upper limit number which is 3999.")
    elif first_int < 1:
        sys.exit("The final result after operation is less than the lower limit number which is 1.")

def arthimetic_operation(integer, integer2): 

#This function is used to do the operation on the first and second
    scan = True 

#We will use this bool value to check if a division has been performed
    operator = input("Choose the an operation to be excuted: ")
    operation = ["+", "-", "*", "/", "^"]
    while operator not in operation:
        operator = input("Enter a valid operator: ")
    if operator == "+":
        total = integer2 + integer
    elif operator == "-":
        total = integer - integer2
    elif operator == "*":
        total = integer2 * integer
    elif operator == "^":
        total = integer ** integer2
    elif operator == "/":
        total = integer // integer2
        remainder = integer % integer2
        scan = False
       
    if scan == False and remainder > 0:
        return total, remainder
    else:
        return total

def integer_to_roman(total, index):

 #this function is used to convert integer number to roman number.
    int_to_roman = "" 

# this string is used to store converted roman numerals 
    while total:
        value = total // my_integer[index]
        total %= my_integer[index]
 
        while value:
            int_to_roman+=roman_numerals[index]
            value -= 1
        index -= 1
    return int_to_roman

# The below dicitionary contains roman numbers and their appropriate assignment to an integer.

roman_dic = {"I": 1, "II" : 2, "III" : 3, "IV" : 4, "V" : 5, "VI" : 6,
              "VII" : 7, "VIII" : 8, "IX" : 9, "X" : 10, "XX" : 20, "XXX" : 30,
              "XL" : 40, "L" : 50, "LX" : 60, "LXX" : 70, "LXXX" : 80, "XC" : 90, "C" :
              100, "CC" : 200, "CCC" : 300, "CD" : 400, "D" : 500, "CM" : 900, "M": 1000}

# creating two parallel lists, we will use this to convert the integer back to roman numerals
my_integer = [1, 4, 5, 9, 10, 40, 50, 90,100, 400, 500, 900, 1000]
roman_numerals = ["I", "IV", "V", "IX", "X", "XL","L", "XC", "C", "CD", "D", "CM", "M"]

letter_to_proceed_the_program = "G"  
while letter_to_proceed_the_program  != "L": 

#this is used to check what the user enters and if the user enters a letter Q the program exists other wise it will continue and
# agian asks the user to enter another roman numeral. 

    userI = input("Enter the first roman number:").upper()
    i=0
    while i < len(userI):
        while userI[i] not in roman_numerals:
            userI = input("Enter a valid rom number:").upper()
        i+=1
    userIn2 = input("Enter the second roman number: ").upper()
    i=0
    while i < len(userIn2):
        while userIn2[i] not in roman_numerals:
            userIn2 = input("Enter a valid rom number:").upper()
        i+=1

   
    integer = roman_to_int(userI, userIn2)
    first_integer = integer[0]
    second_integer = integer[1]

    error_check(first_integer)
    error_check(second_integer)

    index = integer[2]  
    result = arthimetic_operation(first_integer, second_integer)
    test = type(result) is tuple 
       
    if test == True:
        total = result[0]
        error_check(total)
        print(f'The quotient is {integer_to_roman(total, index)}')
        remainder = result[1]
        error_check(remainder)
        print(f' and the remainder is {integer_to_roman(remainder, index)}')
    else:
        error_check(result)
        print(f'The total value is {integer_to_roman(result, index)}')
   
    letter_to_proceed_the_program = input("Enter l to leave or any other letter to continue:").upper()
    
print("You have succesfully left the program!")

