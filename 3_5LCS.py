
#generate map
def LCS_m(x,y):
    list_LCS =[[0 for _ in range(len(y)+1)] for _ in range(len(x)+1) ]

    for i in range(1,len(x)+1):
        for j in range(1,len(y)+1):
            if x[i-1] == y[j-1]:
                
                list_LCS[i][j] = list_LCS[i-1][j-1] + 1 
            elif x[i-1] != y[j-1]:
                list_LCS[i][j] = max(list_LCS[i-1][j], list_LCS[i][j-1])
    return list_LCS

#find LCS string
def LCS(x,y):
    list_LCS = LCS_m(x,y)
    i = len(list_LCS)-1
    j = len(list_LCS[0])-1
    maxstring = ""
    while i != 0 and j != 0:
        if x[i-1] == y[j-1]:
            print(i-1)
            maxstring = x[i-1] + maxstring
            i-=1
            j-=1
        elif list_LCS[i-1][j] > list_LCS[i][j-1]:
            i-=1
        else:
            j-=1
    return maxstring, list_LCS

x = "jkkdfsljlksjflnn,mn,masd,mfn"
y = "wpeuwnuewoiybwtnmwnyrehkhalksf"


maxstring, list_LCS = LCS(x,y)

for i in list_LCS:
    print(i)
print(list_LCS[-1][-1])
print(maxstring)
