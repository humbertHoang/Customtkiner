# Bai 1
import customtkinter as ctk
ctk.set_appearance_mode("dark")

app = ctk.CTk()
app.geometry("500x300")
app.resizable(width=False, height=False)
app.title("Phat CustomTkinter ")

button = ctk.CTkButton(app, text="Button", command=lambda: print("Button Clicked"))
button.place(relx=0.5, rely=0.5, anchor="center")
app.mainloop()