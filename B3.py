import customtkinter as ctk

class App(ctk.CTk):
    def __init__(self, start=0, end=50):
        super().__init__()

        self.title("1000 Buttons App")
        self.geometry("500x300")
        self.resizable(width=False, height=False)

        self.main_frame = ctk.CTkScrollableFrame(self)
        self.main_frame.pack(fill="both", expand=True)
        
        self.create_buttons(start, end)

    def create_buttons(self, start, end):
        for i in range(start, end):
            button = ctk.CTkButton(
                self.main_frame,
                text=f"Button {i+1}"
            )
            button.pack(pady=5)
        
        self.main_frame.update_idletasks()
        
        if end < 1000:
            self.after(1000, self.create_buttons, end, min(end + 50, 1000))

if __name__ == "__main__":
    app = App(0, 50)
    app.mainloop()