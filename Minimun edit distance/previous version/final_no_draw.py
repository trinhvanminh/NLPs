import tkinter as tk
import numpy as np


#constant value
costs = (1, 1, 2)
del_cost, ins_cost, sub_cost = costs
#----------------cal minimun edit distance-------------------------

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

#---------------User Interface---------------------------------------

#just insert the matrix
def ShowMatrix(MED_Matrix):
    root2 = tk.Tk() 
    root2.title("Cost Chart") 
    for i in range(len(source_input.get()) + 1): 
        for j in range(len(target_input.get()) + 1):     
            e = tk.Entry(root2, width=5, fg='blue',font=('Arial',16,'bold')) 
            e.grid(row=i, column=j) 
            e.insert(tk.END, MED_Matrix[i][j])
    # root2.mainloop()

#insert source, target, matrix 
def Show_MED_table(MED_Matrix):
    root2 = tk.Tk() 
    root2.title("Cost Chart")

    #get lenght
    target = " #"+target_input.get()
    m = len(target)
    source = " #"+source_input.get()
    n = len(source)

    #insert " #execution"
    for j in range(m):
        e = tk.Entry(root2, width=5, bg = '#e7e7e7', font=('Arial',16,'bold')) 
        e.grid(row=0, column=j) 
        e.insert(tk.END, target[j])
   
     #insert " #intention"
    for i in range(n):
        e = tk.Entry(root2, width=5, bg = '#e7e7e7', font=('Arial',16,'bold')) 
        e.grid(row=i, column=0) 
        e.insert(tk.END, source[i])

    #insert MinEdit
    for i in range(1, n):   
        for j in range(1, m):     
            e = tk.Entry(root2, width=5, bg = '#e7e7e7', font=('Arial',16)) 
            e.grid(row=i, column=j) 
            e.insert(tk.END, MED_Matrix[i-1][j-1])

    # root2.mainloop()

def Show_Med_Score():
    #calculate minimun edit distance
    MED_Matrix = Calculate_Minimum_edit_distance(source_input.get(),target_input.get(),costs)
    #get mininum edit distance
    Score_Med = tk.Label(root, text = "Cost: %d" % MED_Matrix[-1][-1], fg='blue', font=('Arial', 20, 'bold'))
    canvas1.create_window(200, 160, window = Score_Med)

    #show table via med matrix
    btn_ShowTable = tk.Button(text='Show Table', 
                              command=lambda:Show_MED_table(MED_Matrix),
                              font=('Arial', 9, 'bold'))
    canvas1.create_window(200, 200, window=btn_ShowTable)


root = tk.Tk()
root.title("Minimun Edit Distance")
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

#create btn
btn_Cal_Med = tk.Button(text='Calculate', 
                        command=Show_Med_Score,
                        font=('Arial', 9, 'bold'))
canvas1.create_window(200, 120, window=btn_Cal_Med)

#loop
root.mainloop()









#source: https://stackoverflow.com/questions/6920302/how-to-pass-arguments-to-a-button-command-in-tkinter