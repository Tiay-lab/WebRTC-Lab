import tkinter as tk

app = tk.Tk()
app.title("Ứng dụng của tôi")
app.geometry("300x150") # Kích thước cửa sổ

# Tạo nhãn hiển thị chữ Hello
label = tk.Label(app, text="Hello", font=("Arial", 24))
label.pack(expand=True)

app.mainloop()