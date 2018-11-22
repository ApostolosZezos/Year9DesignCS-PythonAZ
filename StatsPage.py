import tkinter as tk


root = tk.Tk()

output = tk.Text(root, background = "blue", height = 10, width = 50)
output.config(state = "disable")
output.grid(row = 0, column = 0, columnspan = 2)

btnStat1 = tk.button(root, text = "Stat 1")
btnStat1.grid(row = 1, column = 0, stick = "NESW")



root.mainloop()