import tkinter as tk             # importing the tkinter module as tk  
from tkinter import ttk          # importing the ttk module from the tkinter library  
from tkinter import messagebox   # importing the messagebox module from the tkinter library  
import sqlite3 as sql            # importing the sqlite3 module as sql 


# Create a connection to the SQLite database
conn = sql.connect("todo_list.db")
cursor = conn.cursor()

# Create a table for the tasks if it doesn't exist
cursor.execute("CREATE TABLE IF NOT EXISTS tasks (id INTEGER PRIMARY KEY AUTOINCREMENT, task TEXT)")

# defining the function to Add a task to the list
def add_task():
    task = entry.get()
    if task:
        # Insert the task into the database
        cursor.execute("INSERT INTO tasks (task) VALUES (?)", (task,))
        conn.commit()
        # Update the listbox
        listbox.insert(tk.END, task)
        entry.delete(0, tk.END)

# defining the function to delete a task from the list
def remove_task():
    selected_task = listbox.curselection()
    if selected_task:
        index = selected_task[0]
        task = listbox.get(selected_task)
        # Delete the task from the database
        cursor.execute("DELETE FROM tasks WHERE task=?", (task,))
        conn.commit()
        # Update the listbox
        listbox.delete(selected_task)

# defining the function to delete all tasks from the list
def delete_all_tasks():  
    # asking user for confirmation  
    message_box = messagebox.askyesno('Delete All', 'Are you sure?')  
    if message_box == True:  
        # using while loop to iterate through the tasks list until it's empty   
        while(len(tasks) != 0):  
            # using the pop() method to pop out the elements from the list  
            tasks.pop()  
        # using the execute() method to execute a SQL statement  
        cursor.execute('delete from tasks')  
        # update the listbox  
        listbox.delete(0, 'end')  
        
def close():
    # asking user for confirmation  
    message_box = messagebox.askyesno('exit','Are you sure, you want to exit?') 
    if message_box == True:  
        # using the destroy() method to close the application  
        window.destroy() 

# Create the Tkinter window
window = tk.Tk()
window.title("To-Do List")
window.geometry("500x450+750+250")  
window.resizable(0, 0)  
window.configure(bg = "#008080") 


# defining frames using the tk.Frame() widget  
header_frame = tk.Frame(window, bg = "#008080")  
functions_frame = tk.Frame(window, bg = "#008080")  
listbox_frame = tk.Frame(window, bg = "#008080")  

# using the pack() method to place the frames in the application  
header_frame.pack(fill="both")
functions_frame.pack(side="left", expand=True, fill="both")
listbox_frame.pack(side="right", expand=True, fill="both")

# defining a list box using the tk.Listbox() widget  
listbox = tk.Listbox(  
    listbox_frame,  
    width = 26,  
    height = 14,  
    selectmode = 'SINGLE',  
    background = "#FFFFFF",  
    foreground = "#000000",  
    selectbackground = "#CD853F",  
    selectforeground = "#FFFFFF"  
)  
# using the place() method to place the list box in the application  
listbox.place(x = 30, y = 40)  


# Populate the listbox with tasks from the database
cursor.execute("SELECT task FROM tasks")
tasks = cursor.fetchall()
for task in tasks:
    listbox.insert(tk.END, task[0])

# defining a label using the ttk.Label() widget  
header_label = ttk.Label(  
    header_frame,  
    text = "My To-Do List",  
    font = ("Roboto", "30"),  
    background = "#008080",  
    foreground = "#000000"  
)  
# using the pack() method to place the label in the application  
header_label.pack(padx = 20, pady = 20)  


# defining another label using the ttk.Label() widget  
task_label = ttk.Label(  
    functions_frame,  
    text = "Enter the Task:",  
    font = ("Consolas", "15", "bold"),  
    background = "#008080",  
    foreground = "#000000"  
)  
# using the place() method to place the label in the application  
task_label.place(x = 30, y = 40)  

# defining an entry field using the ttk.Entry() widget  
entry = ttk.Entry(  
    functions_frame,  
    font = ("Consolas", "12"),  
    width = 16,  
    background = "#FFF8DC",  
    foreground = "#A52A2A"  
)  
# using the place() method to place the entry field in the application  
entry.place(x = 30, y = 80)  


# adding buttons to the application using the ttk.Button() widget  

add_btn = ttk.Button(  
    functions_frame,  
    text = "Add Task",  
    width = 24,  
    command = add_task  
)  

remove_btn = ttk.Button(  
    functions_frame,  
    text = "Delete Task",  
    width = 24,  
    command = remove_task  
)  

del_all_btn = ttk.Button(  
    functions_frame,  
    text = "Delete All Tasks",  
    width = 24,  
    command = delete_all_tasks  
) 

exit_btn = ttk.Button(  
    functions_frame,  
    text = "Exit",  
    width = 24,  
    command = close  
) 

# using the place() method to set the position of the buttons in the application  
add_btn.place(x = 30, y = 120)  
remove_btn.place(x = 30, y = 160)
del_all_btn.place(x = 30, y = 200)
exit_btn.place(x = 30, y = 240)  

window.mainloop()

# Close the database connection
cursor.close()
conn.close()
