first_number = int(raw_input('Enter first number: '))
second_number = int(raw_input('Enter second number: '))

sum_answer = str(first_number + second_number)

print 'The sum of ' + str(first_number) + ' and ' + str(second_number) + ' is ' + str(sum_answer)

sub_answer = str(second_number - first_number)

print 'The difference of ' + str(second_number) + ' and ' + str(first_number) + ' is ' + sub_answer

product_answer = str(first_number * second_number)

print 'The product of ' + str(first_number) + ' and ' + str(second_number) + ' is ' + product_answer

integer_division = str(first_number / second_number)
integer_remainder = str(first_number % second_number)

print 'The quotient of ' + str(first_number) + ' and ' + str(second_number) +  ' is ' + integer_division +\
      ' with the remainder ' + integer_remainder

