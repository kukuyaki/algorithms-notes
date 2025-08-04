#can seperate item 
#greedy algorithm
import json

def fKP(w,v,s):
    v_w=[]
    value_get=0
    for i in range(len(w)-1):
        v_w.append(v[i]/w[i])
    for i in range(len(w)):
        if s == 0:
            break
        item = max(v_w)
        index = v_w.index(item)
        if w[index] <= s:
            value_get += v[index]
            s-=w[index]
        elif w[index] > s:
            value_get += v_w[index]*s
            s = 0
        v_w[index] = min(v_w)-1
    return value_get, backpac_size



weight = [1,2,3]
value = [60,100,120]
backpac_size=int(input("Enter backpac size:"))

value_get, backpac_size = fKP(weight, value, backpac_size)
print(f"value_get: {value_get}\nbackpac_size: {backpac_size} ")


