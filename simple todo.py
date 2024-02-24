import customtkinter


class Task:
    def __init__(self, name, status="Pending", frame=None):
        self.name = name
        self.status = status
        self.frame=frame
        self.task_checkbox = customtkinter.CTkCheckBox(master=self.frame, text=f'{self.name}',command=self.delete_task)
        self.task_checkbox.pack()
    def delete_task(self):
        self.task_checkbox.pack_forget()


def create_task(name, frame):
    name= Task(name=name,frame=frame)
    print(name.frame)
    print(name.status)
    print(name.name)


class App:
    def __init__(self):
        window = customtkinter.CTk()
        window.title('Todo')
        self.task_view_frame = customtkinter.CTkScrollableFrame(master=window)
        self.task_view_frame.pack()

        self.task_entry = customtkinter.CTkEntry(master=window)
        self.task_entry.pack()

        add_button = customtkinter.CTkButton(master=window, text='Add Task', command=self.add_task)
        add_button.pack()

        window.mainloop()

    def add_task(self):
        name = self.task_entry.get()
        self.task_entry.delete(0,len(name))
        frame = self.task_view_frame
        create_task(name, frame)
App()
