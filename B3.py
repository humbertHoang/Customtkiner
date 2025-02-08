import customtkinter as ctk

class App(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("1000 Buttons App")
        self.geometry("500x300")
        self.resizable(width=False, height=False)

        self.main_frame = ctk.CTkScrollableFrame(self)
        self.main_frame.pack(fill="both", expand=True, padx=10, pady=10)

        for i in range(1000):
            button = ctk.CTkButton(
                self.main_frame,
                text=f"Button {i+1}"
            )
            button.pack(pady=5)

if __name__ == "__main__":
    app = App()
    app.mainloop()