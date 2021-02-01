#Function that identifies numbers that appear in both arrays


#Choose number of elements
numberOfElements = input("Enter the number of elements per array: ")
N = int(numberOfElements)

#Array A
arrayA = []
for x in range(N):
    elementString = input("Array A: Enter Element: " )
    element = int(elementString)
    arrayA.append(element)

print("Array A: ", arrayA)

#Array B
arrayB = []
for x in range(N):
    elementString = input("Array B: Enter Element: " )
    element = int(elementString)
    arrayB.append(element)

print("Array B: ", arrayB)

#Numbers that appear in both Array A and Array B: 
arrayC =[]


for x in arrayA:
    if x in arrayB:
        arrayC.append(x)


#Removes repeated values
arrayC = list(set(arrayC))

print("Array C consists of the numbers that appear in both Array A and Array B")


#Final array
print("Array C: ", arrayC)

