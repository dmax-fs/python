def trip_welcome():
  print("Welcome to Tripcademy!") 
  print("Let's get you to your destination.")
trip_welcome()

#This will print out the statements within the fuctions body

def generate_trip_instructions(location):
  print("Looks like you are planning a trip to visit " + location)
  print("You can use the public subway system to get to " + location)

generate_trip_instructions("Grand Central Station")

#Same as above, but has a parameter defined for the function

def calculate_expenses(plane_ticket_price, car_rental_rate, hotel_rate, trip_time):

  car_rental_total = car_rental_rate * trip_time

  hotel_total = hotel_rate * trip_time - 10

  print("Total cost of your trip will be: £"+ str(car_rental_total+hotel_total+plane_ticket_price))

calculate_expenses(200, 100, 100, 5)

#calling a funcation with multiple arguments


tshirt_price = 9.75
shorts_price = 15.50
mug_price = 5.99
poster_price = 2.00

# Write your code below:
max_price=max(9.75, 15.50, 5.99, 2.00)
print(max_price)

min_price=min(9.75, 15.50, 5.99, 2.00)
print(min_price)

rounded_price=round(tshirt_price,1) #round to nearest 1 dp
print(rounded_price)
#some built in pyton funcation

#-------------------------------------------------------------
current_budget = 3500.75

def print_remaining_budget(budget):
  print("Your remaining budget is: $" + str(budget))

print_remaining_budget(current_budget)
#this funcation takes one parameter (budget) and will print out the remaining budget
#to the terminal

def deduct_expense(budget, expense):
  return budget-expense
#This funcation takes 2 parameters (budget, expense), it will return the product of
#subtracting budget from expense.

shirt_expense = 9

new_budget_after_shirt = deduct_expense(current_budget, shirt_expense)
#new variable that calls the deduct_expense function, and calls the current_budget as the first parameter
#and shirts_expense as the second parameter.

print_remaining_budget(new_budget_after_shirt)

#------------------------------------------------
def top_tourist_locations_italy():
  first = "Rome"
  second = "Venice"
  third = "Florence"
  return first, second, third
  
most_popular1,most_popular2,most_popular3 = top_tourist_locations_italy()

print(most_popular1)
print(most_popular2)
print(most_popular3)

#-------------------------------------------------

def trip_planner_welcome(name): 
  print("Welcome to tripplanner v1.0 " + name)

trip_planner_welcome("David ")

def estimated_time_rounded(estimated_time):
  rounded_time = round(estimated_time)
  return rounded_time

estimate = estimated_time_rounded(2.73)

def destination_setup(origin, destination, estimated_time, mode_of_transport="Car"):

  print("Your trip starts off in " + origin +
" And you are traveling to " + destination +
" You will be traveling by " + mode_of_transport +
"It will take approximately " + str(estimated_time) + " hours")

destination_setup("London", "New York", estimate, "Plane")

#simple example trip planner
#----------------------------------------------------------------
def f_to_c(f_temp):
  c_temp = (f_temp-32) * 5/9
  return c_temp

f100_in_celsius = f_to_c(100)
print(f100_in_celsius)
#Function that converts f_to_celsius

#----------------------------------------------------------------
#science funcations
train_mass = 22680
train_acceleration = 10
train_distance = 100
bomb_mass = 1
c=3*10**8

# Write your code below: 

def f_to_c(f_temp):
  c_temp = (f_temp-32) * 5/9
  return c_temp

f100_in_celsius = f_to_c(100)
print(f100_in_celsius)
#-------------f_to_c-------------
def c_to_f(c_temp):
  f_temp = ((c_temp*(9/5)) + 32)
  return f_temp
#--------------c_to_f------------
c0_in_fahrenheit = c_to_f(0)
print(c0_in_fahrenheit)
#--------------f=ma--------------
def get_force(mass, acceleration):
  force = mass * acceleration
  return force

train_force = get_force(train_mass, train_acceleration)
print("The GE train supplies: "+str(train_force) +" Newtons of force")
#---------------energy-----------
def get_energy(mass, c):
  energy = mass * c
  return energy

