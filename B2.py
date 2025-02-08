#Bai 2
import customtkinter as ctk
from PIL import Image
import os
from pathlib import Path

# Cấu hình customtkinter
ctk.set_appearance_mode("System")
ctk.set_default_color_theme("blue")

class App:
    def __init__(self):
        self.root = ctk.CTk()
        self.root.title("iPhone Products")
        self.root.geometry("800x600")
        self.root.resizable(width=False, height=False)
        # Danh sách sản phẩm iPhone (tên và đường dẫn hình ảnh)
        self.products = [
            {"name": "iPhone 13", "image": "iphone13.jpg"},
            {"name": "iPhone 13 Pro", "image": "iphone13pro.jpg"},
            {"name": "iPhone 14", "image": "iphone14.jpg"},
            {"name": "iPhone 14 Pro", "image": "iphone14pro.jpg"},
            {"name": "iPhone 15", "image": "iphone15.jpg"},
            {"name": "iPhone 16", "image": "iphone16.jpg"},
            {"name": "iPhone SE", "image": "iphonese.jpg"},
            {"name": "iPhone 12", "image": "iphone12.jpg"},
            {"name": "iPhone 11", "image": "iphone11.jpg"},
            {"name": "iPhone XR", "image": "iphonexr.jpg"},
        ]
        
        self.setup_ui()
        
    def setup_ui(self):
        # Tạo một frame cuộn
        self.scrollable_frame = ctk.CTkScrollableFrame(self.root)
        self.scrollable_frame.pack(fill="both", expand=True, padx=20, pady=20)
        
        # Thêm sản phẩm
        for i, product in enumerate(self.products):
            row = i // 4
            col = i % 4
            product_frame = self.create_product_frame(product)
            product_frame.grid(row=row, column=col, padx=10, pady=10)
    
    def load_and_resize_image(self, image_path, size=(150, 150)):
        try:
            # Kiểm tra xem file ảnh có tồn tại không
            if not Path(image_path).exists():
                raise FileNotFoundError(f"Image not found: {image_path}")
                
            img = Image.open(image_path)
            return ctk.CTkImage(light_image=img, dark_image=img, size=size)
        except Exception as e:
            print(f"Error loading image {image_path}: {str(e)}")
            # Tạo placeholder khi có lỗi
            placeholder = Image.new('RGB', size, color='gray')
            return ctk.CTkImage(light_image=placeholder, dark_image=placeholder, size=size)

    def create_product_frame(self, product):
        frame = ctk.CTkFrame(master=self.scrollable_frame)
        frame.grid_propagate(False)
        
        # Tải và hiển thị hình ảnh
        image_path = os.path.join("img", product["image"])
        photo = self.load_and_resize_image(image_path)
        
        # Hiển thị hình ảnh
        image_label = ctk.CTkLabel(frame, image=photo, text="")
        image_label.pack(pady=10, expand=True)
        
        # Hiển thị tên sản phẩm
        name_label = ctk.CTkLabel(frame, text=product["name"], 
                                font=ctk.CTkFont(size=14, weight="bold"))
        name_label.pack(pady=(0, 10))
        
        # Đặt kích thước frame
        frame.configure(width=180, height=250)
        
        return frame

if __name__ == "__main__":
    app = App()
    app.root.mainloop()