import os
from io import BytesIO
from tkinter import filedialog
from tkinter import *
from PIL import Image


def process_image(file_path, size):
    if not os.path.isfile(file_path):
        print(f"Error: {file_path} not found.")
        return

    try:
        image = Image.open(file_path)
    except IOError:
        print(f"Error: {file_path} is not a valid image file.")
        return

    print(f"Processing image {file_path} to size {size}x{size}")


    # Resize the image and save it to a buffer
    resized_image = image.copy()
    resized_image.thumbnail((size, size))
    buffer = BytesIO()
    resized_image.save(buffer, format=image.format)


    # Save the resized image to a file
    buffer.seek(0)
    filename, file_extension = os.path.splitext(file_path)
    output_filename = f"{filename}_{size}x{size}{file_extension}"
    with open(output_filename, "wb") as f:
        f.write(buffer.getvalue())

    print(f"Resized image saved as {output_filename}")


def browse_image():
    global selected_file
    global success_message
    selected_file = StringVar()
    filename_label.config(text="")
    file_path = filedialog.askopenfilename(title="Select an image", filetypes=[("Image files", "*.jpg;*.jpeg;*.png;*.bmp;*.gif")])
    if file_path:
        filename_label.config(text=f"Selected file: {os.path.basename(file_path)}")
        selected_file.set(file_path)
        resize_button.config(state="normal")

def resize_image():
    file_path = selected_file.get()
    process_images(file_path)

def process_images(file_path):
    sizes = []

    if size_emote_var.get():
        sizes.append(128)
        sizes.append(56)
        sizes.append(28)
    if size_badge_var.get():
        sizes.append(72)
        sizes.append(36)
        sizes.append(18)
    if custom_size_var.get():
        try:
            custom_size = int(custom_size_entry.get())
            sizes.append(custom_size)
        except ValueError:
            print("Error: Custom size must be an integer value.")

    for size in sizes:
        process_image(file_path, size)

    show_success_message()

def show_success_message():
    global success_message
    success_message = Label(root, text="Images resized successfully!", fg="green", font=("Arial", 12))
    success_message.pack(pady=10)
def clear_success_message():
    global success_message
    if success_message and success_message.winfo_exists():
        success_message.destroy()

root = Tk()
root.title("Image Resizer")

frame = Frame(root)
frame.pack(padx=10, pady=10)

select_image_button = Button(frame, text="Select Image", command=browse_image, font=("Arial", 12))
select_image_button.grid(row=0, column=0, padx=5, pady=5)

resize_button = Button(frame, text="Resize", command=resize_image, font=("Arial", 12), state=DISABLED)
resize_button.grid(row=0, column=1, padx=5, pady=5)

size_emote_var = IntVar()
size_emote_checkbox = Checkbutton(frame, text="Twitch Emotes", variable=size_emote_var, font=("Arial", 10))
size_emote_checkbox.grid(row=1, column=0, padx=5, pady=5)

size_badge_var = IntVar()
size_badge_checkbox = Checkbutton(frame, text="Twitch Badges", variable=size_badge_var, font=("Arial", 10))
size_badge_checkbox.grid(row=2, column=0, padx=5, pady=5)

selected_file_label = Label(frame, text="", font=("Arial", 10))
selected_file_label.grid(row=0, column=2, padx=5, pady=5)

filename_label = Label(frame, text="", font=("Arial", 10))
filename_label.grid(row=3, column=0, columnspan=2, pady=5)

custom_size_var = IntVar()
custom_size_checkbox = Checkbutton(frame, text="Custom size:", variable=custom_size_var, font=("Arial", 10))
custom_size_checkbox.grid(row=4, column=0, padx=5, pady=5)

custom_size_entry = Entry(frame)
custom_size_entry.grid(row=4, column=1, padx=5, pady=5)

root.mainloop()