import math
import tkinter as tk
from tkinter import messagebox
from tkinter.ttk import *
from GalaxyMaker import GalaxyMaker,Star

class MainWindow(tk.Frame):
    def __init__(self,master=None):
        super().__init__(master)
        self.master = master
        # self.pack()
        self.galaxy_type = tk.IntVar()
        self.slider_alpha_value = tk.DoubleVar()
        self.slider_radius_value = tk.DoubleVar()
        self.create_widgets()
        self.canvas_center = (300,300)
    
    def create_widgets(self):

        self.radiobtn_ellipse_galaxy = tk.Radiobutton(self.master,text='Эллиптическая',value = 0,command = self.init_widgets_for_galaxies,variable = self.galaxy_type)
        self.radiobtn_ellipse_galaxy.grid(row = 0,column = 0)
        self.radiobtn_ellipse_galaxy.deselect()
        self.slider_for_radius = tk.Scale(self.master,variable = self.slider_radius_value,from_=0.1,to=1,resolution=0.1,orient = tk.HORIZONTAL,state = tk.DISABLED,label = 'Радиус',highlightcolor = 'green')
        self.slider_for_radius.grid(row = 1, column = 1)

        self.radiobtn_mindal_galaxy = tk.Radiobutton(self.master,text='Миндалевидная',value = 1,command = self.init_widgets_for_galaxies,variable = self.galaxy_type)
        self.radiobtn_mindal_galaxy.grid(row = 0,column = 1)
        self.radiobtn_mindal_galaxy.deselect()
        self.label_for_a = tk.Label(self.master,text = 'A [1-20]',state = tk.DISABLED)
        self.label_for_a.grid(row = 2,column = 0)
        self.label_for_b = tk.Label(self.master,text = 'B [1-20]',state = tk.DISABLED)
        self.label_for_b.grid(row = 3,column = 0)
        self.a_entry = tk.Entry(self.master,state = tk.DISABLED)
        self.a_entry.grid(row = 2,column = 1)
        self.b_entry = tk.Entry(self.master,state = tk.DISABLED)
        self.b_entry.grid(row = 3,column = 1)

        self.radiobtn_spiral_galaxy = tk.Radiobutton(self.master,text='Спиральная',value = 2,command = self.init_widgets_for_galaxies,variable = self.galaxy_type)
        self.radiobtn_spiral_galaxy.grid(row = 0,column = 2)
        self.radiobtn_spiral_galaxy.deselect()       
            
        self.slider_for_alpha = tk.Scale(self.master,variable = self.slider_alpha_value,from_=-3,to=3,resolution=0.2,orient = tk.HORIZONTAL,state = tk.DISABLED,label = 'Угол поворота')
        self.slider_for_alpha.grid(row = 4,column = 1)        
        self.label_for_arms = tk.Label(self.master,text = 'Количество рукавов [1-5]',state = tk.DISABLED)
        self.label_for_arms.grid(row = 5,column = 0)        
        self.arms_entry = tk.Entry(self.master,state = tk.DISABLED)
        self.arms_entry.grid(row = 5,column = 1)

        self.show_button = tk.Button(self.master,text = 'Нарисовать галактику',command = self.draw_stars)
        self.show_button.grid(row = 6,column = 0,columnspan = 3,pady = 10)
  
        self.galaxy_area = tk.Canvas(self.master,width = 600 ,height = 600,bg = 'black')
        self.galaxy_area.grid(row = 7,columnspan = 3)    

    def init_widgets_for_galaxies(self):
        if self.galaxy_type.get() == 0:
            self._reset_widgets()
            self.slider_for_radius['state'] = tk.NORMAL
        if self.galaxy_type.get() == 1:
            self._reset_widgets()
            self.label_for_a['state'] = tk.NORMAL
            self.label_for_b['state'] = tk.NORMAL
            self.a_entry['state'] = tk.NORMAL
            self.b_entry['state'] = tk.NORMAL          
        if self.galaxy_type.get() == 2:
            self._reset_widgets()
            self.slider_for_alpha['state'] = tk.NORMAL
            self.label_for_arms['state'] = tk.NORMAL
            self.arms_entry['state'] = tk.NORMAL

    def _reset_widgets(self):
        self.slider_for_radius['state'] = tk.DISABLED
        self.label_for_a['state'] = tk.DISABLED
        self.label_for_b['state'] = tk.DISABLED
        self.a_entry['state'] = tk.DISABLED
        self.b_entry['state'] = tk.DISABLED
        self.slider_for_alpha['state'] = tk.DISABLED
        self.label_for_arms['state'] = tk.DISABLED
        self.arms_entry['state'] = tk.DISABLED
        

    def _calculate_color_of_star(self,distance):
##        r = hex((255+distance%255)%255)
        r_value = int(int(self.galaxy_area['width'])/630*distance)%256
        r = hex(r_value)
        g = hex(0) 
        b = hex(255-r_value)
        return '#' + r[r.index('x')+1:].zfill(2) + g[g.index('x')+1:].zfill(2) + b[b.index('x')+1:].zfill(2)
##        return '#' + r[r.index('x')+1:][0] + g[g.index('x')+1:][0] + b[b.index('x')+1:][0]

    def _validate_values(self,galaxy_type):
        if galaxy_type == 1 :
            try:
                a = int(self.a_entry.get()) 
                b = int(self.b_entry.get())
                if a and b in range(1,21):
                    return True
                else : return False
            except ValueError:
                return False
        if galaxy_type == 2:
            try:
                if int(self.arms_entry.get()) in range(1,6):
                    return True
                else : return False    
            except ValueError:
                return False
   
    def draw_stars(self):
        try:
            if self.galaxy_type.get() == 0:
                stars = GalaxyMaker(600,600).make_ellipse_galaxy(self.slider_radius_value.get())   
            elif self.galaxy_type.get() == 1 and self._validate_values(self.galaxy_type.get()):                
                stars = GalaxyMaker(600,600).make_mindal_galaxy(int(self.a_entry.get()),int(self.b_entry.get()))        
            elif self.galaxy_type.get() == 2 and self._validate_values(self.galaxy_type.get()):
                stars = GalaxyMaker(600,600).make_spiral_galaxy(int(self.arms_entry.get()),self.slider_alpha_value.get())
            else:
                messagebox.showinfo('Error','Неверные данные')
                return
        except(tk.TclError):
            return
        self.galaxy_area.delete('all')
        center_x = int(self.galaxy_area['width'])/2
        center_y = int(self.galaxy_area['height'])/2
        for star in stars:
            distance_to_the_center = star.calculate_distance(self.canvas_center[0],self.canvas_center[1])
            color_string = self._calculate_color_of_star(distance_to_the_center)
            star_new_x = star.x + center_x
            star_new_y = star.y + center_y
            self.galaxy_area.create_line(star_new_x,star_new_y,star_new_x+1,star_new_y,fill=color_string)

        
if __name__ == "__main__":
    root = tk.Tk()
    root.geometry("600x800+200+50")
    root.title("Lab 1")
    root.resizable(False,False)
    app = MainWindow(master=root)
    app.mainloop()