bomb_energy = get_energy(bomb_mass,c)
print("A 1kg bomb supplies: "+ str(bomb_energy) +" Joules.")
#---------------work------------
def get_work(mass, acceleration, distance):
  wrk = (mass*acceleration)*distance
  return wrk

train_work = get_work(train_mass, train_acceleration, train_distance)
print("The GE train does: " + str(train_work) + " Joules of work over " + str(train_distance) + " meters.")

#----------------------------------------------------------------
#Codeing challenge 1

def large_power(base, exponent):
  power=base**exponent
  #return power
  if power > (5000):
   return True
  else:
   return False


# Uncomment these function calls to test your large_power function:
#print(large_power(2, 13))
# should print True
print(large_power(2, 12))
# should print False

def large_power(base, exponent):
  if base ** exponent > 5000:
    return True
  else:
    return False
#Easier solution with one less step

#Codeing challenge 2
def over_budget(budget, food_bill, electricity_bill, internet_bill, rent):
  if (budget < food_bill + electricity_bill + internet_bill + rent):
    return True
  else:
    return False

#Codeing challenge 5
def max_num(num1, num2, num3):
  if num1 > num2 and num1 > num3:
    return num1
  elif num2 > num1 and num2 > num3:
    return num2
  elif num3 > num1 and num3 > num2:
    return num3
  else:
    return "It's a tie!"

print(max_num(4,6,3))
#Will take an input string and return max_num from list

#----------------------------------------------------------------
#List Challenges
#
#calculate the length of a list and
#then append the value to the end of the list.

def append_size(my_list):
  my_list.append(len(my_list))
  return my_list

print(append_size([23, 42, 108]))

#2
#function that calculates the sum of the last two 
#elements of a list and appends it to the end.

def append_sum(my_list):
  for i in my_list:
    my_list.append(my_list[-1]+my_list[-2])
    if len(my_list) == 6:
 
      return my_list

print(append_sum([1, 1, 2]))

#------------------------------------------------------
#3
#The function should return the last element of the list that contains more elements. 
# If both lists are the same size, then return the last element of my_list1.
def larger_list(my_list1, my_list2):
  if len(my_list1) > len(my_list2) or len(my_list1) == len(my_list2):
      #replace with >= duh! less lines of code, gets same result
    return my_list1[-1]
  else:
    return my_list2[-1]


#Uncomment the line below when your function is done
print(larger_list([4, 10, 2, 5], [-10, 2, 5, 10]))

#------------------------------------------------------
#4
#Create a function named more_than_n that has three parameters named my_list, item, and n.
#The function should return True if item appears in the list more than n times. 
#The function should return False otherwise.

def more_than_n(my_list, item, n):
    in_list=[]
    for i in my_list:
        if i == item:
            in_list.append(i)
        continue
    if len(in_list)>n:
        return True
    else:
        return False

#Uncomment the line below when your function is done
print(more_than_n([2, 4, 6, 2, 3, 2, 1, 2], 2, 3))

#simplified version of more_than_n - I didn't know about count function
def more_than_n(my_list, item, n):
  if my_list.count(item) > n:
    return True
  else:
    return False
#------------------------------------------------------
#§
#Write a function named combine_sort that has two parameters named my_list1 and my_list2.
#The function should combine these two lists into one new list and 
#sort the result. Return the new sorted list.
def combine_sort(my_list1, my_list2):
  new_list=my_list1+my_list2
  sorted_list = sorted(new_list)
  return sorted_list

print(combine_sort([4, 10, 2, 5], [-10, 2, 5, 10]))
#------------------------------------------------------
#LIST ADVANCED PROBLEMS
#1
#Create a function called every_three_nums that has one parameter named start.
#The function should return a list of every third number between start and 100 (inclusive).
#For example, every_three_nums(91) should return the list [91, 94, 97, 100]. 
# If start is greater than 100, the function should return an empty list.
def every_three_nums(start):
  return list(range(start, 101, 3))
print(every_three_nums(91))
#------------------------------------------------------
#2
# The function will accept a list, a starting index, and an ending index. All elements with 
# an index between the starting and ending index should be removed from the list.
def remove_middle(my_list, start, end):
    end = end + 1
    del my_list[start:end]
    return my_list

