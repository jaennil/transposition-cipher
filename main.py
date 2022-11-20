import tkinter as tk

def button_listener():
    row = row_entry_var.get()
    col = col_entry_var.get()
    string = input_entry_var.get()

    icol = int(col)
    irow = int(row)

    if col.isdigit():
        if row.isdigit():
            for i in range(irow):
                for j in range(icol):
                    text = string[0]
                    string = string[1:]
                    if i % 2 == 0:
                        exec(f'l{i}_{j} = tk.Label(master=frame,text=text)')
                        exec(f'l{i}_{j}.grid(row={4 + i},column={3 + j})')
                    else:
                        exec(f'l{i}_{j} = tk.Label(master=frame,text=text)')
                        exec(
                            f'l{i}_{j}.grid(row={4 + i},column={3 + icol - j - 1})')


root = tk.Tk()
root.geometry('500x500')
frame = tk.Frame(master=root, width=500, height=500, bg='grey')
frame.grid(row=0, column=0, sticky='nsew')
row_entry_var = tk.StringVar(value='4')
row_entry = tk.Entry(master=frame, textvariable=row_entry_var)
row_entry.grid(row=0, column=0)
col_entry_var = tk.StringVar(value='7')
col_entry = tk.Entry(master=frame, textvariable=col_entry_var)
col_entry.grid(row=0, column=1)
input_entry_var = tk.StringVar(value='примермаршрутнойперестановки')
input_entry = tk.Entry(master=frame, textvariable=input_entry_var)
input_entry.grid(row=1, column=0)
button = tk.Button(master=frame, command=button_listener, text='start')
button.grid(row=1, column=1)
root.mainloop()
