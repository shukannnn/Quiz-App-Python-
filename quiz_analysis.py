from tkinter import *
from cProfile import label
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, NavigationToolbar2Tk)
import numpy as np

class QuizAnalysis:
    def display_analysis(self):
        self.window = Tk()
        self.window.title('Previous Performance Analysis')
        self.window.geometry("1050x530")
        # self.display_title()
        self.plot()

    def plot(self):
        fig = Figure(figsize = (5, 5),dpi = 100)

        y=[]

        with open("data.txt") as x :
            content = x.read().splitlines()
        for i in range(len(content)-1):
            if content[i+1]==content[len(content)-1]:
                y.append(int(content[i]))

        x=np.arange(1,len(y)+1)
        print(content)
        print(y)      
  
        # adding the subplot
        plot1 = fig.add_subplot(111)
    
        # plotting the graph
        plot1.plot(x,y,color='b',marker='o')
    
        # creating the Tkinter canvas
        # containing the Matplotlib figure
        canvas = FigureCanvasTkAgg(fig,
                                master = self.window)  
        canvas.draw()
    
        # placing the canvas on the Tkinter window
        canvas.get_tk_widget().pack()
    
        # creating the Matplotlib toolbar
        toolbar = NavigationToolbar2Tk(canvas,
                                    self.window)
        toolbar.update()
    
        # placing the toolbar on the Tkinter window
        canvas.get_tk_widget().pack()



