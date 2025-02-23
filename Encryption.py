from tkinter import *
from tkinter import filedialog
from PIL import Image, ImageTk
import os
from stegano import lsb  # pip install stegano

# Setup the main window (root)
root = Tk()
root.title("Steganography - Encrypt Message (Hide Message)")
root.geometry("700x500+150+180")
root.resizable(False, False)
root.configure(bg="#2f4155")

# Function to show the image on the GUI
def showimage():
    global filename
    filename = filedialog.askopenfilename(initialdir=os.getcwd(), title='Select Image File', filetypes=[("PNG file", "*.png"), ("JPG File", "*.jpg"), ("All files", "*")])
    img = Image.open(filename)
    img = ImageTk.PhotoImage(img)
    lbl.configure(image=img, width=250, height=250)
    lbl.image = img

# Encryption: Hide secret message in the image
def encrypt_message():
    global secret_image
    message = text1.get(1.0, END).strip()  # Get the message to hide
    if message:
        secret_image = lsb.hide(str(filename), message)  # Hide the message in the image
        text1.delete(1.0, END)
        text1.insert(END, "Message hidden in image successfully.")
    else:
        text1.delete(1.0, END)
        text1.insert(END, "Please enter a message to hide.")

# Save the new image (with hidden message)
def save_image():
    global secret_image
    secret_image.save("hidden_image.png")
    text1.delete(1.0, END)
    text1.insert(END, "Hidden image saved as 'hidden_image.png'.")

# GUI Components
image_icon = PhotoImage(file="logo.jpg")
root.iconphoto(False, image_icon)

# Logo and Title
logo = PhotoImage(file="logo.png")
Label(root, image=logo, bg="#2f4155").place(x=10, y=0)
Label(root, text="DATAVEIL", bg="#2d4155", fg="white", font="arial 25 bold").place(x=100, y=20)

# Image Display Frame
f = Frame(root, bd=3, bg="black", width=340, height=280, relief=GROOVE)
f.place(x=10, y=80)

lbl = Label(f, bg="black")
lbl.place(x=40, y=10)

# Message Text Area
frame2 = Frame(root, bd=3, width=340, height=280, bg="white", relief=GROOVE)
frame2.place(x=350, y=80)

text1 = Text(frame2, font="Roboto 20", bg="white", fg="black", relief=GROOVE, wrap=WORD)
text1.place(x=10, y=0, width=320, height=295)

scrollbar1 = Scrollbar(frame2)
scrollbar1.place(x=320, y=0, height=300)
scrollbar1.configure(command=text1.yview)
text1.configure(yscrollcommand=scrollbar1.set)

# Buttons for Opening, Saving, Encrypting
frame3 = Frame(root, bd=3, bg="#2f4155", width=330, height=100, relief=GROOVE)
frame3.place(x=10, y=370)

Button(frame3, text="Open Image", width=10, height=2, font="arial 14 bold", command=showimage).place(x=20, y=30)
Button(frame3, text="Save Image", width=10, height=2, font="arial 14 bold", command=save_image).place(x=180, y=30)
Label(frame3, text="Picture, Image, Photo File", bg="#2f4155", fg="pink").place(x=20, y=5)

frame4 = Frame(root, bd=3, bg="#2f4155", width=330, height=100, relief=GROOVE)
frame4.place(x=360, y=370)

Button(frame4, text="Hide Message", width=10, height=2, font="arial 14 bold", command=encrypt_message).place(x=20, y=30)
Label(frame4, text="Picture, Image, Photo File", bg="#2f4155", fg="pink").place(x=20, y=5)

# Run the main loop
root.mainloop()
