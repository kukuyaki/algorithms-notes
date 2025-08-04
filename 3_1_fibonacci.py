import json

def fib(num):
    if num < len(list_fib):
        return list_fib[num]
    return fib(num-1) + fib(num-2)


def spfib(num):
    return 


list_fib = [0,1,1]
with open("list_fib.json", "r") as f:
    list_fib = json.load(f)
    
#Each time you run this code, list_fib.json will be extented by 10 more elements.
for i in range(len(list_fib),len(list_fib)+10):
    list_fib.append(list_fib[i-1] + list_fib[i-2])
# print(list_fib)

with open("list_fib.json", "w") as f:
    json.dump(list_fib, f, indent=2)

# print(fib(10))