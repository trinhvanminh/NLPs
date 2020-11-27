import numpy as np
import matplotlib.pylab as plt
from tkinter import *
#Character Based Distance


def Calculate_Minimum_edit_distance(source, target, costs = (1, 1, 1)):    
    del_cost, ins_cost, sub_cost = costs
    n= len(source)
    m= len(target)
    MED_Matrix = np.zeros((n + 1, m + 1), dtype = 'int32')
    for i in range(1, n + 1):
        MED_Matrix[i][0] = MED_Matrix[i - 1][0] + del_cost
    for i in range(1, m + 1):
        MED_Matrix[0][i] = MED_Matrix[0][i - 1] + del_cost   
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
    # print(np.matrix(MED_Matrix))
    # print(MED_Matrix[n][m])
    # return MED_Matrix[n][m]
    return MED_Matrix

cost = (1, 1, 2)
a  = Calculate_Minimum_edit_distance('intention', 'execution', cost)
print(a,"\n",a[-1,-1])




  
root = Tk()  
for i in range(10): 
    for j in range(10):     
        e = Entry(root, width=5, fg='blue',font=('Arial',16,'bold')) 
        e.grid(row=i, column=j) 
        e.insert(END, a[i][j])

root.mainloop() 
