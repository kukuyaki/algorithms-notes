#use reccursion to build string
def mat_str(s_position,a,b):
    if b-a  == 1:
        return "(" +  str(a) + "*" + str(b) + ")"
    if b-a == 0:
        return str(a)
    index_i = s_position[a-1][b-2]
    return "(" + mat_str(s_position, a,index_i) + ")("+ mat_str(s_position,index_i+1,b) + ")"
#call mat_str function and then make it pretty!
def mat_str_clear(s_position,a,b):
    mat_str_item = mat_str(s_position,a,b)
    item = list("(" + mat_str_item + ")")
    keep = False
    for i in range(len(item)):
        if item[i] == "(":
            index_x = i
            keep = True
        elif item[i] == ")" and keep == True:
            keep = False
            item[index_x] = "r"
            item[i] = "r"
    return ''.join(item).replace("r","")
#build map
def MCM(p_i):
    matrix_num = len(p_i)-1
    matrix_time = [[0 for _ in range(matrix_num+1)] for _ in range(matrix_num+1)] #store how many multiplications each situation need.
    s_position = [[0 for _ in range(matrix_num-1)] for _ in range(matrix_num-1)] #store where to put brackets ")("
    for i in range(matrix_num):
        matrix_time[i][i] = 0
    for h in range(1,matrix_num):
        for w in range(1, matrix_num-h+1):
            i = w
            j = w + h
            min_k = 9999999999999999
            for k in range(i,j):
                temp_total = matrix_time[i][k] + matrix_time[k+1][j] + p_i[i-1]*p_i[k]*p_i[j]
                if temp_total < min_k:
                    min_k = temp_total
                    s_position[i-1][j-2] = k
            matrix_time[i][j] = min_k
    matrix_time = matrix_time[1:]
    for i in range(len(matrix_time)):
        matrix_time[i] = matrix_time[i][1:]
    return matrix_time, s_position
#main
p_i =[2,4,3,2,5,1]   #5 matrix: 2*4, 4*3, 3*2, 2*5, 5*1
multiplication_time, s_position = MCM(p_i)
print("multiplication_time:")
max_len = max(len(str(cell)) for row in multiplication_time for cell in row)
for row in multiplication_time:
    print(' '.join(f"{str(x):>{max_len+2}}" for x in row))
print("\ns_position:")
max_len = max(len(str(cell)) for row in s_position for cell in row)
for row in s_position:
    print(' '.join(f"{str(x):>{max_len+2}}" for x in row))
print(f"max mutiplication time is {multiplication_time[0][-1]}")
print(mat_str_clear(s_position,1,len(p_i)-1))