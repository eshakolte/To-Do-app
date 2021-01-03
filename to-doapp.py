from tkinter import *
from tkinter.font import Font
import pickle
from tkinter import filedialog

window = Tk()
window.title("To-Do list")


# Methods

def delete_task():
    todoList.delete((ANCHOR))

def add_task():
    todoList.insert(END,task_name.get())
    task_name.delete(0,END)

def done_task():
    todoList.itemconfig(
        todoList.curselection(), fg = "#a9addb"
    )
    todoList.select_clear(0, END)


def pending_task():
    todoList.itemconfig(
        todoList.curselection(), fg="#000000"
    )
    todoList.select_clear(0, END)

def dctask():
    count = 0
    while count < todoList.size():
        if todoList.itemcget(count , "fg") == "#a9addb":
            todoList.delete(todoList.index(count))
        else:
            count += 1

def savel():
    fname = filedialog.asksaveasfilename(
        initialdir = "C:\\Users\\Esha Kolte\\PycharmProjects\\guiproject",
        title = "Save File",
        filetypes = (("Dat Files","*.dat") , ("All  Files", "*.*"))
    )
    if fname:
        if fname.endswith(".txt"):
            pass
        else :
            fname = f'{fname}.dat'
    #delete done before saving
    count = 0
    while count < todoList.size():
        if todoList.itemcget(count, "fg") == "#a9addb":
            todoList.delete(todoList.index(count))
        else:
            count += 1

    stuf = todoList.get(0,END)

    ofile = open(fname, 'wb')

    pickle.dump(stuf, ofile)

def openl():
    fname = filedialog.askopenfilename(initialdir = "C:\\Users\\Esha Kolte\\PycharmProjects\\guiproject",
        title = "Open File",
        filetypes = (("Dat Files","*.dat") , ("All  Files", "*.*")))
    if fname:
        todoList.delete(0,END)
        input_file = open(fname , 'rb')
        stuf = pickle.load(input_file)
        for item in stuf:
            todoList.insert(END,item)

def clearl():
    todoList.delete(0,END)

#window geometry
window.geometry("500x500")
list_font = Font(
    family = "Comic Sans MS",
    size = 20)

todoframe = Frame(window)
todoframe.pack()
todoList = Listbox(todoframe, font = list_font , width = 20 , height = 5, bg = "SystemButtonFace",  fg = '#000000',
                   highlightthickness = 0, selectbackground = "#a6a6a6", activestyle = "none")

todoList.pack()

# schedule = ["coding","debugging", "rest","eat","coding","die because code not debugged"]
#
# for item in schedule:
#     todoList.insert(END,item)

scrollist = Scrollbar(todoframe)
scrollist.pack(side = RIGHT , fill = Y)

todoList.config(yscrollcommand = scrollist.set)
todoList.pack(side = LEFT , fill=BOTH)
scrollist.config(command = todoList.yview)

task_name = Entry(window, font= ("Helvetica" , 24),width = 27)
task_name.pack(pady = 30)


#create menu

listmenu = Menu(window)
window.config(menu = listmenu)
#add item to menu
filemenu = Menu(listmenu , tearoff = False)
listmenu.add_cascade(label = "File", menu = filemenu)
#add dropdown items
filemenu.add_command(label = "save", command = savel)
filemenu.add_command(label = "opem", command = openl)
filemenu.add_separator()
filemenu.add_command(label = "clear", command = clearl)

button = Frame(window)
button.pack(pady = 30)

#buttons

delete_button = Button(button, text = "Delete Task" , bg = "black" ,fg = "#ff8800",command = delete_task)
add_button = Button(button, text = "Add Task" ,bg = "black",fg = "#ff8800", command = add_task)
cross_button = Button(button, text = "Task Done" , bg = "black",fg = "#ff8800", command = done_task)
uncross_button = Button(button, text = "Task pending" , bg = "black",fg = "#ff8800", command = pending_task)
delete_crossed_button = Button(button, text = "Delete Completed Task" , bg = "black",fg = "#ff8800", command = dctask)

delete_button.grid(row = 0, column = 0)
add_button.grid(row = 0, column = 1 , padx  = 20)
cross_button.grid(row = 0, column = 2 )
uncross_button.grid(row = 0, column = 3, padx  = 20)
delete_crossed_button.grid(row = 0, column = 4)


window.mainloop()
