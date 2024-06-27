#!/usr/bin/env python
import sys


# Sum of all sales (values) is initialized with zero, we just started
sum_of_values = 0

# Previous key is initialized with None, we just started
previous_key = None

# For each new line in the standard input 
for line in sys.stdin:

    data = line.strip().split("\t")
    key, value = data

    # Do we have a previous_key (previous_key != None) and 
    # is the new key different than the previous key?
    # This means the line starts with a new key (key changes e.g. from "Visa" to "Cash")
    # Remember that our keys are sorted
    if previous_key != None and previous_key != key:
        # Then write the result of the old key (Key=category, Value= Sum of Sales)
        # to the standart output (stdout)
        # Key and value are seperated by a tab (\t)
        # Line ends with new line (\n)
        sys.stdout.write("{0}\t{1}\n".format(previous_key, sum_of_values))
        # Sum of sales starts again with 0
        sum_of_values = 0

    # Add the value to the total sales
    # a += b is the same as a = a + b
    # the float function transforms the value
    # to a float data type (like decimal)
	sum_of_values += float(value)
	previous_key = key
    # the previous key for the next iteration is the current key of the this iteration 

# write the last result to stdout
sys.stdout.write("{0}\t{1}\n".format(previous_key, sum_of_values))
