oldNum = 0
newNum = 1
numSum = 0

# Print the first 2 nums outside the loop for optimization purposes
print(oldNum)
print(newNum)

# Iterate 98 times to get the remaining numbers in the sequence
for i in range(98):
    numSum = oldNum + newNum
    print(numSum)
    oldNum = newNum
    newNum = numSum
