import random, time
import tkinter as tk
from ring_test import RingTest, HoleyRing


class App:

    def __init__(self):
        self.current_test_size = None
        self.canvas = None
        self.canvassize = 700
        self.frm_test = None
        self.frm_controls = None
        sizes = [5, 20, 50, 110, 230]
        self.ring_test = RingTest(self.canvassize/2, sizes)

    def main(self):
        window = tk.Tk()
        window.title('The Lord of the Holey Rings')
        self.frm_test = tk.Frame(master=window, width=900, height=900, bg='darkgrey', borderwidth=2, relief='sunken')
        lbl_test_head = tk.Label(master=self.frm_test, text="Test", bg='black', fg='white', font=("Arial", 50, 'bold'))
        lbl_test_head.place(x=0, y=0)

        self.current_test_size = tk.StringVar()
        self.current_test_size.set("")
        lbl_test_size = tk.Label(master=self.frm_test, textvariable=self.current_test_size, bg='black', fg='white', font=("Arial", 50, 'bold'))
        lbl_test_size.place(x=200, y=0)

        self.frm_controls = tk.Frame(master=window, width=900, height=900, bg='darkgrey', borderwidth=2, relief='sunken')
        lbl_controls_head = tk.Label(master=self.frm_controls, text="Controls", bg='black', fg='white', font=("Arial", 50, 'bold'))
        lbl_controls_head.place(x=0, y=0)

        self.frm_test.pack(fill=tk.Y, side=tk.LEFT)
        self.frm_controls.pack(fill=tk.Y, side=tk.RIGHT)
        self.draw_new_random_circle()

        window.mainloop()

    def create_circle(self, x, y, r, is_hole, line_width):
        x0 = x - r
        y0 = y - r
        x1 = x + r
        y1 = y + r
        if is_hole:
            outline = 'black'
            fill = 'black'
        else:
            outline = 'white'
            fill = ''
        self.canvas.create_oval(x0, y0, x1, y1, width=line_width, outline=outline, fill=fill)

    def create_test_circle(self, master, ring):
        self.canvas = tk.Canvas(master=master, width=self.canvassize, height=self.canvassize, bg='black')
        self.canvas.bind("<Button-1>", self.canvas_clicked)
        self.canvas.place(x=100, y=200)

        self.create_circle(ring.center_position, ring.center_position, ring.circle_radius, False, ring.line_width)

        self.create_circle(ring.hole_position[0], ring.hole_position[1], ring.hole_radius, True, 1)

    def canvas_clicked(self, event):
        ring = self.ring_test.current_ring()
        if abs(event.x - ring.hole_position[0]) < ring.hole_radius \
                and abs(event.y - ring.hole_position[1]) < ring.hole_radius:
            print("yes")
        else:
            print("no")
        self.draw_new_random_circle()

    def draw_new_random_circle(self):
        if self.canvas:
            self.canvas.delete("all")
            self.canvas.update_idletasks()
            time.sleep(0.5)
        if self.ring_test.next_ring():
            self.current_test_size.set(self.ring_test.current_ring().circle_radius)
            self.create_test_circle(self.frm_test, self.ring_test.current_ring())
        else:
            self.current_test_size.set("Done")
