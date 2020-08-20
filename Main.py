def count_steps(stepArray, stair, totalSteps=0):
    internalCount = 0
    if totalSteps <= stair:
        if totalSteps == stair:
            internalCount += 1
        else:
            for i in range(len(stepArray)):
                newSteps = stepArray[i] + totalSteps
                internalCount += count_steps(stepArray, stair, newSteps)
    return internalCount



print(count_steps([1,2,3], 4))