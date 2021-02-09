'''
items =["potato","milk","veggies"]

length = len(items)
counter = 0
while counter < length:
      print(items[counter])
      counter = counter + 1
range(endvalue)
'''

'''

for loop is used for repeating  over a sequence
'''
for number in range(5,10):
      print("this is coming from range funcion",number)

# homework for negative number
"""var = input("enter the inout here")
for evennumber in range(-30,-1,2):

      print(evennumber)"""

age = input("Enter you age here")
name = input("enter your name here")
if int(age) >= 18:
      print("Provide alcohol to ",name)
else:
      print("do not provide alcohol to ",name)


fruits = ("apple","banana", "orange")
for s in fruits:
      print (s)
for x in "banana" and "Orange":
      print(x)

''' Range function returns a sequence of numbers starting 
 by default 0 and increments by 1(default) and ends at a specified number'''

for x in range(2,6): # third parameter can be added fr how much value we are incrementing
    print(x)