print(remove_middle([4, 8, 15, 16, 23, 42], 1, 3))
#simplified version of remove_middle
def remove_middle(my_list, start, end):
  return my_list[:start] + my_list[end+1:]
#------------------------------------------------------
#3
#
def more_frequent_item(my_list, item1, item2):
    if my_list.count(item1) > my_list.count(item2) or my_list.count(item1) == my_list.count(item2):
        return item1
    else:
        return item2
    
print(more_frequent_item([2, 3, 3, 2, 3, 2, 2, 3], 2, 3))
#simplified version of more_frequent_item
def more_frequent_item(my_list, item1, item2):
  if my_list.count(item1) >= my_list.count(item2):
    return item1
  else:
    return item2
#------------------------------------------------------
#4
#The function should return a new list where all elements are the same 
#as in my_list except for the element at index. The element at index should be 
#double the value of the element at index of the original my_list.
def double_index(my_list, index):
    if index >= len(my_list):
        return my_list
    else:
        new_list = my_list[0:index]
    new_list.append(my_list[index]*2)
    new_list = new_list + my_list[index+1:]
    return new_list

print(double_index([1, 2, 3, 4], 2))
#***didn't manage to solve this one***
#------------------------------------------------------
#5
#If there are an odd number of elements in my_list, the function should 
#return the middle element. If there are an even number of elements, the function 
#should return the average of the middle two elements.
def middle_element(my_list):
  if len(my_list) % 2 == 0:
    sum = my_list[int(len(my_list)/2)] + my_list[int(len(my_list)/2) - 1]
    return sum / 2
  else:
    return my_list[int(len(my_list)/2)]

print(middle_element([5, 2, -10, -4, 4, 5]))
#***didn't manage to solve this one***

#------------------------------------------------------
#LOOPS
#1
#Create a function named divisible_by_ten() that takes a list of numbers 
#named nums as a parameter.
#Return the count of how many numbers in the list are divisible by 10.
def divisible_by_ten(nums):
    new_list = []
    for i in nums:
        if i % 10 == 0:
            new_list.append(i)
    return len(new_list)
            
print(divisible_by_ten([20, 25, 30, 35, 40]))
#----------------------------------------------------
#2
#In the function, create an empty list that will contain each greeting.
#Add the string 'Hello, ' in front of each name in names and append the greeting to the list.
def add_greetings(names):
    new_greeting = []
    for name in names:
        new_greeting.append("Hello, " + name)
    return new_greeting
    
print(add_greetings(["Owen", "Max", "Sophie"]))
#----------------------------------------------------
#3
#The function should remove elements from the front of my_list until the front of the list
# is not even. The function should then return my_list.
def delete_starting_evens(my_list):
        while len(my_list) > 0 and my_list[0] % 2 == 0:
            my_list = my_list[1:]
        return my_list

    
print(delete_starting_evens([4, 8, 10, 11, 12, 15]))
#----------------------------------------------------
#4
#The function should create a new empty list and add every element from my_list 
#that has an odd index. The function should then return this new list.
def odd_indices(my_list):
    odd_list = []
    for i in range(1, len(my_list), 2):
        odd_list.append(my_list[i])
    return odd_list

print(odd_indices([4, 3, 7, 10, 11, -2]))
#----------------------------------------------------
#5
#Create a function named exponents() that takes two lists as parameters
#named bases and powers. Return a new list containing every number in bases raised
#to every number in powers.
def exponents(bases, powers):
    raised = []
    for i in bases:
        for j in powers:
            raised.append(i**j)
    return raised

print(exponents([2, 3, 4], [1, 2, 3]))
#----------------------------------------------------
#ADVANCED LOOPS
#1
#Larger Sum: returns the list of number that has the highest sum value
def larger_sum(lst1, lst2):
    sum1 = 0
    sum2 = 0
    for i in lst1:
        sum1 += i
    for j in lst2:
        sum2 += j
    if sum1 >= sum2:
        return lst1
    else:
        return lst2

