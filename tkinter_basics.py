from tkinter import *
import tkinter.ttk as ttk
from tkinter import scrolledtext, messagebox, filedialog, Menu
from os import path

# def clicked():
#     res = "Welcome "+ txt.get()+" "+combo.get()
#     lbl.configure(text=res)

window = Tk()
window.title("Starter App")
window.geometry('600x400')

# lbl = Label(window, text="Hello World", font=("Arial Bold", 20))
# lbl.grid(column=0, row=0)

# btn = Button(window, text="Click me", bg="orange", fg="red", command=clicked)
# btn.grid(column=0, row=1)

# txt = Entry(window, width=30)
# txt.grid(column=1, row=1)
# txt.focus()

# combo = ttk.Combobox(window)
# combo.grid(column=0, row=2)
# combo['values'] = (1,2,3,4,5,"Text")
# combo.current(1)

# chk_var = BooleanVar()
# chk_var.set(False)
# chkbx = ttk.Checkbutton(window, text="Check box", var=chk_var)
# chkbx.grid(column=0, row=3)

# def radioClicked():
#     print(selected.get())

# selected = IntVar()
# rdbtn1 = ttk.Radiobutton(window, text="First", value=1, variable=selected, command=radioClicked )
# rdbtn2 = ttk.Radiobutton(window, text="Second", value=2, variable=selected, command=radioClicked )
# rdbtn1.grid(column=0, row=4)
# rdbtn2.grid(column=1, row=4)

# def clearScrolled():
#     scrltxt.delete(1.0, END)

# scrltxt = scrolledtext.ScrolledText(window, width= 30, height=10)
# scrltxt.insert(INSERT,"Enter your text")
# scrltxt.grid(column=0, row=5)

# scrlbtn = Button(window, text="Clear Scrolled text", command=clearScrolled)
# scrlbtn.grid(column=1, row=5)

# def callShowInfo():
#     messagebox.showinfo('Message Title', 'Message Content')

# msgbtn1 = Button(window, text="ShwoInfoMessage", command=callShowInfo)
# msgbtn1.grid(column=0, row=6)

# def callShowError():
#     messagebox.showerror('Message Title', 'Message Content')

# msgbtn2 = Button(window, text="ShwoErrorMessage", command=callShowError)
# msgbtn2.grid(column=1, row=6)

# def callShowWarning():
#     messagebox.showwarning('Message Title', 'Message Content')

# msgbtn3 = Button(window, text="ShwoWarningMessage", command=callShowWarning)
# msgbtn3.grid(column=3, row=6)

    
# def askQuestion():
#     res = messagebox.askyesno('Message title','Message content')
#     print(res)

# msgbtn4 = Button(window, text="AskYesorNo", command=askQuestion)
# msgbtn4.grid(column=1, row=7)

# def askAnotherQuestion():
#     res = messagebox.askyesnocancel('Message title','Message content')
#     print(res)
#     if res == None:
#         print("Pressed cancel button")

# msgbtn5 = Button(window, text="AskYesorNoCancel", command=askAnotherQuestion)
# msgbtn5.grid(column=1, row=8)

# def changed():
#     print(var.get())

# var = IntVar()
# var.set(20)

# spin = Spinbox(window, from_=0, to=100, width=5, textvariable=var, command=changed)
# spin.grid(column=0, row=9)


# spin = Spinbox(window, values=(10,20,30), width=5)
# spin.grid(column=0, row=9)

# pbar = ttk.Progressbar(window, length=200)
# pbar['value'] = 70
# pbar.grid(column=1, row=1)

# style = ttk.Style()
# style.theme_use('default')
# style.configure("black.Horizontal.TProgressbar", background='black')

# pbar = ttk.Progressbar(window, length=200, style='black.Horizontal.TProgressbar')
# pbar['value'] = 70
# pbar.grid(column=1, row=1)

# def openFIle():
#     file = filedialog.askopenfilename(filetypes = (("Text files","*.txt"),("all files","*.*")), initialdir=path.dirname(path.abspath(__file__)))
#     print(file)


# msgbtn5 = Button(window, text="AskYesorNoCancel", command=openFIle)
# msgbtn5.grid(column=1, row=1)


# def clicked():
#     print("Another")

# menu = Menu(window)
# new_item = Menu(menu)
# new_item.add_command(label='New')
# new_item.add_separator()
# new_item.add_command(label='Another', command=clicked)
# menu.add_cascade(label='File', menu=new_item)
# menu.add_cascade(label='Edit', menu=new_item)
# window.configure(menu=menu)

tab_control = ttk.Notebook(window)
tab1 = ttk.Frame(tab_control)
tab2 = ttk.Frame(tab_control)
tab_control.add(tab1, text='First')
tab_control.add(tab2, text='Second')
lbl1 = Label(tab1, text= 'label1', padx=50, pady=50)
lbl1.grid(column=0, row=0)
lbl2 = Label(tab2, text= 'label2', padx=50, pady=50)
lbl2.grid(column=0, row=0)
tab_control.pack(expand=1, fill='both')

window.mainloop()

