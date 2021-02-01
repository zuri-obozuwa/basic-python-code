
#when passed a decimal digit Y, returns thevalue of Y+YY+YYY+YYYY


#Enter digit

condition = 0
while condition == 0:
    integer = int(input("Enter digit: "))
    if (integer >= 0) & (integer <= 9):
        condition = 1
        break

    print("Invalid input")


def functionQ4(X):

    XX = int(str(X)+ str(X))
    XXX = int(str(X)+ str(X) + str(X))
    XXXX = int(str(X)+ str(X) + str(X) + str(X))
    
    result = X + XX + XXX + XXXX

    return result


print(functionQ4(integer))