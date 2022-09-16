def objCoincidence(array):
    return dict((p,array.count(p)) for p in array)


def getIndexOfElement(array,key,element):
    count=0
    for a in array:
        if a[key]==element:
            return count
        else:
            count+=1
    return -1