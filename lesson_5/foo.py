# Data
people = [["Alex", 178], ["Noah", 189], ["Peter", 175], ["John", 185], ["Michelle", 165]]

# Iterating over external list
for i in range(len(people)):
    if type(people[i]) is list:
        # Calculate and round height in inches
        ht_in = round(people[i][1]/2.54, 2)
        print(people[i][0], 'is', ht_in, 'inches tall')

# Define function
def sum_squared(a, b):
  return (a + b)**2

# Call function
print(sum_squared(2, 3))

# Define a function
def is_odd(n):
  if n % 2 == 0:
    return "even"
  else:
    return "odd"

# Testing function
print('2 is', is_odd(2))
print('3 is', is_odd(3))