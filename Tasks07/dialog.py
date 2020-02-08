from tkinter import *
from tkinter import messagebox
import os


# https://effbot.org/tkinterbook/tkinter-dialog-windows.htm
class Dialog(Toplevel):
    def __init__(self, parent, title=None, **kwargs):
        Toplevel.__init__(self, parent)
        self.transient(parent)
        self.parent = parent
        if title:
            self.title(title)

        self.box = None
        body_frame = Frame(self)
        self.initial_focus = self.initialize(body_frame, **kwargs)
        body_frame.pack(padx=5, pady=5)
        self.values = []

        if not self.initial_focus:
            self.initial_focus = self

        self.buttonbox()
        self.grab_set()
        self.protocol("WM_DELETE_WINDOW", self.cancel)
        self.geometry("+%d+%d" % (parent.winfo_rootx()+50,
                                  parent.winfo_rooty()+50))
        self.initial_focus.focus_set()
        self.wait_window(self)

    def initialize(self, frame):
        return self

    def buttonbox(self):
        self.box = Frame(self)

        ok_btn = Button(self.box, text="OK", width=10,
                        command=self.ok, default=ACTIVE)
        ok_btn.pack(side=LEFT, padx=5, pady=5)
        cancel_btn = Button(self.box, text="Cancel",
                            width=10, command=self.cancel)
        cancel_btn.pack(side=LEFT, padx=5, pady=5)

        self.bind("<Return>", self.ok)
        self.bind("<Escape>", self.cancel)

        self.box.pack()

    def ok(self, event=None):
        if not self.validate():
            self.initial_focus.focus_set()
            return

        self.withdraw()
        self.update_idletasks()
        self.apply()
        self.cancel()

    def cancel(self, event=None):
        self.parent.focus_set()
        self.destroy()

    def validate(self):
        return True

    def apply(self):
        pass
