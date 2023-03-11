import random


# x = 25
# if x > 50:
#    print("X seems to be greater than 50!")
# else:
#     print("x is less than 50")



randomNumberGen = random.randint(1, 40)
# print(randomNumberGen)

name = "Erick"
# print(f"{name} is {randomNumberGen} years old")

#Creating a list and experimenting on a list
list_of_names = ['Erick', 'Stephen', 'Michael']

information_on_erick = ["21", "Erick", "Blue", "Brown-eyes", "Basketball", "85wpm"]

random_info = ["761", ["Erick", "21", "brown-eyes"], "ginger-ale"]

empty_list = []

empty_list.append(information_on_erick)

fruit = ["Apple", "Banana", "Orange", "Pineapple"]

vegetable = ["Carrots", "Bell Pepper", "Cucumber", "Lettuce"]

fruits_and_vegetables = fruit + vegetable

salad = 3 * vegetable

#Making a copy of a list 

copy_of_information = information_on_erick[:]

copy_of_information.pop()

copy_of_information.append("James Harden")






#------------------------------------------------------------
# print(list_of_names[1])

# print(information_on_erick[0])

# print(random_info[1])

# print(f"Empty list now contains these contents: {empty_list}")

# print(fruits_and_vegetables)

# print(salad)

# print(information_on_erick[:5])

# print(information_on_erick[3:])

# print(information_on_erick[2:4])

# print(f"I made a copy of my information, this is the original:\n{information_on_erick}\nThis is the new updated version:\n{copy_of_information}")

# print(f"The number of items in the list of Information on Erick is: ", len(information_on_erick))
# print(f"The max number of item in the same sequence is: ", len(max(information_on_erick)))
# print(f"The min number of items in the same sequence is: ", min(information_on_erick))
# print(f"This sorts the items in the same sequence: ", sorted(information_on_erick))
#the sorted sequence seems to sort the items first with numbers and then sorts alphabetical order

#---------------------------------------------------------------------------------------

#Trying new things now

copy_of_information.append("Volleyball")  #Using the (dot)append function
# print(f"I just added volleyball, Expected to have it at the end of copy of information of Erick: {copy_of_information}\n\n")

#Using (dot)pop function to take volleyball item out
copy_of_information.pop()
# print(f"it should be the same as before without volleyball using the pop function: {copy_of_information}\n\n")

# print(f"Ill try to access the copy of information of Erick and get the 'brown-eyes' item: {copy_of_information.index('James Harden')}")
#The value when using (dot)index, must be the exact value name of the item that's inside the list


#==========================================================================================================

#practiing tuples

yogi = ("German-Shepard, Husky MIX", 3, "Playful, energetic", "Dog")






