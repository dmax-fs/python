#Loop exmaples

#While loops

while True:
    #do something
    
#Example of a loop that advances an index through a sequence of characters
#until finding an entry with value 'X' or reaching end of sequence.
    j=0
while j<len(data) and data[j] !='X':
    j += 1
#len function returns the length of the sequence such as a list or string


#for loops

#computing the sum of a list of numbers. same as in-build 'sum' function
total = 0 
for val in data:
    total += val
    
#find the maximum value in a list of elements. same as in-build 'max' function
    biggest = data[0]
    for val in data:
        if val > biggest:
            biggest = val
#same as above but index based
    big_index = 0
    for j in range(len(data)):
        if data[j] > data[big_index]:
            big_index = j
            

#functions

#The following function counts the numbers of occurrences of a given target value
#within any form of iterable data set.

    def count(data, target):
        n=0
        for item in data:
            if item == target:
                n += 1
        return

#Return statement: if the conditional within the loop body is satisfied, the return True
#statement is executed and the function immediately ends, with True as target value

#Generators
#the most convenient technique for creating iterators in python

#determine all factors of a positive integer
#traditional function

    def factors(n):
        results = []
        for k in range(1,n+1):
            if n % k == 0:
                results.append(k)
        return results
    
    print (factors(n))
    
#implimentation of a generator for computing the same factors

    def factors(n):
        for k in range(1,1+n):
            if n % k == 0:
                yield k 
        

    
