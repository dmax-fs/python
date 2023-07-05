board_games = ["Settlers of Catan", "Carcassone", "Power Grid", "Agricola", "Scrabble"]

sport_games = ["football", "hockey", "baseball", "cricket"]

for game in board_games:
    print(game)
    
    
for temp in range(6):
  print("Loop is on iteration number " + str(temp + 1))
  #This displays the number of loops run
  
  
  #While loop
count = 0
print("Starting While Loop")
while count <= 3:
  # Loop Body
  # Print if the condition is still true
  print("Loop Iteration - count <= 3 is still true")
  # Print the current value of count 
  print("Count is currently " + str(count))
  # Increment count
  count += 1
  print(" ----- ")
print("While Loop ended")


#Countdown loop
countdown = 10
print("Countdown")
while countdown > 0:
  print(str(countdown))
  countdown -= 1
  print(" ----- ")
print("We have liftoff!")

#use of len with a while-loop
length = len(ingredients)
index = 0
 
while index < length:
  print(ingredients[index])
  index += 1
  
python_topics = ["variables", "control flow", "loops", "modules", "classes"]

#Your code below: 
length = len(python_topics)
index=0
while index < length:
  print("I am learning about " + python_topics[index])
  index += 1

#Example of for loop/of statement with break
  
  dog_breeds_available_for_adoption = ["french_bulldog", "dalmatian", "shihtzu", "poodle", "collie"]
dog_breed_I_want = "dalmatian"

for dog_breed in dog_breeds_available_for_adoption:
  print(dog_breed)

  if dog_breed == dog_breed_I_want:
    print("They have the dog I want!")
    break

#Loop with continue statement. This will loop
#through the ages and only print > 21
ages = [12, 38, 34, 26, 21, 19, 67, 41, 17]

for i in ages:
  if i < 21:
    continue
  print(i)
  
#loops through nested data and prints total of all data at end
  sales_data = [[12, 17, 22], [2, 10, 3], [5, 12, 13]]

scoops_sold = 0

for location in sales_data:
  print(location)
  
  for element in location:
    scoops_sold += element
    
print(scoops_sold)


#Will loop through list and create a new list but with doubles
numbers = [2, -1, 79, 33, -45]
doubled = []
 
for num in numbers:
  doubled.append(num * 2)
 
print(doubled)

#list comprehension, one line *same problem as above
numbers = [2, -1, 79, 33, -45]
doubled = [i * 2 for i in numbers]
print(doubled)

#will only double negative numbers in the list
numbers = [2, -1, 79, 33, -45]
only_negative_doubled = []
 
for num in numbers:
  if num < 0: 
    only_negative_doubled.append(num * 2)
 
print(only_negative_doubled) 

#same problem as above, but using list comprehension.
numbers = [2, -1, 79, 33, -45]
negative_doubled = [num * 2 for num in numbers if num < 0]
print(negative_doubled)

#embedded else/if statement in list comprehension
numbers = [2, -1, 79, 33, -45]
doubled = [num * 2 if num < 0 else num * 3 for num in numbers ]
print(doubled)

#if height if over 161, it will be printed
heights = [161, 164, 156, 144, 158, 170, 163, 163, 157]

can_ride_coaster = [height for height in heights if height > 161]

print(can_ride_coaster)

#The prints our single, square and cubes of numbers 0-9
# Your code below:
single_digits = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9] #could also use range(9), here

for i in single_digits:
    print(i)
    squares.append(i**2)
    print(squares)

cubes = [j**3 for j in single_digits]
print("\n" + str(cubes))

#----------------------------------------------------------------
#loops through the ages and appends >= 21 to new list
#print length of the elements sorted in the new list
ages = [12, 38, 34, 26, 21, 19, 67, 41, 17]
x_list=[]
for i in ages:
    if i >= 21:
        x_list.append(i)
    continue
print(len(x_list))
