# Sal's Shipping
# David Maxwell

print ("\n")
weight = input("Please enter weight of item, in ibs: ")
weight = float(weight)
costofgroundprem =  125.00


if weight <= 2:
    costofground = weight * 1.5 + 20.00
    costofdrone = weight * 4.50
elif weight <= 6:
     costofground = weight * 3.00 + 20.00
     costofdrone = weight * 9.00
elif weight <= 10:
     costofground = weight * 4.00 + 20.00
     costofdrone = weight * 12.00
else: 
    costofground = weight * 4.75 + 20.00
    costofdrone = weight * 14.25

print ("\n")
print ("========================================")
print ("Current cost of Ground Shipping £" + str(costofground))
print ("========================================")
print ("\n")

user_input = input("Would you like to use our Premium Shipping Service, Y/N? ")
print ("\n")


if user_input == "y":
    print ("=====================================")
    print ("Premium Shipping total cost £ " + str(costofgroundprem))
    print ("=====================================")
    print ("\n")
else:
    print ("====================")
    print("Final cost £ " + str(costofground))
    print ("====================")
    print ("\n")

user_input1 = input("Would you like to try our Drone Shipping Service, Y/N? ")
print ("\n")

if user_input1 == "y":
    print ("====================================")
    print ("Final cost Drone Service £ " + str(costofdrone))
    print ("====================================")
    print ("\n")
else: 
    print ("===================================")
    print("Final cost Ground Service £ " + str(costofground))
    print ("===================================")
    print ("\n")
    
if (costofground < costofgroundprem) and (costofground < costofdrone):
    print ("*** We would recommend you use our Ground Shipping Service. ***")
    print ("\n")
    print ("Thank you for choosing our service.")
    print ("\n")
elif (costofgroundprem < costofground) and (costofgroundprem < costofdrone):
    print ("+=+ We would recommend you use our Ground Shipping Premium Service. +=+")
    print ("\n")
    print ("Thank you for choosing our service.")
    print ("\n")
else: 
    print ("+=+ We would recommend you use our Drone Shipping Service. +=+")
    print ("\n")
    print ("Thank you for choosing our service.")
    print ("\n")