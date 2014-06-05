#Changing code formatting for cleaner more readability
i1 = raw_input('Enter the first number: ')

while not i1.isdigit():
    i1 = raw_input("Not a valid integer. Please enter the first integer: ")

i1 = int(i1)

i2 = raw_input('Enter the second number: ')

#since you cannot divide zero in anything, this while loops informs and reprompts user to enter another number
while i2 == '0' or not i2.isdigit():
    if i2 == '0':
        i2 = raw_input("Cannot divide by zero. Please enter the second integer: ")
    else:
        i2 = raw_input("Cannot divide by zero. Enter another number: ")

i2 = int(i2)



#Grouping code together according to function. Arithmetic grouped together and print statements together
#Also shortening variable names from ex. 'first_number to i1.
sum_answer = str(i1 + i2)
sub_answer = str(i2 - i1)
product_answer = str(i1 * i2)
int_division = str(i1 / i2)
int_remainder = str(i1 % i2)

print 'The sum of ' + str(i1) + ' and ' + str(i2) + ' is ' + str(sum_answer)
print 'The difference of ' + str(i2) + ' and ' + str(i1) + ' is ' + sub_answer
print 'The product of ' + str(i1) + ' and ' + str(i2) + ' is ' + product_answer
print 'The quotient of ' + str(i1) + ' and ' + str(i2) +  ' is ' + int_division +\
      ' with the remainder ' + int_remainder

