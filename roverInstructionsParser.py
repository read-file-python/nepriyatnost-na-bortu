def parseInstructions(inst: str):
    stack = []
    result = ""
    currentIterCount = ""

    # Iterate through instructions
    for i in inst:
        if i.isdigit():  # Digit, add it to the iteration count
            currentIterCount += i
        elif i == "[":  # Start of a loop, add the iteration count and the accumulated string to the stack
            stack.append((result, int(currentIterCount)))
            result = ""
            currentIterCount = ""
        elif i == "]":  # End of a loop, get all stack symbols, then, add them to the result times the iteration count
            accumulatedSymbols, times = stack.pop()
            result = accumulatedSymbols + (result * times)
        else:  # Regular symbol, add it to the result
            result += i

    return result


print(parseInstructions("2[3[a]3[b]]23[c]"))
