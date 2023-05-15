#generator test
n = input("Please enter a number to be factored: ")
n = int(n)

def factors(n):
        results = []
        for k in range(1,n+1):
            if n % k == 0:
                results.append(k)
        return results

print ("\nFactors of " + str(n)+ " are :" + str(factors(n))+ "\n")
