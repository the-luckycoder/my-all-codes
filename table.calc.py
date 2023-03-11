#importing time to add sleep time in the loop
import time
#take the no. for which we need the table
number = int(input('the table no. = '))

#take the no. till we need the table
Table_till = int(input('till value = '))

# let us print the value when they both no. get multiplied
print("Product of the both no. = ", number * Table_till)

multipler_value = 1

while  True:
  print(number,"x", multipler_value, "=", number*multipler_value)
  
  #  let's break the loop when we got our value
  if multipler_value == Table_till:
    break
    
    # increament of the multiplier
  multipler_value += 1
  time.sleep(1)
  