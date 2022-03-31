#to print include "Quotes"
#print ("Hello World")

# house is a string, and the output is White House 
house= "White House"
print(house)

#house is an integer and the output is 10
house= 10
print(house)

#Combining strings
house= "White House"
print("I would like to visit the " + house)
print("I would like to visit the" + " " + house + ".")

#another version involving f string (f meaning format)
house = "White House"
print(f"I would like to visit the {house}") 
#Note: Do not space f string, it will cause an error 
# example: print(f "I would like to visit the {house}") 