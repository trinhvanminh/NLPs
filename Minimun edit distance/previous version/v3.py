import tkinter as tk
import numpy as np



root = tk.Tk()

#create a canvas window
canvas1 = tk.Canvas(root, width = 400, height = 300)
canvas1.pack()

#create labels
source_label = tk.Label(root,text = "Source")
canvas1.create_window(100,60,window=source_label)
target_label = tk.Label(root,text = "Target")
canvas1.create_window(300,60,window=target_label)

#create textbox --> get input
source_input = tk.Entry (root) 
canvas1.create_window(100, 80, window=source_input)

target_input = tk.Entry (root) 
canvas1.create_window(300, 80, window=target_input)



def Calculate_Minimum_edit_distance(): 
    source = source_input.get()
    target = target_input.get()
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
    Score_Med = tk.Label(root, text = "Med: %d" % MED_Matrix[n][m], font=('helvetica', 20, 'bold'))
    canvas1.create_window(200, 160, window = Score_Med)
    btn_ShowChart = tk.Button(text='Show Chart')
    canvas1.create_window(200, 200, window=btn_ShowChart)
    return MED_Matrix



# matrix_result  = Calculate_Minimum_edit_distance(source.get(), target.get(), cost)
# print(matrix_result,"\n",matrix_result[-1,-1])


costs = (1, 1, 2)
btn_Cal_Med = tk.Button(text='Calculate Minimun Edit Distance', 
                        command=Calculate_Minimum_edit_distance,
                        font=('helvetica', 9, 'bold'))
canvas1.create_window(200, 120, window=btn_Cal_Med)




root.mainloop()