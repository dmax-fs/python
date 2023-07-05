# IMPORTING MODULES IN PYTHON
from datetime import datetime
current_time = datetime.now()
print(current_time)
#This will import and print the current date and time in the terminal
#----------------------------------------------------------------
import random
# Create random_list
random_list = [random.randint(1,100) for i in range(101)]
# Create randomer_number below
randomer_number = random.choice(random_list)
print(randomer_number)
#This will generate a list of random numbers, in the range 1-100, then choose one randomly
#----------------------------------------------------------------
import seaborn # says not accessed but it does work
from matplotlib import pyplot as plt # no such library exists on local machine
import random
# Add your code below:
numbers_a = range(1,13)
numbers_b = random.sample(range(1000),12)
plt.plot(numbers_a, numbers_b)
plt.show()
#firstly aliasing has been used to change the pyplot to plt, which makes it shorter to call
#numbers_b selects 12 random numbers from the range 1-1000.
#The plt.plot takes two variables as arguments and plt.show() displays these as a table
#From what I can see it looks like it would work using Jupyter.
#----------------------------------------------------------------
# Import Decimal below:
from decimal import Decimal

two_decimal_points = Decimal("0.2") + Decimal("0.69")
print(two_decimal_points)

four_decimal_points = Decimal('0.53') * Decimal('0.65')
print(four_decimal_points)
#the Decimal library will make calculations with float numbers and rounding easier
#----------------------------------------------------------------
# Import library below:
from library import always_three    #library is a seperate file (library.py) that contains a function
                                    #called always_three
# Call your function below:
print(always_three())
#
#----------------------------------------------------------------