print(larger_sum([1,9,5],[2,3,7]))
#----------------------------------------------------
#2
#Over 9000: Once number reaches 9000 of >, depending on numbers in 
#list, it will stop loop and return closed to 9000 or >
def over_nine_thousand(lst):
    sum = 0
    for number in lst:
        if sum < 9000:
            sum += number
        else:
            break
    return sum

print(over_nine_thousand([8000,900,120,5000]))
#-----------------------------------------------------
#3
#Max Num: will iterate over list and return maximum number in list
#works the same way as the built in max() function
def max_num(nums):
    maximum = (nums[0])
    for number in nums:
        if number > maximum:
            maximum = number
    return maximum

print(max_num([2,10,4,9,1]))
#----------------------------------------------------
#4
#Same Values: The function should return a list of the indices where
#the values were equal in lst1 and lst2.


def same_values(lst1, lst2):
    matching_list = []
    for i in range(len(lst1)):
            if lst1[i] == lst2[i]:
             matching_list.append(i)
    return matching_list

print(same_values([5,1,-10,3,3], [5,10,-10,3,5]))
#----------------------------------------------------
#5
#Reversed List: The function should return True if lst1 is the same as lst2 reversed.
#The function should return False otherwise.
def reversed_list(lst1, lst2):
    for i in range(len(lst1)):
        if lst1[i] != lst2[len(lst2)-1-i]:
            return False
    else:
        return True

print(reversed_list([1,2,3],[3,2,1]))
#------------------------------------------------------
#FUNCTIONS
#1
#Power: Returns number to the power of 10
def tenth_power(num):
    num=(num**10)
    return num #could also have had (return num ** 10)
print(tenth_power(2))
#------------------------------------------------------
#FUNCTIONS
#2
#Square Root: returns the square root of num
def square_root(num):
    return num ** 0.5
print(square_root(100))
#------------------------------------------------------
#FUNCTIONS
#3
#Win Percentage: This function should return out the total percentage of games
#won by a team based on these two numbers.
def win_percentage(wins, losses):
    total_percentage = wins/(losses+wins)*100
    return total_percentage
print(win_percentage(10,0))
#------------------------------------------------------
#FUNCTIONS
#4
#Average: returns the average of two numbers
def average(num1, num2):
    return (num1+num2)/2
print(average(1, 100))
#------------------------------------------------------
#FUNCTIONS
#5
#Remainder: The function should return the remainder of twice num1 divided by half of num2.
def remainder(num1, num2):
    return (num1*2)%(num2*0.5)
print(remainder(15,14))
#------------------------------------------------------
#FUNCTIONS ADVANCED
#1
#First Three Multiples: This function should print the first three multiples of num. Then, it should return the third multiple.
def first_three_multiples(num):
    print('\n'+str(num), '\n'+str(num*2), '\n'+str(num*3))
    return (num*3)
print(first_three_multiples(7))
#Other way to solve:
# def first_three_multiples(num):
#   print(num)
#   print(num * 2)
#   print(num * 3)
#   return num * 3
#------------------------------------------------------
#FUNCTIONS ADVANCED
#2
#Tip:This function should return the amount you should tip given a total and the percentage you want to tip.
def tip(total, percentage):
    return ((total*percentage)/100)
print(tip(10, 25))
#------------------------------------------------------
#FUNCTIONS ADVANCED
#3
#Bond, James Bond: Returns names as famous James Bond Intro quote
def introduction(first_name, last_name):
    return(last_name+', '+first_name+' '+last_name)
print(introduction("James", "Bond"))
#------------------------------------------------------
#FUNCTIONS ADVANCED
#4
#Dog Years: Returns name and age in dog years
def dog_years(name, age):
    age=(age*7)
    return(name+', you are '+str(age)+' years old in dog years')
print(dog_years("Lola", 16))
#------------------------------------------------------
#FUNCTIONS ADVANCED
#5
#All Operations: Uses all the math operators
def lots_of_math(a,b,c,d):
    ab=(a+b)
    cd=(c-d)
    print (ab)
    print (cd)
    print (ab*cd)
    return (cd%a)
print(lots_of_math(1,2,3,4))

#*************END OF CODING CHALLENGES ***************