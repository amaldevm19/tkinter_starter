<h3>tKinter_starter</h3>
<p>Create A basic window using tkinter</p>
<p>Create from below details or uncomment th tkinter_basics.py and run using Python 3</p>
<pre>
    from tkinter import *
    window = Tk()
    window.title("Hello world")
    window.mainloop()
</pre>
<p>Create a label and attach to window</p>
<pre>
    from tkinter import *
    window = Tk()
    window.title("Starter App")
    lbl = Label(window, text="Hello World")
    lbl.grid(column=0, row=0)
    window.mainloop()
</pre>
<p>Modify font and size</p>
<pre>
    from tkinter import *
    window = Tk()
    window.title("Starter App")
    lbl = Label(window, text="Hello World", font=("Arial Bold", 50))
    lbl.grid(column=0, row=0)
    window.mainloop()
</pre>
<p>Modify with below code for setting Window size</p>
<pre>
    window.geometry('600x400')
</pre>
<p>Adding a button</p>
<pre>
    btn = Button(window, text="Click me")
    btn.grid(column=0, row=1)
</pre>
<p>To change button color</p>
<pre>
    btn = Button(window, text="Click Me", bg="orange", fg="red")
</pre>
<p>Handle Button click event</p>
<p>Add a clicked function above the button </p>
<pre>
    def clicked():
        lbl.configure(text="Button was clicked")
</pre>
<p>Add clicked() to button</p>
<pre>
    btn = Button(window, text="Click me", bg="orange", fg="red", command=clicked)
</pre>
<p>Adding Tkinter text box , Entry class</p>
<pre>
    txt = Entry(window, width=10)
    txt.grid(column=1, row=1)
</pre>
<p>Modify clicked() for getting data from Text box</p>
<pre>
    def clicked():
        res = "Welcome "+ txt.get()
        lbl.configure(text=res)
</pre>
<p>Focus Input</p>
<pre>
    txt.focus()
</pre>
<p>Disable input</p>
<pre>
    txt = Entry(window, width=10, state="disabled")
</pre>
<p>Import tkinter.ttk, Add A combo box</p>
<pre>
    import tkinter.ttk as ttk
    ...
    combo = Combobox(window)
</pre>
<p>Adding values to combobox</p>
<pre>
    combo['values'] = (1,2,3,4,5,"Text")
    combo.current(1)
</pre>
<p>Getting value of combo to clicked()</p>
<pre>
    def clicked():
        res = "Welcome "+ txt.get()+" "+combo.get()
        lbl.configure(text=res)
</pre>
<p>Add a check box</p>
<pre>
    chk_var = BooleanVar()
    chk_var.set(False)
    chkbx = ttk.Checkbutton(window, text="Check box", var=chk_var)
    chkbx.grid(column=0, row=3)
</pre>
<p>Add a radio button</p>
<pre>
    rdbtn1 = ttk.Radiobutton(window, text="First", value=1 )
    rdbtn2 = ttk.Radiobutton(window, text="Second", value=2 )
    rdbtn1.grid(column=0, row=4)
    rdbtn2.grid(column=1, row=4)
</pre>
<p>function call from radio button</p>
<pre>
    def radioClicked():
        print(selected.get())

    selected = IntVar()
    rdbtn1 = ttk.Radiobutton(window, text="First", value=1, variable=selected, command=radioClicked )
    rdbtn2 = ttk.Radiobutton(window, text="Second", value=2, variable=selected, command=radioClicked )
    rdbtn1.grid(column=0, row=4)
    rdbtn2.grid(column=1, row=4)
</pre>

<p>Import scrolledtext from tkinter and Add a scrolled text widget </p>
<pre>
    from tkinter.scrolledtext import ScrolledText
    ...
    scrltxt = ScrolledText(window, width= 30, height=10)
    scrltxt.insert(INSERT,"Enter your text")
    scrltxt.grid(column=0, row=5)
</pre>
<p>To clear the content of ScrolledText</p>
<pre>
    def clearScrolled():
        scrltxt.delete(1.0, END)

    scrltxt = ScrolledText(window, width= 30, height=10)
    scrltxt.insert(INSERT,"Enter your text")
    scrltxt.grid(column=0, row=5)

    scrlbtn = Button(window, text="Clear Scrolled text", command=clearScrolled)
    scrlbtn.grid(column=1, row=5)
</pre>

