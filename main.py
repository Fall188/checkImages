import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk

# 当前显示的图片索引
current_image_index = -1
# 存储打开的图片对象
images = []
# 图片显示的Label引用
image_label = None

# 打开文件并加载图片
def open_files():
    global images, current_image_index
    file_paths = filedialog.askopenfilenames(
        defaultextension=".jpg", filetypes=[("图片", "*.jpg *.jpeg *.png")]
    )
    for path in file_paths:
        image = Image.open(path)
        photo = ImageTk.PhotoImage(image)
        images.append(photo)
    if images:
        current_image_index = 0
        show_image(images[current_image_index])

# 展示图片
def show_image(image):
    global image_label
    if image_label is None:
        image_label = tk.Label(root)
        image_label.pack()
    image_label.configure(image=image)

# 显示下一张图片
def next_image():
    global current_image_index
    if images and current_image_index < len(images) - 1:
        current_image_index += 1
        show_image(images[current_image_index])

# 显示上一张图片
def previous_image():
    global current_image_index
    if images and current_image_index > 0:
        current_image_index -= 1
        show_image(images[current_image_index])

# 创建窗体
root = tk.Tk()
root.geometry("300x300")
root.title("图片查看器")

# 创建菜单栏
menu_bar = tk.Menu(root)
root.config(menu=menu_bar)

# 设置菜单栏
main_menu = tk.Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="菜单", menu=main_menu)
main_menu.add_command(label="打开图片", command=lambda: open_files())
main_menu.add_separator()  # 分割线
main_menu.add_command(label="退出", command=root.quit)

# 图片切换按钮
btn_frame = tk.Frame(root)
btn_frame.pack(fill=tk.X, side=tk.BOTTOM)

prev_button = tk.Button(btn_frame, text="上一张", command=previous_image)
prev_button.pack(side=tk.LEFT, expand=True, fill=tk.X)

next_button = tk.Button(btn_frame, text="下一张", command=next_image)
next_button.pack(side=tk.RIGHT, expand=True, fill=tk.X)

root.mainloop()
