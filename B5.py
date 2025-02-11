import customtkinter as ctk

class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        
        self.title("4 Frames Pack Layout")
        self.geometry("500x300")
        self.resizable(width=False, height=False)

        top_container = ctk.CTkFrame(self, height=150)
        top_container.pack(side="top", fill="x")
        top_container.pack_propagate(False)
        
        bottom_container = ctk.CTkFrame(self, height=150)
        bottom_container.pack(side="bottom", fill="x")
        bottom_container.pack_propagate(False)
        
        frame1 = ctk.CTkFrame(top_container, fg_color="yellow", width=250)
        frame1.pack(side="left", fill="y")
        frame1.pack_propagate(False)
        
        frame2 = ctk.CTkFrame(top_container, fg_color="red", width=250)
        frame2.pack(side="right", fill="y")
        frame2.pack_propagate(False)
        
        frame3 = ctk.CTkFrame(bottom_container, fg_color="gray", width=250)
        frame3.pack(side="left", fill="y")
        frame3.pack_propagate(False)
        
        frame4 = ctk.CTkFrame(bottom_container, fg_color="blue", width=250)
        frame4.pack(side="right", fill="y")
        frame4.pack_propagate(False)

if __name__ == "__main__":
    app = App()
    app.mainloop()