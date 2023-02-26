import tkinter
from tkinter import *

root = Tk()
root.title("Task Management App")
root.geometry("400x650+400+100")
root.resizable(False,False)

task_list = []

def open_file():
    try:
        global task_list
        with open("tasklist.txt","r") as taskfile:
            tasks = taskfile.readlines()

        for task in tasks:
            if task != '\n':
                task_list.append(task)
                listbox.insert(END,task)
    except:
        file = open('tasklist.txt','w')
        file.close()

def add_task():
    task = task_entry.get()
    task_entry.delete(0,END)
    if task:
        with open('tasklist.txt','a') as taskfile:
            taskfile.write(f"\n{task}")
        task_list.append(task)
        listbox.insert(END,task)


def delete_task():
    global task_list
    task = str(listbox.get(ANCHOR))
    if task in task_list:
        task_list.remove(task)
        with open("tasklist.txt",'w') as taskfile:
            for tassk in task_list:
                taskfile.write(task+'\n')

        listbox.delete(ANCHOR)
#icon
Image_icon = PhotoImage(file="task.png")
root.iconphoto(False,Image_icon)

#top bar
top_img = PhotoImage(file="topbar.png")
Label(root,image=top_img).pack()

dock_img = PhotoImage(file="dock.png")
Label(root,image=dock_img,bg="#32405b").place(x=30,y=25)

note_img = PhotoImage(file="task1.png")
Label(root,image=note_img,bg="#32405b").place(x=340,y=20)

heading = Label(root,text="All Task",font="arial 20 bold",fg="white",bg="#32405b")
heading.place(x=130,y=20)

cancelbtn = Button(root, text = "Exit", font=("poppins",15,"bold"), bg="royalblue", relief="sunken", command=root.destroy)
cancelbtn.place(x = 20,y = 120, width=80)

#main
frame = Frame(root,width=400,height=50,bg="white")
frame.place(x=0,y=180)

task = StringVar()
task_entry = Entry(frame,width=18,font="arial 20",bd=0)
task_entry.place(x=10,y=7)
task_entry.focus()

button = Button(frame,text="ADD",font="arial 20 bold",width=6,bg="cornflowerblue",fg="#fff",bd=0,command=add_task)
button.place(x=300,y=0)

#listbox
frame1 = Frame(root,bd=3,width=700,height=280,bg="#32405b")
frame1.pack(pady=(160,0))

listbox = Listbox(frame1,font=("arial",12),width=40,height=16,bg="#32405b",fg="white",cursor="hand2",selectbackground="cornflowerblue")
listbox.pack(side=LEFT,fill=BOTH,padx=2)
scrollbar = Scrollbar(frame1)
scrollbar.pack(side=RIGHT,fil=BOTH)

listbox.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=listbox.yview)

open_file()

#delete
Delete_icon = PhotoImage(file="delete.png")
Button(root,image=Delete_icon,bd=0,command=delete_task).pack(side=BOTTOM,pady=13)

root.mainloop()
