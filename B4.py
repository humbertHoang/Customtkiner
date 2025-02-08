import customtkinter as ctk

class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        
        self.title("4 Frames Grid Layout")
        self.geometry("500x300")
        self.resizable(width=False, height=False)
        
        self.grid_rowconfigure((0, 1), weight=1)
        self.grid_columnconfigure((0, 1), weight=1)

        # Frame 1
        self.frame1 = ctk.CTkFrame(self, fg_color="yellow")
        self.frame1.grid(row=0, column=0, sticky="nsew")
        
        # Frame 2
        self.frame2 = ctk.CTkFrame(self, fg_color="red")
        self.frame2.grid(row=0, column=1, sticky="nsew")
        
        # Frame 3
        self.frame3 = ctk.CTkFrame(self, fg_color="gray")
        self.frame3.grid(row=1, column=0, sticky="nsew")
        
        # Frame 4
        self.frame4 = ctk.CTkFrame(self, fg_color="blue")
        self.frame4.grid(row=1, column=1, sticky="nsew")

if __name__ == "__main__":
    app = App()
    app.mainloop()