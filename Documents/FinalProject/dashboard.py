import tkinter as tk
from tkinter import ttk, messagebox, simpledialog
from Database import Database
from PIL import Image, ImageTk


class Dashboard:
    def __init__(self):
        self.db = Database('localhost', 'root', '', 'final_project')

        self.window = tk.Tk()
        self.window.title("Car Rentals")
        self.window.state('zoomed')
        self.window.resizable(False, False)

        self.main_frame = tk.Frame(self.window, bg="#d3d3d3")
        self.main_frame.pack(fill=tk.BOTH, expand=True)

        header = tk.Frame(self.main_frame, bg="#007bff", height=50)
        header.pack(fill=tk.X)

        title_label = tk.Label(header, text="Car Rentals Dashboard", font=("Arial", 20, "bold"), bg="#007bff", fg="white")
        title_label.pack(pady=10)

        sidebar = tk.Frame(self.main_frame, bg="#343a40", width=200)
        sidebar.pack(side=tk.LEFT, fill=tk.Y)

        rent_button = tk.Button(sidebar, text="Rent", font=("Arial", 14), command=self.show_rental_form, bg="#495057", fg="white", width=15)
        rent_button.pack(pady=10)

        gallery_button = tk.Button(sidebar, text="Gallery", font=("Arial", 14), command=self.show_gallery, bg="#495057", fg="white", width=15)
        gallery_button.pack(pady=10)

        update_button = tk.Button(sidebar, text="Update", font=("Arial", 14), command=self.show_update_form, bg="#ffc107", fg="white", width=15)
        update_button.pack(pady=10)

        delete_button = tk.Button(sidebar, text="Delete", font=("Arial", 14), command=self.delete_rent, bg="#dc3545", fg="white", width=15)
        delete_button.pack(pady=10)

        search_button = tk.Button(sidebar, text="Search", font=("Arial", 14), command=self.show_search_dialog, bg="#17a2b8", fg="white", width=15)
        search_button.pack(pady=10)

        self.content_frame = tk.Frame(self.main_frame, bg="#d3d3d3")
        self.content_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        self.display_rentals()

        self.window.mainloop()

    def display_rentals(self, search_term=None):
        for widget in self.content_frame.winfo_children():
            widget.destroy()

        rental_list_label = tk.Label(self.content_frame, text="List of Rentals", font=("Arial", 16), bg="#d3d3d3")
        rental_list_label.pack(pady=10)

        self.tree = ttk.Treeview(self.content_frame, columns=("ID", "Customer Name", "Contact", "Car", "Date Rented", "Date Due", "Days Rented", "Total"), show="headings")
        self.tree.heading("ID", text="ID")
        self.tree.heading("Customer Name", text="Customer Name")
        self.tree.heading("Contact", text="Contact Number")
        self.tree.heading("Car", text="Car")
        self.tree.heading("Date Rented", text="Date Rented")
        self.tree.heading("Date Due", text="Rent Due")
        self.tree.heading("Days Rented", text="Days Rented")
        self.tree.heading("Total", text="Total")

        self.tree.column("ID", width=0, stretch=tk.NO)

        rentals = self.db.fetch_rentals()
        if search_term:
            rentals = [rental for rental in rentals if search_term.lower() in rental[1].lower() or
                   search_term.lower() in rental[2].lower() or
                   search_term.lower() in rental[3].lower()]

        for rental in rentals:
            self.tree.insert('', tk.END, values=(rental[0], rental[1], rental[2], rental[3], rental[4], rental[5], rental[6], rental[7]))

        self.tree.pack(fill=tk.BOTH, expand=True, padx=20, pady=10)

    def show_rental_form(self):
        rent_window = tk.Toplevel(self.window)
        rent_window.title("Rental Information")
        rent_window.resizable(True, True)

        window_width = 1050
        window_height = 550

        screen_width = rent_window.winfo_screenwidth()
        screen_height = rent_window.winfo_screenheight()

        center_x = int(screen_width / 2 - window_width / 2)
        center_y = int(screen_height / 2 - window_height / 2)

        rent_window.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')

        tk.Label(rent_window, text="Customer's Name", font=("Times", 12)).grid(row=0, column=0)
        name_entry = tk.Entry(rent_window, width=25)
        name_entry.grid(row=0, column=1, pady=8)

        tk.Label(rent_window, text="Contact Number", font=("Times", 12)).grid(row=1, column=0)
        contact_entry = tk.Entry(rent_window, width=25)
        contact_entry.grid(row=1, column=1, pady=8)

        tk.Label(rent_window, text="Type of Vehicle", font=("Times", 12)).grid(row=2, column=0)
        vehicle_types = [
            "Honda BR-V", "Honda HR-V", "Honda Brio", "Honda Civic", "Toyota Hilux",
            "Toyota Innova MPV", "Toyota Wigo G-CVT", "Toyota Tundra", "Toyota Sienna",
            "Toyota Camry", "Honda CR-V", "Ford Fusion", "Ford Explorer", "Kia Carnival",
            "Honda Odyssey", "Ford Transit", "Mercedes-Benz Sprinter", "Chevrolet Express",
            "Nissan Livina", "Ford Everest", "Ford Everest Titanium", "Nissan NV350",
            "Chevrolet Equinox", "Chevrolet Colorado Z71", "Mercedes-Benz EQV",
            "GMC Savana", "Rivian R1T", "Honda Freed", "Chrysler Pacifica Pinnacle",
            "Mitsubishi Xpander MVP", "Mitsubishi Mirage"
        ]
        vehicle_combobox = ttk.Combobox(rent_window, values=vehicle_types, width=23, font=("Times", 10))
        vehicle_combobox.grid(row=2, column=1, pady=8)

        tk.Label(rent_window, text="Rent Date", font=("Times", 12)).grid(row=3, column=0)
        date_entry = tk.Entry(rent_window, width=25)
        date_entry.grid(row=3, column=1, pady=8)

        tk.Label(rent_window, text="Rent Due", font=("Times", 12)).grid(row=4, column=0)
        due_entry = tk.Entry(rent_window, width=25)
        due_entry.grid(row=4, column=1, pady=8)

        tk.Label(rent_window, text="Days Rented", font=("Times", 12)).grid(row=5, column=0)
        day_rent_entry = tk.Entry(rent_window, width=25)
        day_rent_entry.grid(row=5, column=1, pady=8)

        tk.Label(rent_window, text="Cost per day", font=("Times", 12)).grid(row=6, column=0)
        cost_entry = tk.Entry(rent_window, width=25)
        cost_entry.grid(row=6, column=1, pady=8)
        cost_entry.insert(0, "4120")

        tk.Label(rent_window, text="Total:", font=("Times", 12)).grid(row=7, column=0)
        total_label = tk.Label(rent_window, width=25)
        total_label.grid(row=7, column=1, pady=8)

        def submit():
            try:
                day_rent = int(day_rent_entry.get())
                cost = int(cost_entry.get())
                total_cost = day_rent * cost
                total_label.config(text=f"Total Cost: ₱{total_cost:,}")

                # Save rental info to the database
                customer_name = name_entry.get()
                contact_number = contact_entry.get()
                vehicle = vehicle_combobox.get()
                rent_date = date_entry.get()
                rent_due = due_entry.get()
                days_rented = day_rent_entry.get()

                # Ensure the required fields are filled
                if not all([customer_name, contact_number, vehicle, rent_date, rent_due]):
                    messagebox.showwarning("Incomplete Data", "Please fill all fields.")
                    return

                self.db.rent_car(customer_name, contact_number, vehicle, rent_date, rent_due, day_rent, total_cost)
                messagebox.showinfo("Success", "Rental Confirmed!")
                self.display_rentals()  # Refresh the rental display

                rent_window.destroy()  # Close the rental window
            except ValueError:
                messagebox.showerror("Input Error", "Please enter valid numbers for days and cost.")

        button = tk.Button(rent_window, text="Enter", command=submit)
        button.config(height=2, width=4)
        button.grid(row=9, column=1, columnspan=3, pady=6)

    def show_gallery(self):
        gallery_window = tk.Toplevel(self.window)
        gallery_window.title("CAR GALLERY")

        frame = tk.Frame(gallery_window)
        frame.pack()

        car_images = {
            "Honda BR-V": "hondabr-v.jpg",
            "Honda HR-V": "hondahr-v.jpg",
            "Honda Brio": "hondab.jpg",
            "Honda Civic": "hondac.jpg",
            "Honda CR-V": "hondacr-v.jpg",
            "Toyota Hilux": "toyotahilux.jpg",
            "Toyota Innova MPV": "toyotainn.jpg",
            "Toyota Wigo G-CVT": "toyotawig.jpg",
            "Toyota Sienna": "toyotas.jpg",
            "Toyota Camry": "toyotac.jpg",
            "Ford Fusion": "fordf.jpg",
            "Ford Explorer": "fordex.jpg",
            "Kia Carnival": "kiac.png",
            "Honda Odyssey": "hondaodyssey.jpg",
            "Ford Transit": "fordtransit.jpg",
            "Mercedes-Benz Sprinter": "mercedes.jpg",
            "Chevrolet Express": "chevroletexpress.jpg",
            "Nissan Livina": "nissanlivina.jpg",
            "Ford Everest": "fordeverest.jpg",
            "Ford Everest Titanium": "fordeverestitanium.jpg",
            "Nissan NV350": "nissan.jpg",
            "Chevrolet Equinox": "chevroletequinnox.jpg",
            "Chevrolet Colorado Z71": "chevroletcolorado.jpg",
            "Mercedes-Benz EQV": "mercedesbenzeqv.jpg",
            "GMC Savana": "gmcsavana.jpg",
            "Rivian R1T": "rivianr1t.jpg",
            "Honda Freed": "hondafreed.jpg",
            "Chrysler Pacifica Pinnacle": "chrysler.jpg",
            "Mitsubishi Xpander MVP": "mitsubishix.jpg",
            "Mitsubishi Mirage": "mitsubishim.jpg"
        }

        car_images_tk = {}
        for brand, image_path in car_images.items():
            try:
                image = Image.open(image_path).resize((200, 100), Image.LANCZOS)
                car_images_tk[brand] = ImageTk.PhotoImage(image)
            except FileNotFoundError:
                messagebox.showwarning("Image Error", f"Image {image_path} not found.")

        row = 0
        column = 0
        for brand, image_tk in car_images_tk.items():
            label = tk.Label(frame, text=brand, image=image_tk)
            label.image = image_tk  # Keep a reference to avoid garbage collection
            label.grid(row=row, column=column, padx=12, pady=6)

            button = tk.Button(frame, text=brand, command=lambda b=brand: self.show_details(b))
            button.grid(row=row + 1, column=column, padx=20, pady=20)

            column += 1
            if column > 5:
                column = 0
                row += 2

    def show_details(self, brand):
        messagebox.showinfo("Car Details", f"You clicked on {brand}!")

    def show_update_form(self):
        selected_item = self.tree.selection()

        if not selected_item:
            messagebox.showwarning("No Selection", "Please select a rental to update.")
            return

        rental_data = self.tree.item(selected_item)['values']

        customer_name = simpledialog.askstring("Update", f"Edit Customer Name ({rental_data[1]}):", initialvalue=rental_data[1])
        contact_number = simpledialog.askstring("Update", f"Edit Contact Number ({rental_data[2]}):", initialvalue=rental_data[2])
        car = simpledialog.askstring("Update", f"Edit Car ({rental_data[3]}):", initialvalue=rental_data[3])
        date_rented = simpledialog.askstring("Update", f"Edit Date Rented ({rental_data[4]}):", initialvalue=rental_data[4])
        rent_due = simpledialog.askstring("Update", f"Edit Rent Due ({rental_data[5]}):", initialvalue=rental_data[5])
        days_rented = simpledialog.askstring("Update", f"Edit Days Rented ({rental_data[6]}):", initialvalue=rental_data[6])

        if not all([customer_name, contact_number, car, date_rented, rent_due, days_rented]):
            messagebox.showwarning("Incomplete Data", "All fields must be filled.")
            return

        rental_id = rental_data[0]
        self.db.update_rental(rental_id, customer_name, contact_number, car, date_rented, rent_due, days_rented)
        self.display_rentals()
        messagebox.showinfo("Success", "Rental Updated!")

    def delete_rent(self):
        selected_item = self.tree.selection()

        if not selected_item:
            messagebox.showwarning("No Selection", "Please select a rental to delete.")
            return

        confirm = messagebox.askyesno("Confirm Delete", "Are you sure you want to delete this rental?")

        if confirm:
            rental_id = self.tree.item(selected_item)['values'][0]
            self.db.delete_rental(rental_id)
            self.display_rentals()
            messagebox.showinfo("Deleted", "Rental deleted successfully.")

    def show_search_dialog(self):
        search_term = simpledialog.askstring("Search Rentals", "Enter name, contact, or car to search:")
        if search_term:
            self.display_rentals(search_term)

if __name__ == "__main__":
    Dashboard()
