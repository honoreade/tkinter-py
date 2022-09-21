from tkinter import *


def btn_clicked():
    print("Button Clicked")


window = Tk()

window.geometry("816x549")
window.configure(bg = "#ffffff")
canvas = Canvas(
    window,
    bg = "#ffffff",
    height = 549,
    width = 816,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge")
canvas.place(x = 0, y = 0)

img0 = PhotoImage(file = f"img0.png")
b0 = Button(
    image = img0,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_clicked,
    relief = "flat")

b0.place(
    x = 556, y = 365,
    width = 99,
    height = 38)

background_img = PhotoImage(file = f"background.png")
background = canvas.create_image(
    408.0, 247.0,
    image=background_img)

window.resizable(False, False)
window.mainloop()
