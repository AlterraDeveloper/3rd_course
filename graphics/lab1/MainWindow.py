import math
import tkinter as tk
from tkinter import messagebox
from tkinter.ttk import *
from GalaxyMaker import GalaxyMaker,Star
from EllipseGalaxy import EllipseGalaxy
from MindalGalaxy import MindalGalaxy
from SpiralGalaxy import SpiralGalaxy

ELLIPSE_GALAXY_ID = 0
MINDAL_GALAXY_ID = 1
SPIRAL_GALAXY_ID = 2

class MainWindow(tk.Frame):
    def __init__(self,master=None):
        super().__init__(master)
        self.master = master
        self.galaxy_type = tk.IntVar()
        self.slider_alpha_value = tk.DoubleVar()
        self.slider_radius_value = tk.DoubleVar()
        self.create_widgets()
    
    def create_widgets(self):

        self.radiobtn_ellipse_galaxy = tk.Radiobutton(self.master,text='Эллиптическая',value =ELLIPSE_GALAXY_ID ,command = self.init_widgets_for_galaxies,variable = self.galaxy_type)
        self.radiobtn_ellipse_galaxy.grid(row = 0,column = 0)
        self.radiobtn_ellipse_galaxy.deselect()
        self.slider_for_radius = tk.Scale(self.master,variable = self.slider_radius_value,from_=0.1,to=1,resolution=0.1,orient = tk.HORIZONTAL,state = tk.DISABLED,label = 'Радиус')
        
        self.radiobtn_mindal_galaxy = tk.Radiobutton(self.master,text='Миндалевидная',value = MINDAL_GALAXY_ID,command = self.init_widgets_for_galaxies,variable = self.galaxy_type)
        self.radiobtn_mindal_galaxy.grid(row = 0,column = 1)
        self.radiobtn_mindal_galaxy.deselect()
        self.label_for_a = tk.Label(self.master,text = 'A [1-20]',state = tk.DISABLED)
        self.label_for_b = tk.Label(self.master,text = 'B [1-20]',state = tk.DISABLED)
        self.a_entry = tk.Entry(self.master,state = tk.DISABLED)
        self.b_entry = tk.Entry(self.master,state = tk.DISABLED)
        
        self.radiobtn_spiral_galaxy = tk.Radiobutton(self.master,text='Спиральная',value = SPIRAL_GALAXY_ID,command = self.init_widgets_for_galaxies,variable = self.galaxy_type)
        self.radiobtn_spiral_galaxy.grid(row = 0,column = 2)
        self.radiobtn_spiral_galaxy.deselect()       
            
        self.slider_for_alpha = tk.Scale(self.master,variable = self.slider_alpha_value,from_=-3,to=3,resolution=0.2,orient = tk.HORIZONTAL,state = tk.DISABLED,label = 'Угол поворота')
        self.label_for_arms = tk.Label(self.master,text = 'Количество рукавов [1-5]',state = tk.DISABLED)
        self.arms_entry = tk.Entry(self.master,state = tk.DISABLED)

        self.show_button = tk.Button(self.master,text = 'Нарисовать галактику',command = self.draw_stars)
        self.show_button.grid(row = 3,column = 0,columnspan = 3,pady = 10)
  
        self.galaxy_area = tk.Canvas(self.master,width = 600 ,height = 600,bg = 'black')
        self.galaxy_area.grid(row = 4,columnspan = 3)    

    def init_widgets_for_galaxies(self):
        if self.galaxy_type.get() == ELLIPSE_GALAXY_ID:
            
            self._disable_widgets()
            self._hide_widgets()
            
            self.slider_for_radius['state'] = tk.NORMAL
            self.slider_for_radius.grid(row = 1,column = 1)

        if self.galaxy_type.get() == MINDAL_GALAXY_ID:
            
            self._disable_widgets()
            self._hide_widgets()

            self.label_for_a['state'] = tk.NORMAL
            self.label_for_b['state'] = tk.NORMAL
            self.a_entry['state'] = tk.NORMAL
            self.b_entry['state'] = tk.NORMAL

            self.label_for_a.grid(row = 1,column = 0)
            self.label_for_b.grid(row = 2,column = 0)
            self.a_entry.grid(row = 1,column = 1)
            self.b_entry.grid(row = 2,column = 1)

        if self.galaxy_type.get() == SPIRAL_GALAXY_ID:

            self._disable_widgets()
            self._hide_widgets()
            
            self.slider_for_alpha['state'] = tk.NORMAL
            self.label_for_arms['state'] = tk.NORMAL
            self.arms_entry['state'] = tk.NORMAL

            self.slider_for_alpha.grid(row = 1,column = 1)
            self.label_for_arms.grid(row = 2,column = 0)
            self.arms_entry.grid(row = 2,column = 1)
    def _disable_widgets(self):
        self.slider_for_radius['state'] = tk.DISABLED
        self.label_for_a['state'] = tk.DISABLED
        self.label_for_b['state'] = tk.DISABLED
        self.a_entry['state'] = tk.DISABLED
        self.b_entry['state'] = tk.DISABLED
        self.slider_for_alpha['state'] = tk.DISABLED
        self.label_for_arms['state'] = tk.DISABLED
        self.arms_entry['state'] = tk.DISABLED

    def _hide_widgets(self):
        if self.galaxy_type.get() == ELLIPSE_GALAXY_ID:
            # widgets for mindal galaxy 
            self.label_for_a.grid_forget()
            self.label_for_b.grid_forget()
            self.a_entry.grid_forget()
            self.b_entry.grid_forget()
            ###########################

            # widgets for spiral galaxy
            self.slider_for_alpha.grid_forget()
            self.label_for_arms.grid_forget()
            self.arms_entry.grid_forget()
            ###########################

        if self.galaxy_type.get() == MINDAL_GALAXY_ID:
            # widgets for ellipse galaxy 
            self.slider_for_radius.grid_forget()
            ###########################
            self.slider_for_alpha.grid_forget()
            self.label_for_arms.grid_forget()
            self.arms_entry.grid_forget()

        if self.galaxy_type.get() == SPIRAL_GALAXY_ID:
            # widgets for ellipse galaxy
            self.slider_for_radius.grid_forget()
            ###########################

            # widgets for mindal galaxy
            self.label_for_a.grid_forget()
            self.label_for_b.grid_forget()
            self.a_entry.grid_forget()
            self.b_entry.grid_remove()
            ###########################
        

    def _calculate_color_of_star(self,distance):
        r_value = int(int(self.galaxy_area['width'])/630*distance)%256
        r = hex(r_value)
        g = hex(0) 
        b = hex(255-r_value)
        return '#' + r[r.index('x')+1:].zfill(2) + g[g.index('x')+1:].zfill(2) + b[b.index('x')+1:].zfill(2)

    def _reset_widgets(self,*widgets):
        if widgets:
            for widget in widgets:
                widget.delete(0,'end') 

    def _validate_values(self,galaxy_type):
        if galaxy_type == MINDAL_GALAXY_ID :
            try:
                a = int(self.a_entry.get()) 
                b = int(self.b_entry.get())
                if a and b in range(1,21):
                    return True
                else : return False
            except ValueError:return False
        if galaxy_type == SPIRAL_GALAXY_ID:
            try:
                if int(self.arms_entry.get()) in range(1,6):
                    return True
                else : return False    
            except ValueError: return False
   
    def draw_stars(self):
        canvas_width  = int(self.galaxy_area['width'])
        canvas_height = int(self.galaxy_area['height'])
        canvas_center_x = canvas_width/2
        canvas_center_y = canvas_height/2
        try:
            if self.galaxy_type.get() == ELLIPSE_GALAXY_ID:
                stars = EllipseGalaxy(canvas_width,canvas_height,self.slider_radius_value.get()).make()   
            elif self.galaxy_type.get() == MINDAL_GALAXY_ID and self._validate_values(self.galaxy_type.get()):
                stars = MindalGalaxy(canvas_width,canvas_height,int(self.a_entry.get()),int(self.b_entry.get())).make()                        
            elif self.galaxy_type.get() == SPIRAL_GALAXY_ID and self._validate_values(self.galaxy_type.get()):
                stars = SpiralGalaxy(canvas_width,canvas_height,int(self.arms_entry.get()),self.slider_alpha_value.get()).make()
            else:
                messagebox.showinfo('Error','Неверные данные')
                self._reset_widgets(self.arms_entry,self.a_entry,self.b_entry) 
                return
        except(tk.TclError):
            return
        self.galaxy_area.delete('all')
        for star in stars:
            distance_to_the_center = star.calculate_distance(canvas_center_x,canvas_center_y)
            color_string = self._calculate_color_of_star(distance_to_the_center)
            star_new_x = star.x + canvas_center_x
            star_new_y = star.y + canvas_center_y
            self.galaxy_area.create_line(star_new_x,star_new_y,star_new_x+1,star_new_y,fill=color_string)

        
if __name__ == "__main__":
    root = tk.Tk()
    root.geometry("600x700+200+50")
    root.title("Lab 1")
    root.resizable(False,False)
    app = MainWindow(master=root)
    app.mainloop()
