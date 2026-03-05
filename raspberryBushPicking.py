def getBestBushes(n: str, values: str):
    round(int(n))  # Useless, really, this exists just to meet the requirements of the task
    prev2 = 0
    prev1 = 0
    values = str(values).split()  # Turn values into a list

    # Iterate through all the values
    for i in values:
        current = max(prev1, int(i) + prev2)  # Set the current result

        prev2 = prev1
        prev1 = current

    return prev1


num = input()
worth = input()
print(getBestBushes(num, worth))
