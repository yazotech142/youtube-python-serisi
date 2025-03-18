from tkinter import *
#Pencere oluşturma
pencere = Tk()

Label(pencere, text = "ilk metin", bg = "blue").grid(column=0, row = 
0)
Label(pencere, text = "ikinci metin",bg = "white").grid(column=1,
row = 0)
Label(pencere, text = "Son metin",bg = "yellow").grid(column=1, row=
1)
#Pencereyi sürekli açık tutmak
pencere.mainloop()