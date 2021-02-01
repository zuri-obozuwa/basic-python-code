#Generator that generates positive integers up to maximum dividend,
# and divides it by the divisor

#User inputs the maximum dividend

maxDividendString = input("Enter the Maximum Dividend: ")
maxDividend = int(maxDividendString) 

#User inputs the divisor

divisorString = input("Enter the Divisor: \n")
Divisor = int(divisorString) 


print("The Maximum Dividend is", maxDividend, "and the Divisor is", Divisor, "\n")






#Function that generates the numnbers
def generator(maxDividend, Divisor):

    #Dividend starts at 0 and then iterates
    Dividend = 0

    #Empty Array to store the generated numbers
    Sequence = []

    for c in range(maxDividend):
        Dividend += 1

        if (Dividend%Divisor == 0):
            Sequence.append(Dividend)
    

    return(Sequence)


Sequence = generator(maxDividend, Divisor)

print("The numbers generated are:", Sequence)

#Sum of all positive integers less than 102030:

print("The new Maximum Dividend is 102029")
print("The Divisor is still 3 \n")

maxDividend = 102029
Divisor = 3

Sequence = generator(maxDividend, Divisor)

Sum = sum(Sequence)

print("The sum of the positive integers less than 102030 which are divisible by 3 is:")

print(Sum)




