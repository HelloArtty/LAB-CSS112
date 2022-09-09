#1
print("Cutie, Cutie, little girl,\n\tHow I wonder what you are!\n\t\tUp above the world so high,\n\t\tLike a star in sky.\nCutie, cutie, little girl,\n\tHow I wonder what you are!")

#2
list_jack = ['Jack',':','How ','are ','you ','today ','?']
list_jim = ['Jim ',"I'm ",'well ','Thank ','you ','and ','you ','?']

print("".join(list_jack))
print("".join(list_jim))

#3
import math
square_root = 3
triple_root = 8
root2 = square_root**(1/2)
root3 = triple_root**(1/3)
print("The square root of 3.000 is %.3f"%root2)
print("The square root of 8.000 is %.3f"%root3)

#4
celsius = 100
fahrenheit = (9/5*celsius)+32
print("Temperature in 100 Celsius =" + str(fahrenheit) + " Fahrenheit")

#5
tuple1 = ("Orange",[10,20,30],(5,15,25))

print(tuple1[1][1])
print(tuple1[2][2])

#6
tuple1 = tuple1 = ('ab',78) 
tuple2 = (99,'cd')
tuple1,tuple2 = tuple2,tuple1

print("From the original Tuple 1 =('ab',78)\n\tand Tuple2 = (99,'cd')")
print("The newly swapped tuples are:")
print("Tuple 1 = " + str(tuple1))
print("Tuple 2 = " + str(tuple2))

#7
sample_dict = {
 'emp1': {'name': 'Jhon', 'salary': 7500},
 'emp2': {'name': 'Emma', 'salary': 8000},
 'emp3': {'name': 'Brad', 'salary': 6500}
}

sample_dict['emp2']['salary'] = 10000
print(sample_dict)