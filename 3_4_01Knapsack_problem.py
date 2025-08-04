#item must be whole
#no greedy algorithm
#dynamic programming
#not friendly for human to read
import json

def KP01(w,v,tv,ti,s):
    for i in range(s+1):
        tv[0][i] = 0
        ti[0][i] =[]
    for i in range(1,len(w)+1):
        tv[i][0] = 0
        ti[i][0] =[]
        for k in range(1,s+1):
            if w[i-1] <= k:
                if v[i-1] + tv[i-1][k-w[i-1]] > tv[i-1][k]:
                    tv[i][k] = v[i-1] + tv[i-1][k-w[i-1]]
                    ti[i][k] = ti[i-1][k-w[i-1]] + [i]
                else:
                    tv[i][k] = tv[i-1][k]
                    ti[i][k] = ti[i-1][k] 
            else:
                tv[i][k] = tv[i-1][k]
                ti[i][k] = ti[i-1][k] 
    
    return tv,ti
weight = [1,2,3,4]
value = [60,100,120,500]
backpac_size = 5
table_v =[[None for i in range(backpac_size+1)] for j in range(len(weight)+1)]
table_item =[[None for i in range(backpac_size+1)] for j in range(len(weight)+1)]
# print(table_item)
table_v, table_item = KP01(weight, value, table_v, table_item, backpac_size)

print("table_v:")
max_len = max(len(str(cell)) for row in table_v for cell in row)
for row in table_v:
    print(' '.join(f"{str(x):>{max_len+2}}" for x in row))

print("\ntable_i:")
max_len = max(len(str(cell)) for row in table_item for cell in row)
for row in table_item:
    print(' '.join(f"{str(x):>{max_len+2}}" for x in row))

print(f"value get: {table_v[-1][-1]}")
print(f"item get: {table_item[-1][-1]}")


