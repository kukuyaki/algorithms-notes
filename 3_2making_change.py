#input: [a1,a2...an]
#for example: you have 1,3, 5, 10, 50 four kind of money
#plz input "1 3 5 10 50"
import json

def money_change(least_money,n,x):           
    if len(least_money) <= n:
        least_money.extend([None] * (n + 1 - len(least_money)))
    for i in range(n):
        if i == 0:
            least_money[0] = 0
            continue
        elif i in x:
            least_money[i] = 1
            continue
        candidate=[least_money[i-mo]+1 for mo in x if i-mo>=0]
        least_money[i]=min(candidate)
    print(least_money)
    return least_money


x=list(map(int, input("Enter all kind of money you have:").split(" ")))     #x = [all different value cash]
value = int(input("value that you want to change to money:"))               #least_money[what value you have] = the least number of cash you need to change

with open("change_money.json", "r") as f:                                   #for dynamic programming
    least_money = json.load(f)

if len(least_money) < value+1 and least_money[value] == None:               #in you dont have anwser, you use money_change function to look for it.
    least_money=money_change(least_money,value,x)
print(least_money[value])

with open("change_money.json", "w") as f:
    json.dump(least_money,f,indent=2)