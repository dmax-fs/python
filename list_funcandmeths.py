zero_to_seven = range(8)
print(list(zero_to_seven))

#prints a list of numbers in the range 0 through 7
#the range has to be 1 more than the numbers wanting to
#be displayed.

range_diff_five = range(0, 40, 5)
print(list(range_diff_five))

#This prints a list of numbers from 0 to 39 with incriments
#of 5 (skipts every 5th number)

long_list = [1, 5, 6, 7, -23, 69.5, True, "very", "long", "list", "that", "keeps", "going.", "Let's", "practice", "getting", "the", "length"]

big_range = range(2, 3000, 10)

long_list_len = len(long_list)
print(long_list_len)
#saves long_list length as a variable and prints the length of long_list

big_range_length = len(big_range)
print(big_range_length)
#prints the length of the range of items in the the big_range, range

letters = ["a", "b", "c", "d", "e", "f", "g"]
sliced_list = letters[1:6]
print(sliced_list)
#["b", "c", "d", "e", "f"]

fruits = ["apple", "cherry", "pineapple", "orange", "mango"]
print(fruits[:3]) # can use fruits[-2:] to start slicing from end of list
#it all depends of where the ':' is in the argument to where sliing starts
#['apple', 'cherry', 'pineapple']

how_many_apples = fruits.count("apple")
print(how_many_apples)
#will display how many times 'apples' appears in list

names = ["Ron", "Hermione", "Harry", "Albus", "Sirius"]
names.sort()
#will sort names in alphabetical order
#if names.sort(reverse=True) this sort in reverse alpha order

games = ["Portal", "Minecraft", "Pacman", "Tetris", "The Sims", "Pokemon"]

# Your code below:
games_sorted = sorted(games)
print(games)
print(games_sorted)
#this is similar to the above method, but instead is a built in function

owners = ["Jenny", "Alexus", "Sam", "Grace"]
dogs_names = ["Elphonse", "Dr. Doggy DDS", "Carter", "Ralph"]

names_and_dogs_names = zip(owners, dogs_names)
list_of_names_and_dogs_names = list(names_and_dogs_names)
print(list_of_names_and_dogs_names)

#This will combine two lists together and pack them into a new object
#The new object then has to be converted to a list which can
#then be printed to the terminal, which has 1st element of the 1st list
#followed by the 1st element of the 2nd list... and so on.