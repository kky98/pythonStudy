from tkinter import *
from PIL import Image, ImageTk
# pip install pillow
# constants
jump_height = 10

# functions
def create_ball(canvas):
    global ball_image
    img = Image.open('hoho.png')  # replace 'your_image.png' with your image file path
    img = img.resize((50, 50))
    ball_image = ImageTk.PhotoImage(img)
    canvas.create_image(100, 350, image=ball_image, tag='ho')
def move_left(event):
    print("왼쪽이동")
    canvas.move('ho', -5, 0)
    canvas.after(20)
    canvas.update()
def move_right(event):
    canvas.move('ho', 5, 0)
    canvas.after(20)
    canvas.update()
def jump(event):
    # Move the ball upwards
    for _ in range(jump_height):
        canvas.move('ho', 0, -20)
        canvas.update()
        canvas.after(20)
    # Make the ball fall down with a bounce
    for _ in range(jump_height):
        canvas.move('ho', 0, 20)
        canvas.update()
        canvas.after(20)
    # Bounce a few times
    for _ in range(3):
        for _ in range(2):
            canvas.move('ho', 0, -10)
            canvas.update()
            canvas.after(20)
        for _ in range(2):
            canvas.move('ho', 0, 10)
            canvas.update()
            canvas.after(20)

# setting up Tkinter window
window = Tk()
canvas = Canvas(window, width=400, height=400)
canvas.pack()

create_ball(canvas)
canvas.bind('<Left>', move_left)
canvas.bind('<Right>', move_right)
canvas.bind('<space>', jump)
canvas.focus_set()
canvas.pack()
window.mainloop()
