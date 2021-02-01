#Calculating sum of first 100 even fibonacci numbers

Sequence = [1,1]

#Fibonacci Sequence
for x in range(2,300):
    Sequence.append(Sequence[x-2]+Sequence[x-1])



#Even Fibonnacci Sequence (first 100 numbers)
evenSequence = []
for x in Sequence:
    if (x%2==0):
        evenSequence.append(x)
        if len(evenSequence) == 100:
            break




print(evenSequence)









