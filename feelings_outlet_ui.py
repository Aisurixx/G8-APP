import tkinter as tk
from tkinter import messagebox
from ttkbootstrap import Label, Button, Entry, Checkbutton, LabelFrame, Style
from tkinter import font
from datetime import datetime
from database_handler import DatabaseHandler

class FeelingsOutletUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Feelings Outlet")
        root.geometry("367x780")
        root.configure(bg="#FFFFFF")
        custom_font = font.Font(family="Press Start 2P", size=12)
        root.attributes('-toolwindow', 1)
        
        

        # bg image
        self.bg = tk.PhotoImage(file="bg.png")
        my_label = Label(image=self.bg)
        my_label.place(x=0, y=0, relwidth=1, relheight=1)

        # database
        self.db_handler = DatabaseHandler()

        # user entry 1
        self.username_label = Label(root, text="Username:", font=custom_font, background='#f4dce4' )
        self.username_label.pack()
        self.username_entry = Entry(root, style="secondary.TEntry", font=custom_font, background='#f4dce4')
        self.username_entry.pack()

        self.anonymous_var = tk.IntVar()
        self.anonymous_check = Checkbutton(root,  variable=self.anonymous_var,bootstyle="secondary.Roundtoggle.Toolbutton", text=': Anoymous')
        self.anonymous_check.pack(padx=10, pady=15)

        self.confession_label = Label(root, text="Confession:", font=custom_font, background='#f4dce4')
        self.confession_label.pack()
        self.confession_entry = Entry(root, style="secondary.TEntry", font=custom_font)
        self.confession_entry.pack()

        # post
        self.post_button = Button(root, text="Post Confession", command=self.post_confession,style="secondary.Outline.TButton", )
        self.post_button.pack(padx=5, pady=10)
        # delete
        self.delete_button = Button(root, text="Delete Confession", command=self.delete_confession,
                                    style="secondary.Outline.TButton")
        self.delete_button.pack(padx=6, pady=10)
        
        
        self.remove_anonymous_button = Button(root, text="Remove Anonymous", command=self.remove_anonymous_posts,style="secondary.Outline.TButton")
        self.remove_anonymous_button.pack(padx=5, pady=10)
        

        self.display_confessions()
        
        
    def remove_anonymous_posts(self):
        result = messagebox.askquestion("Remove Anonymous Posts", "Are you sure you want to remove all anonymous posts?")
        if result == 'yes':
            self.db_handler.remove_anonymous_posts()
            messagebox.showinfo("Success", "Anonymous posts removed successfully!")
            self.display_confessions()
        
        

    def post_confession(self):
        username = self.username_entry.get() if not self.anonymous_var.get() else "Anonymous"
        confession = self.confession_entry.get()

        if not username:
            messagebox.showwarning("Error", "Please enter your Username or turn on anonymous!")
            return

        if not confession:
            messagebox.showwarning("Error", "Please enter your Confession!")
            return

        self.db_handler.post_confession(username, confession)

        messagebox.showinfo("Success", "Confession posted!")

        self.display_confessions()

    def delete_confession(self):
        username = self.username_entry.get()
        if not username:
            messagebox.showwarning("Error", "Please enter your username.")
            return

        self.db_handler.delete_confession(username)

        messagebox.showinfo("Success", "Confession deleted successfully!")

        self.display_confessions()

    def display_confessions(self):
        for widget in self.root.winfo_children():
            if "confessions_label_frame" in widget.winfo_name():
                widget.destroy()

        all_confessions = self.db_handler.get_all_confessions()
        label_frame = LabelFrame(text="Confessions", style="secondary", name="confessions_label_frame", )
        label_frame.pack(padx=20, pady=20)

        if all_confessions:
            confessions_text = "\n".join(
                [f"{confession[1]}: {confession[2]} ({confession[3]})" for confession in all_confessions], )
            all_confessions_label = Label(label_frame, text=confessions_text, name="confessions_label",style="dark.TLabel", background='#f4dcec')
            all_confessions_label.pack()
