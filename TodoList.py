import  tkinter
import random

#Create root window!
root = tkinter.Tk()

#change background color 
root.configure(bg="white")

#change title
root.title("Todo List")

#change size
root.geometry("200x500")

#Create an empty list
tasks = []

#test
tasks = ["Call mom" , "Buy guitar" , "Eat sushi "] 



#Create Functions 
def update_listbox():
     #clear the current list
        clear_listbox()
        #Populate the listbox
        for task in tasks:
           lb_tasks.insert("end",task)

def clear_listbox():
    lb_tasks.delete(0,"end")
    

def add_task():
    #Get the task to add
    task = txt_input.get()
    #Make sure the task is not empty
    if task !="":
        #Append to the list
        tasks.append(task)
        #Update the listbox
        update_listbox()
    else:
        lbl_display["text"] = "Please enter a task."        
    txt_input.delete(0,"end")
def del_all():
    #Since we are changing the list, it needs to be global
    global tasks
    #Clear the tasks list
    tasks = []
    #Update the listbox
    update_listbox()

def del_one():
    #Get the text of the currently select item
    task = lb_tasks.get("active")
    #Confirm it is in the list
    if task in tasks:
        tasks.remove(task)
    #Update the listbox
    update_listbox()

def sort_asc():
    #Sort the list
    tasks.sort()
    #Update the listbox
    update_listbox()


def sort_desc():
    #Sort the list
    tasks.sort()
    #Reverse the list 
    tasks.reverse()
    #Update the listbox
    update_listbox()


def choose_random():
    #Choose a random task
    task = random.choice(tasks)
    #Update the display label
    lbl_display["text"] = task

def show_number():
    #Get the number of tasks
    number_of_tasks = len(tasks)
    #Create and format the message
    msg = "Number of tasks: %s" %number_of_tasks
    #display the message
    lbl_display["text"] = msg



lbl_title = tkinter.Label(root,text = "ToDo List" , bg = "white")
lbl_title.pack()

lbl_display = tkinter.Label(root,text = "" , bg = "white")
lbl_display.pack()

txt_input = tkinter.Entry(root, width = 15 )
txt_input.pack()

btn_add_task = tkinter.Button(root , text = "Add task " , fg = "green", bg = "white" , command = add_task)
btn_add_task.pack()

btn_del_all = tkinter.Button(root , text = "Delete all " , fg = "green", bg = "white" , command =del_all)
btn_del_all.pack()

btn_del_one = tkinter.Button(root , text = "Delete" , fg = "green", bg = "white" , command = del_one)
btn_del_one.pack()

btn_sort_asc = tkinter.Button(root , text = "Sort (ASC) " , fg = "green", bg = "white" , command = sort_asc)
btn_sort_asc.pack()

btn_sort_desc = tkinter. Button(root , text = "Sort (DESC) " , fg = "green", bg = "white" , command = sort_desc)
btn_sort_desc.pack()

btn_choose_random= tkinter.Button(root , text = "Random Task " , fg = "green", bg = "white" , command = choose_random)
btn_choose_random.pack()

btn_number_of_tasks = tkinter.Button(root , text = "Number of tasks" , fg = "green", bg = "white" , command = show_number)
btn_number_of_tasks.pack()

btn_quit = tkinter.Button(root , text = "Exit " , fg = "green", bg = "white" , command =exit)
btn_quit.pack()

lb_tasks= tkinter.Listbox(root)
lb_tasks.pack()





#main loop
root.mainloop()