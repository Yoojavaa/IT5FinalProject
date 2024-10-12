import tkinter as tk
from tkinter import messagebox
from PIL import ImageTk, Image
from Database import Database

class Register:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Create Account")
        self.window.resizable(False, False)

        window_width = 1050
        window_height = 550

        screen_width = self.window.winfo_screenwidth()
        screen_height = self.window.winfo_screenheight()

        center_x = int(screen_width / 2 - window_width / 2)
        center_y = int(screen_height / 2 - window_height / 2)

        self.window.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')

        frame_width = int(window_width * 3 / 5)
        frame_height = window_height
        first_frame = tk.Frame(self.window, bg='#ff0000', width=frame_width, height=frame_height)
        first_frame.place(x=0, y=0)

        image = Image.open("car.jpg")
        image = image.resize((frame_width, frame_height))
        self.image = ImageTk.PhotoImage(image)

        image_label = tk.Label(first_frame, image=self.image)
        image_label.place(relwidth=1, relheight=1)

        second_frame_width = window_width - frame_width
        second_frame = tk.Frame(self.window, bg='#ffffff', width=second_frame_width, height=frame_height)
        second_frame.place(x=frame_width, y=0)

        canvas = tk.Canvas(second_frame, width=second_frame_width, height=frame_height, bg='#ffffff', highlightthickness=0)
        canvas.pack(fill='both', expand=True)

        create_account_label = tk.Label(canvas, text="CREATE ACCOUNT", font=("Arial", 18), bg='#ffffff')
        create_account_label.place(relx=0.5, rely=0.1, anchor='center')

        name_label = tk.Label(canvas, text="Name", font=("Arial", 12), bg='#ffffff')
        name_label.place(relx=0.5, rely=0.2, anchor='center')

        self.name_input = tk.Entry(canvas, font=("Arial", 12), width=30)
        self.name_input.place(relx=0.5, rely=0.25, anchor='center')

        username_label = tk.Label(canvas, text="Username", font=("Arial", 12), bg='#ffffff')
        username_label.place(relx=0.5, rely=0.3, anchor='center')

        self.username_input = tk.Entry(canvas, font=("Arial", 12), width=30)
        self.username_input.place(relx=0.5, rely=0.35, anchor='center')

        password_label = tk.Label(canvas, text="Password", font=("Arial", 12), bg='#ffffff')
        password_label.place(relx=0.5, rely=0.4, anchor='center')

        self.password_input = tk.Entry(canvas, show="*", font=("Arial", 12), width=30)
        self.password_input.place(relx=0.5, rely=0.45, anchor='center')

        confirm_password_label = tk.Label(canvas, text="Confirm Password", font=("Arial", 12), bg='#ffffff')
        confirm_password_label.place(relx=0.5, rely=0.5, anchor='center')

        self.confirm_password_input = tk.Entry(canvas, show="*", font=("Arial", 12), width=30)
        self.confirm_password_input.place(relx=0.5, rely=0.55, anchor='center')

        create_account_button = tk.Button(canvas, text="Create Account", font=("Arial", 12), bg='#ff0000', fg='#ffffff', command=self.create_account)
        create_account_button.place(relx=0.5, rely=0.65, anchor='center')

        login_label = tk.Label(canvas, text="Already have an account? Login here", font=("Arial", 10), bg='#ffffff', fg='#0000ff', cursor="hand2")
        login_label.bind("<Button-1>", self.open_login)
        login_label.place(relx=0.5, rely=0.75, anchor='center')

    def create_account(self):
        name = self.name_input.get()
        username = self.username_input.get()
        password = self.password_input.get()
        confirm_password = self.confirm_password_input.get()

        if not all([name, username, password, confirm_password]):
            messagebox.showerror("Error", "All fields are required")
            return

        if password != confirm_password:
            messagebox.showerror("Error", "Passwords do not match")
            return

        try:
            db = Database('localhost', 'root', '', 'final_project')
            db.register(name, username, password)
            messagebox.showinfo("Success", "Account created successfully")
            self.open_login(None)
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {str(e)}")

    def open_login(self, event):
        self.window.destroy()
        from Login import Login
        login_window = Login()

