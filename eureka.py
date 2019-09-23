import math

def sum_dig_pow(a, b): # range(a, b + 1) will be studied by the function
    # your code here
    value = a                                                    #value to check for eureka
    eureka = []                                                  #eureka values
    while (a <= value <= b):                                     #check all values in range [a,b]
        sum = 0                                                  #sumation to check against original
        digits = [int(i) for i in str(value)]                    #separate original integer into number list
        for each in digits:                                      #loop through each number in number list
            sum = sum + math.pow(each, (digits.index(each) + 1)) #add number squared to its index to sumation
        if sum == value:                                         #check for eureka between sum and original value
            eureka.append(value)                                 #if true, append to list
        value +=1                                                #increment to next number
    return eureka                                                #return list
