import itertools

#This thing makes all binary strings of length n
def binseq(k):
    return [''.join(x) for x in itertools.product('01', repeat=k)]

n = 10
forbid = '010'
for i in range(n):
    flag = 1;
    myList = binseq(i)
    tag = 0
    for j in range(len(myList)):
        flag = myList[j-tag].find(forbid)
        if flag != -1:
            myList.pop(j-tag)
            tag += 1
    print(len(myList))

