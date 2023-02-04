SampleList= [1,2,3,3,3,3,4,5]
#created a function name uniquelist
def uniquelist(l):
    result=set(l)           #converting list to set to extract unique elements in the list
    return list(result)     #returning the result by converting to list
print(SampleList)
print("unique elements:",uniquelist(SampleList))       #function-call