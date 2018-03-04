
"""     Description: The purpose of this program is to print the unique command line arguments 
        it receives in alphabetical and numerical order. 
        
        This function works for both numeric and string values. The numeric values will be
        printed first in ascending order, and the string values will be inputed second in 
        alphabetical order.
"""

import sys

#Quit if only file name entered
numArgs = len(sys.argv)
if numArgs == 1:
	print('\nOnly the file name was entered. \nFile name: %s' % sys.argv[0])
	quit()
    
#Function to see if element can be converted into a float
def isfloat(value):
  try:
    float(value)
    return True
  except ValueError:
    return False

#Print File Name and Create list of Command Line Inputs (exclude file name)
the_list = []
for i in range(len(sys.argv)):
    if i == 0:
        print ('\nFile name: %s' % sys.argv[0])
    else:
        the_list.append(sys.argv[i])

new_list = set(the_list) #turning into set removes duplicates
new_list = list(new_list) #turn back into list

#Separate String and Floats from each other
float_list = []
str_list = []
for i in range(len(new_list)):
    if isfloat(new_list[i]): #check if float 
        float_list.append(new_list[i]) #float list
    else:
        str_list.append(new_list[i]) #string list


sort_list = sorted(float_list, key=int) + sorted(str_list) #sort each list individually and combine

delimiter = ', '		
print('\nOriginal Command Line Inputs:\n', delimiter.join(the_list)) 
print('\nUnique Sorted List:\n', delimiter.join(sort_list))  


