import tkinter as tk

root = tk.Tk()

root.geometry("800x500")
root.title("Liars Dice Game")

label = tk.Label(root,text="hey krasi", font=('Arial',18))
label.pack(pady=20, padx=20)

textBox = tk.Text(root, height=8, font=('Arial',12))
textBox.pack(padx=15)

# entry = tk.Entry(root)
# entry.pack()


def donothing():
    print("this does exactly nothing :p")

button = tk.Button(root, text="Submit", font=('Arial', 12))
button.pack(pady=10)

menubar = tk.Menu(root)
filemenu = tk.Menu(menubar,tearoff=0)
filemenu.add_command(label="New", command=donothing)
filemenu.add_command(label="Open", command=donothing)
filemenu.add_command(label="Save", command=donothing)
filemenu.add_command(label="Save as...", command=donothing)
filemenu.add_command(label="Close", command=donothing)

filemenu.add_separator()
filemenu.add_command(label="Exit", command=root.quit)
menubar.add_cascade(label="File", menu=filemenu)
editmenu = tk.Menu(menubar, tearoff=0)
editmenu.add_command(label="Undo", command=donothing)
editmenu.add_separator()
editmenu.add_command(label="Cut", command=donothing)
editmenu.add_command(label="Copy", command=donothing)
editmenu.add_command(label="Paste", command=donothing)
editmenu.add_command(label="Delete", command=donothing)
editmenu.add_command(label="Select All", command=donothing)

menubar.add_cascade(label="Edit", menu=editmenu)
helpmenu = tk.Menu(menubar, tearoff=0)
helpmenu.add_command(label="Help Index", command=donothing)
helpmenu.add_command(label="About...", command=donothing)
menubar.add_cascade(label="Help", menu=helpmenu)



root.config(menu=menubar)

root.mainloop()