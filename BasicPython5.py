#Checks whether or not the decimal representation of an integer contains
#any odd digits

#Enter integer
integer = input("Enter integer: ")

def functionQ3(integer):
    integerString = str(integer)

    digitList = []
    oddDigitsCounter = 0

    for x in integerString:
        digitList.append(int(x))
    

    for y in digitList:
        if (y%2 != 0):
            oddDigitsCounter += 1
    

    return oddDigitsCounter == 0





print(functionQ3(integer))