import time
import tkinter as tk
from rings.ring_test import RingTest


class App:
    SIZES = [2, 4, 8, 16, 32]
    CANVASSIZE = 100
    SECONDS_RING_IS_SHOWN = 1
    START_DELAY = 0.5

    def __init__(self):
        self.ring_test = None
        self.btn_pixel = None
        self.current_test_size = None
        self.canvas = None
        self.window = None
        self.frm_test = None
        self.frm_controls = None

    def main(self):
        self.draw_window()
        self.window.mainloop()

    def draw_window(self):
        self.window = tk.Tk()
        self.window.title('The Lord of the Holey Rings')
        self.btn_pixel = tk.PhotoImage(master=self.window, width=1, height=1)
        self.draw_test_frame()
        self.draw_controls_frame()

    def draw_test_frame(self):
        self.frm_test = tk.Frame(master=self.window, width=900, height=900, bg='darkgrey', borderwidth=2,
                                 relief='sunken')
        self.frm_test.pack(fill=tk.Y, side=tk.LEFT)

    def clear_test_frame(self):
        for widget in self.frm_test.winfo_children():
            widget.destroy()

    def draw_controls_frame(self):
        self.frm_controls = tk.Frame(master=self.window, width=900, height=900, bg='darkgrey', borderwidth=2,
                                     relief='sunken')

        frm_control_buttons = tk.Frame(master=self.frm_controls, bg='darkgrey')
        frm_control_buttons.place(x=100, y=100)

        btn_start_black_test = tk.Button(master=frm_control_buttons, text='Start Black Test', font=("Arial", 50, 'bold'),
                                         fg='white', activebackground='darkgrey', image=self.btn_pixel,
                                         bg='black', height=100, compound='center', padx=0, pady=0, command=self.start_black_test)

        btn_start_black_test.grid(row=0, column=0)

        btn_start_white_test = tk.Button(master=frm_control_buttons, text='Start White Test',
                                         font=("Arial", 50, 'bold'),
                                         fg='white', activebackground='darkgrey', image=self.btn_pixel,
                                         bg='black', height=100, compound='center', padx=0, pady=0,
                                         command=self.start_white_test)

        btn_start_white_test.grid(row=1, column=0)

        self.frm_controls.pack(fill=tk.Y, side=tk.RIGHT)

    def start_black_test(self):
        self.ring_test = RingTest(self.CANVASSIZE / 2, self.SIZES, True, time.time())
        self.draw_test()

    def start_white_test(self):
        self.ring_test = RingTest(self.CANVASSIZE / 2, self.SIZES, False, time.time())
        self.draw_test()

    def draw_test(self):
        self.clear_test_frame()
        lbl_test_head = tk.Label(master=self.frm_test, text="Test", bg='black', fg='white', font=("Arial", 50, 'bold'))
        lbl_test_head.place(x=0, y=0)

        self.current_test_size = tk.StringVar()
        self.current_test_size.set("")
        lbl_test_size = tk.Label(master=self.frm_test, textvariable=self.current_test_size, bg='black', fg='white',
                                 font=("Arial", 50, 'bold'))
        lbl_test_size.place(x=200, y=0)

        if self.ring_test.is_black:
            bg_color = 'black'
        else:
            bg_color = 'white'

        self.canvas = tk.Canvas(master=self.frm_test, width=self.CANVASSIZE, height=self.CANVASSIZE, bg=bg_color)
        self.canvas.place(x=400, y=200)

        frm_buttons = tk.Frame(master=self.frm_test, bg='darkgrey')
        frm_buttons.place(x=300, y=300 + self.CANVASSIZE)

        btn_n = self.make_btn(0, frm_buttons)
        btn_ne = self.make_btn(1, frm_buttons)
        btn_e = self.make_btn(2, frm_buttons)
        btn_se = self.make_btn(3, frm_buttons)
        btn_s = self.make_btn(4, frm_buttons)
        btn_sw = self.make_btn(5, frm_buttons)
        btn_w = self.make_btn(6, frm_buttons)
        btn_nw = self.make_btn(7, frm_buttons)

        btn_n.grid(column=1, row=1)
        btn_ne.grid(column=2, row=1)
        btn_e.grid(column=2, row=2)
        btn_se.grid(column=2, row=3)
        btn_s.grid(column=1, row=3)
        btn_sw.grid(column=0, row=3)
        btn_w.grid(column=0, row=2)
        btn_nw.grid(column=0, row=1)

        self.draw_new_random_circle()

    def make_btn(self, ring_type, master):
        if ring_type == 0:
            text = "↑"
        elif ring_type == 1:
            text = "↗"
        elif ring_type == 2:
            text = "→"
        elif ring_type == 3:
            text = "↘"
        elif ring_type == 4:
            text = "↓"
        elif ring_type == 5:
            text = "↙"
        elif ring_type == 6:
            text = "←"
        else:
            text = "↖"

        btn = tk.Button(master=master, text=text, font=("Arial", 50, 'bold'), bg='black', fg='white',
                  activebackground='darkgrey', image=self.btn_pixel, width=100, height=100, compound='center', padx=0,
                  pady=0)
        btn.bind("<Enter>", func=lambda event, a=btn: self.btn_hover_enter(a))
        btn.bind("<Leave>", func=lambda event, a=btn: self.btn_hover_leave(a))
        btn.bind("<Button-1>", func=lambda event, a=btn, b=ring_type: self.btn_press(a, b))
        return btn

    def btn_hover_enter(self, btn):
        btn.configure(bg='white')

    def btn_hover_leave(self, btn):
        btn.configure(bg='black')
        btn.configure(activebackground='darkgrey')

    def btn_press(self, btn, type):
        ring = self.ring_test.current_ring()
        if ring.hole_type == type:
            self.append_current_try_to_file(True)
            btn.configure(activebackground='green')
        else:
            self.append_current_try_to_file(False)
            btn.configure(activebackground='red')
        self.draw_new_random_circle()

    def create_circle(self, x, y, r, is_hole, line_width):
        x0 = x - r
        y0 = y - r
        x1 = x + r
        y1 = y + r
        if self.ring_test.is_black:
            bg_color = 'black'
            fg_color = 'white'
        else:
            bg_color = 'white'
            fg_color = 'black'
        if is_hole:
            outline = bg_color
            fill = bg_color
        else:
            outline = fg_color
            fill = ''
        self.canvas.create_oval(x0, y0, x1, y1, width=line_width, outline=outline, fill=fill)

    def draw_holey_ring(self, ring):
        self.create_circle(ring.center_position, ring.center_position, ring.circle_radius, False, ring.line_width)
        self.create_circle(ring.hole_position[0], ring.hole_position[1], ring.hole_radius, True, 1)

    def draw_new_random_circle(self):
        self.canvas.delete("all")
        self.canvas.update_idletasks()
        time.sleep(self.START_DELAY)
        if self.ring_test.next_ring():
            self.current_test_size.set(self.ring_test.current_ring().circle_radius)
            self.draw_holey_ring(self.ring_test.current_ring())
            self.canvas.update_idletasks()
            time.sleep(self.SECONDS_RING_IS_SHOWN)
            self.canvas.delete("all")
            self.canvas.update_idletasks()
        else:
            self.ring_test = None
            self.clear_test_frame()

    def append_current_try_to_file(self, is_success):
        f = open("log.csv", "a")
        ring = self.ring_test.current_ring()
        if self.ring_test.is_black:
            color = 'black'
        else:
            color = 'white'
        csv_string = "{},{},{},{},{}\n".format(self.ring_test.start_epoch, color, ring.circle_radius, ring.hole_type, is_success)
        f.write(csv_string)
        f.close()
