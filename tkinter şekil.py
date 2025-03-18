from tkinter import *
#Pencere oluşturma 
pencere = Tk()

#canvas tanımlanıyor
c = Canvas(pencere , width = 300, height = 150)
c.pack()

#Polygon çizdiriliyor
c.create_polygon(10,50,30,10,50,50,outline="green")

#Pencereyi sürekli açık tutmak
pencere.mainloop()