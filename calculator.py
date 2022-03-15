#python
import os
os.system("clear")

print("\033[1;32;40m CALCULATOR PROGRAM MADE BY N. DAVID CHINEDU \n")
print("\033[1;33;40m THIS TOOL WILL HELP IN SOLVING BASIC MATHEMATICAL OPERATIONS FOR EDUCATIONAL PURPOSES\n")

print("""                                                                               

$   $        $        $      $   $
$  $        $ $       $      $  $
$ $        $   $      $      $ $
$$        $     $     $      $$
$ $      $$$$$$$$$    $      $ $
$  $    $         $   $      $  $
$   $  $           $  $      $   $
$    $$             $ $$$$$$ $    $
                                

==================Beta Version 2.0==============""")

print("\033[96m  :::::::::::::: CALCULATOR IS NOW WORKING.:::::::::::::\n")
print("\033[95m Follow me on github: https://github.com/DavidKumar45\n") 
print(" Follow me on facebook: https://www.facebook.com/profile.php?id=100063716716333\n")
print("\033[1;37;40m  Follow my group on Facebook: https://www.facebook.com/groups/424459056032458/\n")

def calculate():
    operation = input('''
Please type in the math operation you would like to complete:
Type + for addition
Type - for subtraction
Type * for multiplication
Type / for division
''')

    number_1 = int(input('Please enter the first number: '))
    number_2 = int(input('Please enter the second number: '))

    if operation == '+':
        print('{} + {} = '.format(number_1, number_2))
        print(number_1 + number_2)

    elif operation == '-':
        print('{} - {} = '.format(number_1, number_2))
        print(number_1 - number_2)

    elif operation == '*':
        print('{} * {} = '.format(number_1, number_2))
        print(number_1 * number_2)

    elif operation == '/':
        print('{} / {} = '.format(number_1, number_2))
        print(number_1 / number_2)

    else:
        print("\033[1;31;40m You have not typed a valid operator, please run the program again\n.")

    # Add again() function to calculate() function
    again()

def again():
    calc_again = input('''
Do you want to calculate again?
Please type Y for YES or N for NO.
''')

    if calc_again.upper() == 'Y':
        calculate()
    elif calc_again.upper() == 'N':
      print("\033[2;37;40m THANKS FOR USING THIS CALCULATOR SEE YOU LATER\n")
    else:
        again()

calculate()
