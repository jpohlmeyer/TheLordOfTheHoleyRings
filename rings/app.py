import time
import tkinter as tk
from ring_test import RingTest


class App:

    def __init__(self):
        self.btn_pixel = None
        self.current_test_size = None
        self.canvas = None
        self.canvassize = 700
        self.window = None
        self.frm_test = None
        self.frm_controls = None
        sizes = [5, 20, 50, 110, 230]
        self.ring_test = RingTest(self.canvassize/2, sizes)

    def main(self):
        self.draw_window()
        self.draw_new_random_circle()
        self.window.mainloop()

    def draw_window(self):
        self.window = tk.Tk()
        self.window.title('The Lord of the Holey Rings')
        self.draw_test_frame()
        self.draw_controls_frame()

    def draw_test_frame(self):
        self.frm_test = tk.Frame(master=self.window, width=900, height=900, bg='darkgrey', borderwidth=2,
                                 relief='sunken')
        lbl_test_head = tk.Label(master=self.frm_test, text="Test", bg='black', fg='white', font=("Arial", 50, 'bold'))
        lbl_test_head.place(x=0, y=0)

        self.current_test_size = tk.StringVar()
        self.current_test_size.set("")
        lbl_test_size = tk.Label(master=self.frm_test, textvariable=self.current_test_size, bg='black', fg='white',
                                 font=("Arial", 50, 'bold'))
        lbl_test_size.place(x=200, y=0)

        self.canvas = tk.Canvas(master=self.frm_test, width=self.canvassize, height=self.canvassize, bg='black')
        self.canvas.bind("<Button-1>", self.canvas_clicked)
        self.canvas.place(x=100, y=200)

        self.frm_test.pack(fill=tk.Y, side=tk.LEFT)

    def draw_controls_frame(self):
        self.frm_controls = tk.Frame(master=self.window, width=900, height=900, bg='darkgrey', borderwidth=2,
                                     relief='sunken')
        lbl_controls_head = tk.Label(master=self.frm_controls, text="Controls", bg='black', fg='white',
                                     font=("Arial", 50, 'bold'))
        lbl_controls_head.place(x=0, y=0)

        frm_buttons = tk.Frame(master=self.frm_controls, bg='darkgrey')
        frm_buttons.place(x=200, y=200)

        self.btn_pixel = tk.PhotoImage(master=self.window, width=1, height=1)
        self.btn_n = self.make_btn(0, frm_buttons)
        btn_ne = self.make_btn(1, frm_buttons)
        btn_e = self.make_btn(2, frm_buttons)
        btn_se = self.make_btn(3, frm_buttons)
        btn_s = self.make_btn(4, frm_buttons)
        btn_sw = self.make_btn(5, frm_buttons)
        btn_w = self.make_btn(6, frm_buttons)
        btn_nw = self.make_btn(7, frm_buttons)

        self.btn_n.grid(column=1, row=1)
        btn_ne.grid(column=2, row=1)
        btn_e.grid(column=2, row=2)
        btn_se.grid(column=2, row=3)
        btn_s.grid(column=1, row=3)
        btn_sw.grid(column=0, row=3)
        btn_w.grid(column=0, row=2)
        btn_nw.grid(column=0, row=1)

        self.frm_controls.pack(fill=tk.Y, side=tk.RIGHT)

    def make_btn(self, type, master):
        if type == 0:
            text = "↑"
        elif type == 1:
            text = "↗"
        elif type == 2:
            text = "→"
        elif type == 3:
            text = "↘"
        elif type == 4:
            text = "↓"
        elif type == 5:
            text = "↙"
        elif type == 6:
            text = "←"
        else:
            text = "↖"

        btn = tk.Button(master=master, text=text, font=("Arial", 50, 'bold'), bg='black', fg='white',
                  activebackground='darkgrey', image=self.btn_pixel, width=100, height=100, compound='center', padx=0,
                  pady=0)
        btn.bind("<Enter>", func=lambda event, a=btn: self.btn_hover_enter(a))
        btn.bind("<Leave>", func=lambda event, a=btn: self.btn_hover_leave(a))
        btn.bind("<Button-1>", func=lambda event, a=btn, b=type: self.btn_press(a, b))
        return btn

    def btn_hover_enter(self, btn):
        btn.configure(bg='white')

    def btn_hover_leave(self, btn):
        btn.configure(bg='black')
        btn.configure(activebackground='darkgrey')

    def btn_press(self, btn, type):
        ring = self.ring_test.current_ring()
        if ring.hole_type == type:
            btn.configure(activebackground='green')
        else:
            btn.configure(activebackground='red')
        self.draw_new_random_circle()

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

    def draw_holey_ring(self, ring):
        self.create_circle(ring.center_position, ring.center_position, ring.circle_radius, False, ring.line_width)
        self.create_circle(ring.hole_position[0], ring.hole_position[1], ring.hole_radius, True, 1)

    def draw_new_random_circle(self):
        if self.ring_test.ring_index > -1:
            self.canvas.delete("all")
            self.canvas.update_idletasks()
            time.sleep(0.5)
        if self.ring_test.next_ring():
            self.current_test_size.set(self.ring_test.current_ring().circle_radius)
            self.draw_holey_ring(self.ring_test.current_ring())
        else:
            self.current_test_size.set("Done")

    def canvas_clicked(self, event):
        ring = self.ring_test.current_ring()
        if abs(event.x - ring.hole_position[0]) < ring.hole_radius \
                and abs(event.y - ring.hole_position[1]) < ring.hole_radius:
            print("yes")
        else:
            print("no")
        self.draw_new_random_circle()
