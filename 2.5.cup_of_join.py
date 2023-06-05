def join1(*inputL, sep='-'):
    if not inputL:
        return None
    # creating a new empty list for storing result
    resultList = []

    # Traversing in till the length of the input list of lists
    for m in inputL:
        for n in m:
            resultList.append(n)
        resultList.append(sep)
    return(resultList)


print(join1([1],[2,2],[4,4],[3,3,3],sep='**'))
