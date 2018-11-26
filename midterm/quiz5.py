from random import seed, randint
from math import sqrt
from statistics import mean, median, pstdev
import sys


# Prompt the user for a seed for the random number generator,
# and for a strictly positive number, nb_of_elements.
#
# See previous challenge.

arg_for_seed = input('Input a seed for the random number generator: ')
try:
    arg_for_seed = int(arg_for_seed)
except ValueError:
    print('Input is not an integer, giving up.')
    sys.exit()   

nb_of_elements = input('How many elements do you want to generate? ')
try:
    nb_of_elements = int(nb_of_elements)
except ValueError:
    print('Input is not an integer, giving up.')
    sys.exit()
if nb_of_elements <= 0:
    print('Input should be strictly positive, giving up.')
    sys.exit()
# Generates a list of nb_of_elements random integers between 0 and 99.

seed(arg_for_seed)
L = [randint(-50, 51) for _ in range(nb_of_elements)]
# Prints out the list, computes the maximum element of the list, and prints it out.
print('\nThe list is:', L)

print()
avg=sum(L)/nb_of_elements
print('The mean is %.2f' %avg+'.')

L.sort()
if nb_of_elements%2==0:
	mid=(L[nb_of_elements//2-1]+L[nb_of_elements//2])/2
else:
	mid=L[(nb_of_elements-1)//2]
	
print('The median is %.2f' %mid+'.')
stand=sum((x-avg)**2 for x in L)/nb_of_elements
stand_avg=sqrt(stand)

print('The standard deviation is','%.2f' %stand_avg+'.')
print()

print('Confirming with functions from the statistics module:')
print('The mean is','%.2f' %mean(L)+'.')
print('The median is','%.2f' %median(L)+'.')
print ('The standard deviation is','%.2f' %pstdev(L)+'.')
# Generate a list of nb_of_elements random integers between -50 and 50.
#
# See previous challenge.


# Print out the list, compute the mean, standard deviation and median of the list,
# and print them out.
#
# To compute the mean, use the builtin sum() function.
# To compute the standard deviation, use sum(), the sqrt() from the math module,
# and the ** operator (exponentiation).
# To compute the median, first sort the list.
#
# The following interaction at the python prompt gives an idea of how these functions work:
# >>> from math import sqrt
# >>> sqrt(16)
# 4.0
# >>> L = [2, 1, 3, 4, 0, 5]
# >>> L.sort()
# >>> L
# [0, 1, 2, 3, 4, 5]
# >>> L = [2, 1, 3, 4, 0, 5]
# >>> sum(L)
# 15
# >>> sum(x ** 2 for x in L)
# 55
# >>> L.sort()
# >>> L
# [0, 1, 2, 3, 4, 5]
#
# Then use the imported functions from the statistics module to check the results.
