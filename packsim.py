import tkinter as tk

class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        master.geometry("600x400")
        master.title("tkinter pack layout simulator")
        self.master = master
        self.configure(bg="yellow")
        self.pack(fill=tk.BOTH, expand=True)
        self.layout_panels()
        self.create_widgets()
        self.layout_control_panel()

    def layout_panels(self):
        self.simulation_panel = tk.Frame(self, bg = "black")
        self.control_panel = tk.Frame(self, bg = "Gray")
        self.simulation_panel.pack(side=tk.LEFT,expand=True, fill=tk.BOTH)
        self.control_panel.pack(side=tk.RIGHT, fill=tk.Y)

    def layout_control_panel(self):
        tk.Label(self.control_panel, text="visible").grid(column=0, row=1,sticky="news")
        tk.Label(self.control_panel, text="side").grid(column=0, row=2,sticky="news")
        tk.Label(self.control_panel, text="fill").grid(column=0, row=3,sticky="news")
        tk.Label(self.control_panel, text="extend").grid(column=0, row=4,sticky="news")
        for x in range(1,4):
            tk.Label(self.control_panel, text="Item " + str(x)).grid(column=x,row=0)

    def create_widgets(self):
        self.hi_there = tk.Button(self.simulation_panel)
        self.hi_there["text"] = "Hello World\n(click me)"
        self.hi_there["command"] = self.say_hi
        self.hi_there.pack(side="top")

    def say_hi(self):
        print("hi there, everyone!")

root = tk.Tk()
app = Application(master=root)
app.mainloop()