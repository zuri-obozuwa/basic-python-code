#Returns lists of ascending numbers

#User inputs the value of N
nString = input("Enter a value for N: ")

N = int(nString)


def functionQ2(N):
    #Empty list to store the lists of numbers
    Sequence = []
    N+=2

    for x in range(1,N):
        insideSequence = []
        for y in range(1,x):
            if y!=0:
                insideSequence.append(y)
        Sequence.append(insideSequence)

    #Removes empty first term
    Sequence.pop(0)




    return Sequence 


Sequence = functionQ2(N)

print(Sequence)