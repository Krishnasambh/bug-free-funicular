#learning operators
'''
mathematical, logical, conditional operators
'''

first_num = 200
second_num = 300
third_num =400

print("addition is", first_num + second_num)
print("subtraction is", first_num - second_num)
print("multiplication is", first_num * second_num)
print("Division is", first_num / second_num)
print("exponentiation", first_num ** second_num)
print("Reminder is", first_num % second_num)

# comparision operation >,<,==
#Logical operaters
'''
AND Operator
s1    s2    s1 and s2
t      t       t
t      f       f
f      t       f
f      f      f

OR Operator

S1     S2      S1 Or S2


'''
s1 = first_num > second_num
s2 = first_num > third_num
result = s1 and s2
print("Result:",result)

s1 = first_num > second_num
s2 = first_num > third_num
result = s1 or s2
print(result)
'''
OR Operator
s1    s2    s1 and s2
t      t       T
t      f       T
f      t       T
F      F        F

'''