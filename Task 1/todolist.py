import tkinter as tk
from tkinter import messagebox

tasks_list = []
counter = 1

def check_input_error():
    if enter_task_field.get() == "":
        messagebox.showerror("Input Error")
        return 0
    return 1

def clear_task_number_field():
    task_number_field.delete(0.0, tk.END)

def clear_task_field():
    enter_task_field.delete(0, tk.END)

def add_task():
    global counter
    value = check_input_error()
    if value == 0:
        return
    content = enter_task_field.get() + "\n"
    tasks_list.append(content)
    text_area.insert('end -1 chars', "[ " + str(counter) + " ] " + content)
    counter += 1
    clear_task_field()

def remove_task():
    global counter
    if len(tasks_list) == 0:
        messagebox.showerror("No task")
        return
    task_number = task_number_field.get(1.0, tk.END)
    if task_number == "\n":
        messagebox.showerror("Input error")
        return
    else:
        task_no = int(task_number)
    clear_task_number_field()
    tasks_list.pop(task_no - 1)
    counter -= 1
    text_area.delete(1.0, tk.END)
    for i in range(len(tasks_list)):
        text_area.insert('end -1 chars', "[ " + str(i + 1) + " ] " + tasks_list[i])

if __name__ == "__main__":
    app = tk.Tk()
    app.configure(background="light green")
    app.title("Personal Task Manager")
    app.geometry("250x300")

    enter_task_label = tk.Label(app, text="Enter Your Task", bg="light green")
    enter_task_field = tk.Entry(app)
    submit_button = tk.Button(app, text="Submit", fg="Black", bg="Red", command=add_task)
    text_area = tk.Text(app, height=5, width=25, font="lucida 13")
    task_number_label = tk.Label(app, text="Task Number to Remove", bg="blue")
    task_number_field = tk.Text(app, height=1, width=2, font="lucida 13")
    remove_button = tk.Button(app, text="Remove Task", fg="Black", bg="Red", command=remove_task)
    exit_button = tk.Button(app, text="Exit", fg="Black", bg="Red", command=exit)

    enter_task_label.grid(row=0, column=2)
    enter_task_field.grid(row=1, column=2, ipadx=50)
    submit_button.grid(row=2, column=2)
    text_area.grid(row=3, column=2, padx=10, sticky=tk.W)
    task_number_label.grid(row=4, column=2, pady=5)
    task_number_field.grid(row=5, column=2)
    remove_button.grid(row=6, column=2, pady=5)
    exit_button.grid(row=7, column=2)

    app.mainloop()
