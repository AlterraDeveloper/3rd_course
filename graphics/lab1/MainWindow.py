import tkinter as tk
from tkinter.ttk import *
from PIL import ImageTk,Image
from GalaxyMaker import GalaxyMaker,Star

class MainWindow(tk.Frame):
    def __init__(self,master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_widgets()
    
    def create_widgets(self):
        self.galaxy_radiobtn_group = list()
        self.galaxy_radiobtn_group.append(tk.Radiobutton(self.master,text='Эллиптическая',value = 0).pack(side=tk.TOP))
        self.galaxy_radiobtn_group .append(tk.Radiobutton(self.master,text='Миндалевидная',value = 1).pack(side=tk.TOP))
        self.galaxy_radiobtn_group .append(tk.Radiobutton(self.master,text='Спиральная',value = 2).pack(side=tk.TOP))

        self.galaxy_area = tk.Canvas(self.master,width = 600 ,height = 600,bg = 'black')
        self.galaxy_area.pack()
        img = Image.open(r"/home/altersoft/alterra/3_rd/3rd_course/graphics/lab1/space_bg.jpg")
        bg_image = ImageTk.PhotoImage(img)
        self.galaxy_area.create_image(0,0,image = bg_image)

        
   
    def do_smth(self):
        stars = GalaxyMaker(600,600).make_spiral_galaxy(3,2)
        for star in stars:
            self.galaxy_area.create_line(star.x,star.y,star.x+1,star.y,fill='red')

        
if __name__ == "__main__":
    root = tk.Tk()
    root.geometry("600x600+200+100")
    root.title("Lab 1")
    root.resizable(False,False)
    app = MainWindow(master=root)
    app.do_smth()
    app.mainloop()