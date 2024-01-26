import tkinter as tk
from tkinter import ttk, messagebox
from tkcalendar import Calendar
import pandas as pd
from PIL import Image, ImageTk
from ttkthemes import ThemedStyle
import os

class Application(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Data Entry App")
        self.geometry("500x400")

        self.name_label = ttk.Label(self, text="Name:")
        self.name_label.grid(row=0, column=0, padx=10, pady=5, sticky="w")
        self.name_entry = ttk.Entry(self)
        self.name_entry.grid(row=0, column=1, padx=10, pady=5)

        self.email_label = ttk.Label(self, text="Email:")
        self.email_label.grid(row=1, column=0, padx=10, pady=5, sticky="w")
        self.email_entry = ttk.Entry(self)
        self.email_entry.grid(row=1, column=1, padx=10, pady=5)

        self.birthdate_label = ttk.Label(self, text="Birthdate:")
        self.birthdate_label.grid(row=2, column=0, padx=10, pady=5, sticky="w")
        self.cal = Calendar(self, date_pattern="yyyy-mm-dd")
        self.cal.grid(row=2, column=1, padx=10, pady=5)

        self.college_label = ttk.Label(self, text="College Name:")
        self.college_label.grid(row=3, column=0, padx=10, pady=5, sticky="w")
        self.college_entry = ttk.Entry(self)
        self.college_entry.grid(row=3, column=1, padx=10, pady=5)

        self.gender_label = ttk.Label(self, text="Gender:")
        self.gender_label.grid(row=4, column=0, padx=10, pady=5, sticky="w")
        self.gender_combo = ttk.Combobox(self, values=["Male", "Female", "Other"])
        self.gender_combo.grid(row=4, column=1, padx=10, pady=5)

        self.submit_button = ttk.Button(self, text="Submit", command=self.submit)
        self.submit_button.grid(row=5, column=0, columnspan=2, pady=10)

        self.style = ThemedStyle(self)
        self.style.set_theme("arc")

    def submit(self):
        name = self.name_entry.get()
        email = self.email_entry.get()
        birthdate = self.cal.get_date()
        college = self.college_entry.get()
        gender = self.gender_combo.get()

        data = {
            "Name": [name],
            "Email": [email],
            "Birthdate": [birthdate],
            "College Name": [college],
            "Gender": [gender]
        }

        df = pd.DataFrame(data)

        try:
            filename = "data.csv"
            df.to_csv(filename, index=False)
            messagebox.showinfo("Success", f"Data saved successfully as {filename}")
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {str(e)}")

if __name__ == "__main__":
    app = Application()
    app.mainloop()
