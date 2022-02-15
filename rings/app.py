import tkinter as tk


def create_circle(x, y, r, canvas):
    x0 = x - r
    y0 = y - r
    x1 = x + r
    y1 = y + r
    return canvas.create_oval(x0, y0, x1, y1, width=5, outline="white")

def calculate_button_position(button_center_position, buttonsize, circleradius, position):
    # TODO fix button position because of circle arc
    # TODO use circle instead of rectancle button? do not use button?
    halfbuttonsize = buttonsize/2
    if position == 0:
        x = button_center_position
        y = button_center_position - circleradius
    elif position == 1:
        x = button_center_position + (circleradius/2) + halfbuttonsize
        y = button_center_position - (circleradius/2) - halfbuttonsize
    elif position == 2:
        x = button_center_position + circleradius
        y = button_center_position
    elif position == 3:
        x = button_center_position + (circleradius/2) + halfbuttonsize
        y = button_center_position + (circleradius/2) + halfbuttonsize
    elif position == 4:
        x = button_center_position
        y = button_center_position + circleradius
    elif position == 5:
        x = button_center_position - (circleradius/2) - halfbuttonsize
        y = button_center_position + (circleradius/2) + halfbuttonsize
    elif position == 6:
        x = button_center_position - circleradius
        y = button_center_position
    else:
        x = button_center_position - (circleradius/2) - halfbuttonsize
        y = button_center_position - (circleradius/2) - halfbuttonsize
    return x, y


def create_test_circle(master, circleradius):
    canvassize = 700
    canvas = tk.Canvas(master=master, width=canvassize, height=canvassize, bg='black')
    canvas.bind("<Button-1>", choice_not_right)
    canvas.place(x=100, y=200)

    create_circle(canvassize/2, canvassize/2, circleradius, canvas)

    buttonsize = circleradius/2
    button_center_position = (canvassize/2) - (buttonsize/2)
    buttonposition_x, buttonposition_y = calculate_button_position(button_center_position, buttonsize, circleradius, 1)

    pixel = tk.PhotoImage(width=1, height=1)
    btn_right = tk.Button(master=canvas, relief='flat', bg='grey', borderwidth=0,
                          highlightthickness=0, fg='black', text="", image=pixel,
                          width=buttonsize, height=buttonsize, compound='center')
    btn_right.bind("<Button-1>", choice_right)
    btn_right.place(x=buttonposition_x, y=buttonposition_y)

def choice_not_right(event):
    print("no")

def choice_right(event):
    print("yes")

def main():
    window = tk.Tk()
    window.title('The Lord of the Holey Rings')
    frm_test = tk.Frame(master=window, width=900, height=900, bg='darkgrey', borderwidth=2, relief='sunken')
    lbl_test_head = tk.Label(master=frm_test, text="Test", bg='black', fg='white', font=("Arial", 50, 'bold'))
    lbl_test_head.place(x=0, y=0)

    frm_controls = tk.Frame(master=window, width=900, height=900, bg='darkgrey', borderwidth=2, relief='sunken')
    lbl_controls_head = tk.Label(master=frm_controls, text="Controls", bg='black', fg='white', font=("Arial", 50, 'bold'))
    lbl_controls_head.place(x=0, y=0)

    create_test_circle(frm_test, 50)
    frm_test.pack(fill=tk.Y, side=tk.LEFT)
    frm_controls.pack(fill=tk.Y, side=tk.RIGHT)

    window.mainloop()
