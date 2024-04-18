
from tkinter import *
from tkinter import DISABLED, NORMAL
import threading
import time

class FraiseClicker:


    def __init__(self):
        self.window = Tk()
        self.window.title("FruitClicker")
        self.window.geometry("1080x720")
        self.window.minsize(720, 480)
        self.window.config(background='white')
        self.frame = Frame(self.window, bg='white')
        self.frame.pack(expand=True)
        self.item_value = IntVar()
        self.item_value.set(100)
        self.click_count = 0
        self.item_price = IntVar()
        self.item_price.set(100)
        self.click_value = 1
        self.auto_clicker_running = False 
        self.auto_clicker_price = IntVar()
        self.auto_clicker_price.set(250)
        self.create_widgets()
        

    def create_widgets(self):
        self.create_title()
        self.create_fruit_button()
        self.create_click_counter()
        self.create_price_counter()
        self.create_shop()
        self.create_auto_clicker_price_counter()
        self.create_auto_clicker_button()
        
        
    def create_title(self):
        label_title = Label(self.frame, text="Bienvenue sur FraiseClicker", 
                            font=("Courrier", 40), bg = 'white', fg='black')
        label_title.pack()


    def create_auto_clicker_price_counter(self):
        self.auto_clicker_price_label = Label(self.frame, text=f"Prix : {self.auto_clicker_price.get()}", font=("Courrier", 20), bg='#FF0000', fg='white')
        self.auto_clicker_price_label.pack(side=LEFT)
        
    def update_auto_clicker_price_counter(self):
        self.auto_clicker_price_label.config(text=f"Prix : {self.auto_clicker_price.get()}")
        
        
    def create_fruit_button(self):
        self.image = PhotoImage(file="/home/florentin/Documents/Python/FraiseClicker/fraise.png")
        button = Button(self.frame, image=self.image, command=self.increment_click_count, 
                        borderwidth = 0, bg = 'white', highlightthickness=0, relief='flat', activebackground='white')
        button.pack(expand=True)


    def increment_click_count(self):
        self.click_count += self.click_value
        self.update_click_counter()
        self.update_shop_button_state()
            
        
    def create_click_counter(self):
        self.click_counter_label = Label(self.frame, text="Clics : 0", font=("Courrier", 20), bg='#FF0000', fg='white')
        self.click_counter_label.pack()
    
    
    def update_click_counter(self):
        self.click_counter_label.config(text=f"Clics : {format(self.click_count, '.0f')}")
        
    
    def create_shop(self):
        self.shop_button = Button(self.frame, text="Acheter un ClickBonus", command=self.buy_item, 
                                  font=("Courrier", 15), bg='#41B77F', fg='white')
        if self.click_count < 100:
            self.shop_button.config(state=DISABLED)
        self.shop_button.pack(side=LEFT)
        
        
    def buy_item(self):
    
        if self.click_count >= self.item_price.get():
            self.item_value.set(self.item_value.get() + 1)
            self.click_value *= 1.5
            self.click_count -= self.item_price.get()
            self.update_click_counter()

        self.item_price.set(self.item_price.get() * 1.5)
        self.update_price_counter()    
        
        if self.click_count < self.item_price.get():
            print("> Desactive boutton because no money")
            self.shop_button.config(state=DISABLED)



    def create_price_counter(self):
        self.price_counter_label = Label(self.frame, text=f"Prix : {self.item_price.get()}", 
                                         font=("Courrier", 20), bg ='#FF0000', fg='white')
        self.price_counter_label.pack(side=LEFT)
        
        
    def update_price_counter(self):
        self.price_counter_label.config(text=f"Prix : {self.item_price.get()}")
        
        
    def update_shop_button_state(self):
        if self.click_count < self.item_price.get():
            self.shop_button.config(state=DISABLED)
        else:
            self.shop_button.config(state=NORMAL)
            
        auto_clicker_price = self.auto_clicker_price.get()
        if self.click_count < auto_clicker_price:
            self.auto_clicker_button.config(state=DISABLED)
        else:
            self.auto_clicker_button.config(state=NORMAL)
            

            
    def create_auto_clicker_button(self):
        self.auto_clicker_button = Button(self.frame, text="Acheter un AutoClicker", command=self.buy_auto_clicker, 
                                          font=("Courrier", 15), bg='#41B77F', fg='white')
        self.auto_clicker_button.pack(side=RIGHT)   
                
    def start_auto_clicker_thread(self):
        self.auto_clicker_thread = threading.Thread(target=self.auto_clicker_loop)
        self.auto_clicker_thread.start()
    
    def buy_auto_clicker(self):
        auto_clicker_price = self.auto_clicker_price.get()
        if self.click_count >= auto_clicker_price:
            self.click_count -= auto_clicker_price
            self.update_click_counter()
            self.auto_clicker_running = True
            self.start_auto_clicker_thread() 
            self.auto_clicker_price.set(auto_clicker_price * 1.5)
            self.update_auto_clicker_price_counter()
        else:
            print("Pas assez de clics pour acheter l'auto clicker")
        
    def auto_clicker_loop(self):
        if self.auto_clicker_running:
            self.click_count += 1.15
            self.update_click_counter()
            self.update_shop_button_state()
            self.window.after(300, self.auto_clicker_loop)
        
        
# afficher
app = FraiseClicker()
app.window.mainloop()
