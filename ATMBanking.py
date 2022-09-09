import tkinter as tk
from tkinter.font import BOLD
from PIL import ImageTk, Image
import sqlite3
from imgop import *
class App(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        self.title('ATMBankingv0.1')
        self.geometry("720x720+0+0")
        self.resizable(False,False)

        container = tk.Frame(self)
        container.pack(side = "top", fill = "both", expand = True)
        container.grid_rowconfigure(0, weight = 1)
        container.grid_columnconfigure(0, weight = 1)

        self.frames = {}

        for F in (LoginPage, MainPage, PageActions):
            page_name = F.__name__
            frame = F(parent = container, controller = self)
            self.frames[page_name] = frame

            frame.grid(row=0, column = 0, sticky = "nsew")
        
        self.show_frame("MainPage")

    def show_frame(self, page_name):
        frame = self.frames[page_name]
        frame.tkraise()

class LoginPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        login_form = tk.Frame(self,width = 720, height = 640, bg = '#004d4d')
        login_form.pack(fill = "both", expand = True)
        please_text = tk.Label(login_form, text = "Please enter your login details", bg = "#004d4d", fg = "#b37700", font = ('Verdana', 12, BOLD))
        please_text.pack(pady = (80,10))
        fullname_label = tk.Label(login_form, text = "Full Name:", bg = "#004d4d", fg = "#b37700", font = ('Verdana', 15, BOLD))
        fullname_label.pack(pady = (100,5))
        name_entry = tk.Entry(login_form, width = 20, font = ('Verdana', 12, BOLD), bd = 1)
        name_entry.pack()
        pin_label = tk.Label(login_form, text = "PIN:", bg = "#004d4d", fg = "#b37700", font = ('Verdana', 15 , BOLD))
        pin_label.pack(pady = (40,5))
        pin_entry = tk.Entry(login_form, width = 20, font = ('Verdana', 12, BOLD), bd = 1)
        pin_entry.pack()
        button_login = tk.Button(login_form, cursor = 'hand2', text = "LOGIN", width = 10, height = 3, font = ('Helvetica', 12, BOLD), command = lambda:self.check_login(name_entry.get(), pin_entry.get()),bg = "#004d4d", fg = '#b37700')
        button_login.pack(pady = (40,5))
        bottom_frame = tk.Frame(self, width = 720, height = 30, bg = "#004d4d")
        bottom_frame.pack(fill = 'both')
        bottom_text = tk.Label(bottom_frame, text = "ATMBanking v0.1", bg = "#004d4d", fg = "#a6a6a6", font = ('Verdana', 6, BOLD))
        bottom_text.pack( side = tk.RIGHT)
    
    def check_login(self, name, id):
        connection = sqlite3.connect('data/costumers.db')
        cursor = connection.cursor()
        costumers_name = []
        pins = []
        for costumer in cursor.execute('select fullname from costumers'):
            costumers_name.append(costumer)
        for pin in cursor.execute('select pin from costumers'):
            pins.append(pin)
        for costumer in costumers_name:
            if costumer[0] == name:
                pin_id = costumers_name.index(costumer)
                if pins[pin_id][0] == int(id):
                    self.controller.show_frame('MainPage')
                    pins.clear()
                    costumers_name.clear()
                else:
                    wrong_pin = tk.Label(self, text = "Your PIN is wrong!", font = ('Helvetica', 12, BOLD),bg = "#004d4d", fg = "darkred")
                    wrong_pin.pack(fill = 'both')
                    wrong_pin.after(1000, lambda:wrong_pin.pack_forget())

class MainPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.configure(bg = "black")
        main_frame = tk.Frame(self, bg = "#004d4d")
        main_frame.pack(fill = "both", expand = True)
        text_frame = tk.Frame(main_frame, bg = "#004d4d")
        top_text = tk.Label(text_frame, text = "Please choose a option bellow:", bg = "#004d4d", fg = "white", font = ('Verdana', 16, BOLD))
        top_text.pack(pady = 30)
        text_frame.pack(fill = 'x')
        balance_img = BImage()
        buttons_frame = tk.Frame(main_frame, bg = "#004d4d")
        balance_btn = tk.Button(buttons_frame, text = 'BALANCE', image = balance_img, compound = tk.LEFT, bg = "#0e5c5c", font = ('Bebas NEUE', 20), width = 250, height = 90, cursor = 'hand2')
        balance_btn.image = balance_img
        balance_btn.grid(row = 0, column = 0, sticky = tk.W, padx = 10, pady = (60,40))
        deposit_img = DImage()
        deposit_btn = tk.Button(buttons_frame, text = "DEPOSIT", font = ('Bebas NEUE', 20), image = deposit_img, compound = tk.LEFT, width = 250, height = 90, cursor = 'hand2')
        deposit_btn.image = deposit_img
        deposit_btn.grid(row = 1, column = 0, sticky = tk.W, padx = 10, pady = 40)
        withdraw_img = WImage()
        withdraw_btn = tk.Button(buttons_frame, text = "WITHDRAW", image = withdraw_img, compound = tk.LEFT, font = ('Bebas NEUE', 20), width = 250, height = 90, cursor = 'hand2')
        withdraw_btn.image = withdraw_img
        withdraw_btn.grid(row = 2, column = 0, sticky = tk.W, padx = 10, pady = 40)
        transfer_img = TImage()
        transfer_btn = tk.Button(buttons_frame, text = "TRANSFER", image = transfer_img, compound = tk.LEFT, font = ('Bebas NEUE', 20), width = 250, height = 90, cursor = 'hand2')
        transfer_btn.image = transfer_img
        transfer_btn.grid(row = 0, column = 1, sticky = tk.E, padx = 10, pady = (60,40))
        changepin_img = CPImage()
        changepin_btn = tk.Button(buttons_frame, text = "CHANEGE PIN", image = changepin_img, compound = tk.LEFT, font = ('Bebas NEUE', 20), width = 250, height = 90, cursor = 'hand2')
        changepin_btn.image = changepin_img
        changepin_btn.grid(row = 1, column = 1, sticky = tk.E, padx = 10, pady = 40)
        exit_img = EImage()
        exit_btn = tk.Button(buttons_frame, text = "EXIT", image = exit_img, compound = tk.LEFT, font = ('Bebas NEUE', 20), width = 250, height = 90, cursor = 'hand2')
        exit_btn.image = exit_img
        exit_btn.grid(row = 2, column = 1, sticky = tk.E, padx = 10, pady = 40)
        version_text = tk.Label(buttons_frame, text = "ATMBanking v0.1", bg = "#004d4d", fg = "#a6a6a6", font = ('Verdana', 6, BOLD))
        version_text.grid(row = 3, column = 1, sticky = tk.SE, pady= (60,0))
        buttons_frame.pack(fill = 'both')
        buttons_frame.grid_columnconfigure(0, weight = 1)
        buttons_frame.grid_columnconfigure(1, weight = 1)
        buttons_frame.grid_rowconfigure(3, weight = 1)



class PageActions(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller


if __name__ == "__main__":
    app = App()
    app.mainloop()