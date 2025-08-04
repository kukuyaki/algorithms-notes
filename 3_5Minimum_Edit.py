#Minimum step for change x string to y string

def minE(x,y):
    listE = [[0 for _ in y+" "] for _ in x+" "]
    for i in range(len(x)+1):
        listE[i][0] = i
    for j in range(len(y)+1):
        listE[0][j] = j

  
    for i in range(1,len(x)+1):
        for j in range(1,len(y)+1):
            if x[i-1] == y[j-1]:
                listE[i][j] = listE[i-1][j-1]
                continue
            listE[i][j] = min(listE[i-1][j], listE[i][j-1], listE[i-1][j-1])+1
    return listE




x = "acbabca"
y = "babcbac"
listE = minE(y,x)
for w in listE:
    print(w)
print(f"minimum edit distance: {listE[-1][-1]}")