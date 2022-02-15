import tkinter as tk


def main():
    window = tk.Tk()
    window.title('The Lord of the Holey Rings')
    frm_test = tk.Frame(master=window, width=900, height=900, bg='darkgrey', borderwidth=2, relief='sunken')

    frm_controls = tk.Frame(master=window, width=900, height=900, bg='darkgrey', borderwidth=2, relief='sunken')

    frm_test.pack(fill=tk.Y, side=tk.LEFT)
    frm_controls.pack(fill=tk.Y, side=tk.RIGHT)

    window.mainloop()
