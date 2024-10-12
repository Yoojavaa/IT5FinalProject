import tkinter as tk
from tkinter import messagebox
from PIL import ImageTk, Image
from Database import Database

class Login:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Car Rentals")
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

        image = Image.open("carLoginPic.jpg")
        image = image.resize((frame_width, frame_height))
        self.image = ImageTk.PhotoImage(image)

        image_label = tk.Label(first_frame, image=self.image)
        image_label.place(relwidth=1, relheight=1)

        second_frame_width = window_width - frame_width
        second_frame = tk.Frame(self.window, bg='#ffffff', width=second_frame_width, height=frame_height)
        second_frame.place(x=frame_width, y=0)

        canvas = tk.Canvas(second_frame, width=second_frame_width, height=frame_height, bg='#ffffff', highlightthickness=0)
        canvas.pack(fill='both', expand=True)

        welcome_back_label = tk.Label(canvas, text="WELCOME BACK", font=("Arial", 18), bg='#ffffff')
        welcome_back_label.place(relx=0.5, rely=0.1, anchor='center')

        login_label = tk.Label(canvas, text="Login", font=("Arial", 14), bg='#ffffff')
        login_label.place(relx=0.5, rely=0.2, anchor='center')

        user_label = tk.Label(canvas, text="Username", font=("Arial", 12), bg='#ffffff')
        user_label.place(relx=0.5, rely=0.3, anchor='center')

        self.user_input = tk.Entry(canvas, font=("Arial", 12), width=30)
        self.user_input.place(relx=0.5, rely=0.35, anchor='center')

        pass_label = tk.Label(canvas, text="Password", font=("Arial", 12), bg='#ffffff')
        pass_label.place(relx=0.5, rely=0.4, anchor='center')

        self.pass_input = tk.Entry(canvas, show="*", font=("Arial", 12), width=30)
        self.pass_input.place(relx=0.5, rely=0.45, anchor='center')

        login_button = tk.Button(canvas, text="Login", font=("Arial", 12), bg='#ff0000', fg='#ffffff', command=self.login)
        login_button.place(relx=0.5, rely=0.5, anchor='center')

        register_label = tk.Label(canvas, text="Don't have an account? Register here", font=("Arial", 10), bg='#ffffff', fg='#0000ff', cursor="hand2")
        register_label.bind("<Button-1>", self.open_register)
        register_label.place(relx=0.5, rely=0.55, anchor='center')

        self.window.mainloop()

    def open_register(self, event):
        self.window.destroy()
        import Register
        register_window = Register.Register()
        register_window.window.mainloop()

    def login(self):
        db = Database('localhost', 'root', '', 'final_project')
        user = self.user_input.get()
        password = self.pass_input.get()
        result = db.login(user, password)
        if result:
            print("Login successful")
            self.window.destroy()
            import Dashboard
            dashboard_window = Dashboard.dashboard()
            dashboard_window.window.mainloop()
        else:
            messagebox.showerror("Error", "Incorrect username or password")