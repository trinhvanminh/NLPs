import numpy as np
import tkinter as tk

costs = (1, 1, 2)
del_cost, ins_cost, sub_cost = costs

def Calculate_Minimum_edit_distance(source, target, costs = (1, 1, 1)): 
    del_cost, ins_cost, sub_cost = costs
    n = len(source)
    m = len(target)
    MED_Matrix = np.zeros((n + 1, m + 1), dtype = 'int32')
    for i in range(1, n + 1):
        MED_Matrix[i][0] = MED_Matrix[i - 1][0] + del_cost
    for i in range(1, m + 1):
        MED_Matrix[0][i] = MED_Matrix[0][i - 1] + ins_cost   
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if(source[i - 1] == target[j - 1]):
                MED_Matrix[i][j] = min(
                                       [MED_Matrix[i - 1][j] + del_cost,
                                        MED_Matrix[i-1][j - 1] + 0,
                                        MED_Matrix[i][j - 1] + ins_cost])
            else:
                MED_Matrix[i][j] = min(
                                       [MED_Matrix[i - 1][j] + del_cost,
                                        MED_Matrix[i - 1][j - 1] + sub_cost,
                                        MED_Matrix[i][j - 1] + ins_cost])
    return MED_Matrix

def Show_MED_table(MED_Matrix):
    root2 = tk.Tk() 
    root2.title("Cost Chart")


    target = " #execution"
    m = len(target)
    source = " #intention"
    n = len(source)

    #insert " #execution"
    for j in range(m):
        e = tk.Entry(root2, width=5, fg='blue',font=('Arial',16,'bold')) 
        e.grid(row=0, column=j) 
        e.insert(tk.END, target[j])
   
     #insert " #intention"
    for i in range(n):
        e = tk.Entry(root2, width=5, fg='blue',font=('Arial',16,'bold')) 
        e.grid(row=i, column=0) 
        e.insert(tk.END, source[i])

    #insert MinEdit
    for i in range(1, n):   
        for j in range(1, m):     
            e = tk.Entry(root2, width=5, fg='blue',font=('Arial',16,'bold')) 
            e.grid(row=i, column=j) 
            e.insert(tk.END, MED_Matrix[i-1][j-1])


    # root2.mainloop()
    return root2

#just insert the matrix
def ShowMatrix(MED_Matrix):
    root2 = tk.Tk() 
    root2.title("Cost Chart") 

    target = "execution"
    m = len(target)
    source = "intention"
    n = len(source)

    for i in range(n + 1): 
        for j in range(m + 1):     
            e = tk.Entry(root2, width=5, fg='blue',font=('Arial',16,'bold')) 
            e.grid(row=i, column=j) 
            e.insert(tk.END, MED_Matrix[i][j])
    # root2.mainloop()
    return root2

MED_Matrix = Calculate_Minimum_edit_distance("intention","execution",costs)


# Show_MED_table(MED_Matrix)
# ShowMatrix(MED_Matrix)


source = "intention"
target = "execution"
n = len("intention")
m = len("execution")

root2 = Show_MED_table(MED_Matrix)


def draw(root2, MED_Matrix, i, j):
    #tô màu vị trí min edit distance
    e = tk.Entry(root2, width=5, bg = '#909090' ,font=('Arial',16,'bold')) 
    e.grid(row=i+1, column=j+1) 
    e.insert(tk.END, MED_Matrix[i][j])
    if(i == 0 and j == 0):
        return root2.mainloop()
    
    if source[i-1] == target[j-1]:
        #đường chéo sẽ là đường có cost = 0 nhỏ nhất(do 2 chữ cái bằng nhau)
        draw(root2, MED_Matrix, i - 1, j - 1)
    else:
        #lấy các trường hợp cost có thể
        del_edit = MED_Matrix[i - 1][j] + del_cost
        sub_edit =  MED_Matrix[i-1][j - 1] + 2 
        ins_edit = MED_Matrix[i][j - 1] + ins_cost


        #các số tạo ra 8 (số med, số cuối, số min) 
        edit_list = []
        if del_edit == MED_Matrix[i][j]:
            edit_list.append(MED_Matrix[i - 1][j])
        if sub_edit == MED_Matrix[i][j]:
            edit_list.append(MED_Matrix[i-1][j - 1])
        if ins_edit == MED_Matrix[i][j]:
            edit_list.append(MED_Matrix[i][j - 1])
        
        #lấy số thực sự nhỏ nhất và tạo ra số 8

        min_val = min(edit_list)
        
        if MED_Matrix[i - 1][j - 1] == min_val:
            draw(root2, MED_Matrix, i - 1, j - 1)
        if MED_Matrix[i - 1][j] == min_val:
            draw(root2, MED_Matrix, i - 1, j)
        if MED_Matrix[i][j - 1] == min_val:
            draw(root2, MED_Matrix, i, j - 1)
        

draw(root2, MED_Matrix, n, m)
