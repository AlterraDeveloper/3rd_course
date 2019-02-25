import tkinter as tk
from tkinter.ttk import *
from PIL import ImageTk,Image
from GalaxyMaker import Star,GalaxyMaker 

class MainWindow(tk.Frame):
    def __init__(self,master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_widgets()
    
    def create_widgets(self):
        self.galaxy_radiobtn_group = list()
        self.galaxy_radiobtn_group .append(tk.Radiobutton(self.master,text='Эллиптическая',value = 0).pack(side=tk.TOP))
        self.galaxy_radiobtn_group .append(tk.Radiobutton(self.master,text='Миндалевидная',value = 1).pack(side=tk.TOP))
        self.galaxy_radiobtn_group .append(tk.Radiobutton(self.master,text='Спиральная',value = 2).pack(side=tk.TOP))

        drawing_area = tk.Canvas(self.master,width = 400,height = 400,bg = 'black')
        drawing_area.pack(expand=tk.YES,fill = tk.BOTH)
        image = Image.open("D:/3_year/3rd_course/graphics/lab1/galaxy.png")
        background_img = ImageTk.PhotoImage(image)
        drawing_area.create_image(10,10,image = background_img,anchor = tk.NW)
        # refresh_button = tk.Button(self.master,text = "Обновить", image = tk.PhotoImage("refresh_icon.jpg"),command = self.do_smth)
        # refresh_button.pack(side = tk.LEFT)
   
    def do_smth(self):
        print("click!")
        
if __name__ == "__main__":
    root = tk.Tk()
    root.geometry("600x600+100+100")
    root.title("Lab 1")
    root.resizable(False,False)
    app = MainWindow(master=root)
    app.mainloop()