<p>Import messagebox and show messagebox</p>
<pre>
    from tkinter import scrolledtext, messagebox
    ...
    def callShowInfo():
        messagebox.showinfo('Message Title', 'Message Content')

    msgbtn1 = Button(window, text="ShwoInfoMessage", command=callShowInfo)
    msgbtn1.grid(column=0, row=6)

    def callShowError():
        messagebox.showerror('Message Title', 'Message Content')

    msgbtn2 = Button(window, text="ShwoErrorMessage", command=callShowError)
    msgbtn2.grid(column=1, row=6)

    def callShowWarning():
        messagebox.showwarning('Message Title', 'Message Content')

    msgbtn3 = Button(window, text="ShwoWarningMessage", command=callShowWarning)
    msgbtn3.grid(column=3, row=6)
</pre>
<p>Add Yes/No message box</p>
<pre>
    def askQuestion():
        res = messagebox.askyesno('Message title','Message content')
        print(res)

    msgbtn4 = Button(window, text="AskYesorNo", command=askQuestion)
    msgbtn4.grid(column=1, row=7)
</pre>

<p>askyesnocancel() will return True, False, None</p>
<pre>
    def askAnotherQuestion():
        res = messagebox.askyesnocancel('Message title','Message content')
        print(res)
        if res == None:
            print("Pressed cancel button")

    msgbtn5 = Button(window, text="AskYesorNoCancel", command=askAnotherQuestion)
    msgbtn5.grid(column=1, row=8)
</pre>
<p>Adding a spin box</p>
<pre>
    spin = Spinbox(window, from_=0, to=100, width=5)
    spin.grid(column=0, row=9)
</pre>
<p>Setting Value of spin box</p>
<pre>
    spin = Spinbox(window, values=(10,20,30), width=5)
    spin.grid(column=0, row=9)
</pre>

<p>Setting default value to spin box and getting value from spinbox</p>
<pre>
    def changed():
        print(var.get())

    var = IntVar()
    var.set(20)

    spin = Spinbox(window, from_=0, to=100, width=5, textvariable=var, command=changed)
    spin.grid(column=0, row=9)
</pre>
<p>Progress bar widget</p>
<pre> 
    pbar = ttk.Progressbar(window, length=200)
    pbar['value'] = 70
    pbar.grid(column=1, row=1)
</pre>
<p>Add style to progress bar</p>
<pre>
    style = ttk.Style()
    style.theme_use('default')
    style.configure("black.Horizontal.TProgressbar", background='black')

    pbar = ttk.Progressbar(window, length=200, style='black.Horizontal.TProgressbar')
    pbar['value'] = 70
    pbar.grid(column=1, row=1)
</pre>
<p>File dialog to open files</p>
<pre>
    from tkinter import scrolledtext, messagebox, filedialog
    ...
    def openFIle():
    file = filedialog.askopenfilename(filetypes = (("Text files","*.txt"),("all files","*.*")))
    print(file)

    msgbtn5 = Button(window, text="AskYesorNoCancel", command=openFIle)
    msgbtn5.grid(column=1, row=1)
</pre>
<p>Open mutiple files use</p>
<pre>
    files = filedialog.askopenfilenames()
</pre>
<p>For director </p>
<pre>
    dir = filedialog.askdirectory()
</pre>

<p>To specify initial file path as same as the current location</p>
<pre>
    from os import path
    ...
    file = filedialog.askopenfilename(filetypes = (("Text files","*.txt"),("all files","*.*")), initialdir=path.dirname(path.abspath(__file__)))
</pre>

<p>Add a menubar</p>
<pre>
    from tkinter import scrolledtext, messagebox, filedialog, Menu
    ...
    menu = Menu(window)
    menu.add_command(label='File')
    window.configure(menu=menu)
</pre>

<p>Adding multiple level menu and function</p>
<pre>
    def clicked():
        print("Another")

    menu = Menu(window)
    new_item = Menu(menu)
    new_item.add_command(label='New')
    new_item.add_separator()
    new_item.add_command(label='Another', command=clicked)
    menu.add_cascade(label='File', menu=new_item)
    menu.add_cascade(label='Edit', menu=new_item)
    window.configure(menu=menu)
</pre>
<p>Tearoff can be disabled</p>
<pre>
    new_item = Menu(menu, tearoff=0)
</pre>
<p>Add a Tab control</p>

<pre>
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

</pre>