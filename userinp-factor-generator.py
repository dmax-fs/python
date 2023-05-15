#generator test
n = input("Please enter a number to be factored: ")     #Takes input from the user
n = int(n)                                              #Stores the number as an integer

def factors(n): 
        results = []                                    #Stores the results in a list
        for k in range(1,n+1):                          #loop through the numbers from 1 to n+1
            if n % k == 0:                              #if the number is divisible by k, add it to the list
                results.append(k)                       #add the number to the list
        return results  #                               #list of the factors stored in results

print ("\nFactors of " + str(n)+ " are :" + str(factors(n))+ "\n")
