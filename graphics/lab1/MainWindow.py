import math
import tkinter as tk
from tkinter.ttk import *
#from PIL import ImageTk,Image
from GalaxyMaker import GalaxyMaker,Star

class MainWindow(tk.Frame):
    def __init__(self,master=None):
        super().__init__(master)
        self.master = master
        # self.pack()
        self.galaxy_type = tk.IntVar()
        self.slider_value = tk.DoubleVar()
        self.create_widgets()
        self.canvas_center = (300,300)
    
    def create_widgets(self):
        self.radiobtn_ellipse_galaxy = tk.Radiobutton(self.master,text='Эллиптическая',value = 0,command = self.init_widgets_for_spiral,variable = self.galaxy_type)
        self.radiobtn_ellipse_galaxy.grid(row = 0,column = 0)
        self.radiobtn_ellipse_galaxy.deselect()

        self.radiobtn_mindal_galaxy = tk.Radiobutton(self.master,text='Миндалевидная',value = 1,command = self.draw_stars,variable = self.galaxy_type)
        self.radiobtn_mindal_galaxy.grid(row = 0,column = 1)
        self.radiobtn_mindal_galaxy.deselect()
 
        self.radiobtn_spiral_galaxy = tk.Radiobutton(self.master,text='Спиральная',value = 2,command = self.draw_stars,variable = self.galaxy_type)
        self.radiobtn_spiral_galaxy.grid(row = 0,column = 2)
        self.radiobtn_spiral_galaxy.deselect()

        self.show_button = tk.Button(self.master,text = 'Show galaxy')
        self.show_button.grid(row = 1,column = 0,columnspan = 3)
  
        self.galaxy_area = tk.Canvas(self.master,width = 600 ,height = 600,bg = 'black')
        self.galaxy_area.grid(row = 4,columnspan = 3)

    

    def init_widgets_for_spiral(self):
        self.slider = tk.Scale(self.master,variable = self.slider_value,from_=-3,to=3,resolution=0.25)
        self.slider.grid(row = 2,columnspan = 3)

    def calculate_color_of_star(self,distance):
        r = hex((255+distance%255)%255) 
        g = hex(0) 
        b = hex(255 - distance%255)
        return '#' + r[r.index('x')+1:][0] + g[g.index('x')+1:][0] + b[b.index('x')+1:][0]

   
    def draw_stars(self):
        self.galaxy_area.delete('all')
        if self.galaxy_type.get() == 0:
            stars = GalaxyMaker(600,600).make_ellipse_galaxy()   
        if self.galaxy_type.get() == 1:
            stars = GalaxyMaker(600,600).make_mindal_galaxy()        
        if self.galaxy_type.get() == 2:
            stars = GalaxyMaker(600,600).make_spiral_galaxy(3,-0.75)           
        for star in stars:
            distance_to_the_center = star.calculate_distance(self.canvas_center[0],self.canvas_center[1])
            color_string = self.calculate_color_of_star(distance_to_the_center)
            self.galaxy_area.create_line(star.x,star.y,star.x+1,star.y,fill=color_string)

        
if __name__ == "__main__":
    root = tk.Tk()
    root.geometry("600x650+200+50")
    root.title("Lab 1")
    root.resizable(False,False)
    app = MainWindow(master=root)
    app.mainloop()
