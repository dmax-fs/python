#Strings
#----------------------------------------------------------------
#Takes the first 3 letters of the first_name and last_name to
#produce a username
first_name = "Julie"
last_name = "Blevins"

def account_generator(first_name, last_name):
  account_name = first_name[:3]+last_name[:3]
  return account_name

new_account = account_generator(first_name, last_name)

print(new_account)
#----------------------------------------------------------------
#same as above but this time, last 3 letters of names for temp password
first_name = "Reiko"
last_name = "Matsuki"

def password_generator(first_name, last_name):
  password = first_name[-3:] + last_name[-3:]
  return password

temp_password = password_generator(first_name, last_name)
print(temp_password)
#----------------------------------------------------------------
#This would be how to fix a user_name that's been created with the wrong spelling
first_name = "Bob"
last_name = "Daily"

fixed_first_name = ("R" + first_name[-2:])

print(fixed_first_name)
#----------------------------------------------------------------
#putting \ before "'s that you want to be included in the string"
password = "theycallme\"crazy\"91"
#----------------------------------------------------------------
#emulates the len() funcation
def get_length(word):
    counter = 0
    for letter in word:
        counter += 1
        print(counter)
    return word
print(get_length('sausage'))
##
#This returns just the final number of the count, exactly like len()
def get_length(word):
    counter = 0
    for letter in word:
        counter += 1
    return counter
#----------------------------------------------------------------
#check if a letter is in a word
def letter_check(word, letter):
  for i in word:
    if i == letter:
     return True
  return False
#----------------------------------------------------------------
#handy 'in' funcation to know
print("e" in "blueberry")
# => True
print("a" in "blueberry")
# => False
print("blue" in "blueberry")
# => True
print("blue" in "strawberry")
# => False
print("e" in "blueberry" and "e" in "carrot")
# => False
print("e" in "blueberry" and not "e" in "carrot")
# => True
#----------------------------------------------------------------
#function that will check common characters in a string and return common ones
def common_letters(string_one, string_two):
  common=[]
  for i in string_one:
      if i in string_two:
          common.append(i)
          return i
print(common_letters('banana', 'cream'))

#solution from Codecademy
def common_letters(string_one, string_two):
  common = []
  for letter in string_one:
    if (letter in string_two) and not (letter in common):
      common.append(letter)
  return common

#----------------------------------------------------------------
#Final Strings task 12/12
#two functions that generate user_name and password
def username_generator(first_name, last_name):
  user_name = first_name[:3]+last_name[:4]
  return user_name

user_name = (username_generator('Abe', 'Simpson'))

print(user_name)

def password_generator(user_name):
  password = ''
  for i in range (0, len(user_name)):
      password += user_name[i-1]
  return password
print(password_generator(user_name))
#----------------------------------------------------------------
#String Methods
poem_title = "spring storm"
poem_author = "William Carlos Williams"

poem_title_fixed = poem_title.title()
print(poem_title)
print(poem_title_fixed)

poem_author_fixed = poem_author.upper()
print(poem_author)
print(poem_author_fixed)
#------------------------------------------------------------------------
#These are useful, first one seperate names in long list and the second one
#will itireate over the names and only store the last names in a list
authors = "Audre Lorde,Gabriela Mistral,Jean Toomer,An Qi,Walt Whitman,Shel Silverstein,Carmen Boullosa,Kamala Suraiyya,Langston Hughes,Adrienne Rich,Nikki Giovanni"

author_names = authors.split(',')
print (author_names)

author_last_names=[]
for names in author_names:
  author_last_names.append(names.split()[-1])
print (author_last_names)
#------------------------------------------------------------------------
#use this method to join individual words together to make a sentence
reapers_line_one_words = ["Black", "reapers", "with", "the", "sound", "of", "steel", "on", "stones"]

reapers_line_one = (' '.join(reapers_line_one_words))

print(reapers_line_one)
#------------------------------------------------------------------------
#used to strip words out from unnecessary characters, and add to a list
love_maybe_lines = ['Always    ', '     in the middle of our bloodiest battles  ', 'you lay down your arms', '           like flowering mines    ','\n' ,'   to conquer me home.    ']

love_maybe_lines_stripped = []

for lines in love_maybe_lines:
  love_maybe_lines_stripped.append(lines.strip()) # for loop to iterate through the poem and added to empty list
  
  love_maybe_full = '\n'.join(love_maybe_lines_stripped) #poem is joined up via the \n (new lines) to make readable

print(love_maybe_full)
#----------------------------------------------------------------
#Replace will replace all instances of first argument with second. In the example we want to replace
#all words that say Tomer with Toomer.
toomer_bio_fixed = toomer_bio.replace('Tomer', 'Toomer')
print(toomer_bio_fixed)
#----------------------------------------------------------------
#find at what index a certain word or letter is, in the example "disown" is index pos. 20
god_wills_it_line_one = "The very earth will disown you"

disown_placement = (god_wills_it_line_one.find('disown'))
print(disown_placement)
#----------------------------------------------------------------
#using the .format method 
def poem_title_card(title, poet):
  return "The poem \"{}\" is written by {}.".format(title, poet)

print(poem_title_card("I Hear America Singing", "Walt Whitman"))
#----------------------------------------------------------------
#using the .format method, but this time including the keywords in the code this
#makes the code more readable.
def poem_description(publishing_date, author, title, original_work):
  poem_desc = "The poem {title} by {author} was originally published in {original_work} in {publishing_date}.".format(publishing_date=publishing_date, author=author, title=title, original_work=original_work)
  return poem_desc

author = "Shel Silverstein"
title = "My Beard"
original_work = "Where the Sidewalk Ends"
publishing_date = "1974"

my_beard_description = poem_description(publishing_date, author, title, original_work)

print(my_beard_description)
#----------------------------------------------------------------
#FINAL STRING LESSON, EXAMPLE OF EVERYTHING!
highlighted_poems = "Afterimages:Audre Lorde:1997,  The Shadow:William Carlos Williams:1915, Ecstasy:Gabriela Mistral:1925,   Georgia Dusk:Jean Toomer:1923,   Parting Before Daybreak:An Qi:2014, The Untold Want:Walt Whitman:1871, Mr. Grumpledump's Song:Shel Silverstein:2004, Angel Sound Mexico City:Carmen Boullosa:2013, In Love:Kamala Suraiyya:1965, Dream Variations:Langston Hughes:1994, Dreamwood:Adrienne Rich:1987"

highlighted_poems_list = highlighted_poems.split(',')

highlighted_poems_stripped = []

for lines in highlighted_poems_list:
  highlighted_poems_stripped.append(lines.strip())
  
print(highlighted_poems_stripped)

highlighted_poems_details = []

for lines in highlighted_poems_stripped:
  highlighted_poems_details.append(lines.split(':'))

titles = []
poets = []
dates = []

for lines in highlighted_poems_details:
  titles.append(lines[0])
  poets.append(lines[1])
  dates.append(lines[2])

for i in range(0, len(highlighted_poems_details)):
  print("The poem {} was published by {} in {}".format(titles[i], poets[i], dates[i]))
  #----------------------------------------------------------------
