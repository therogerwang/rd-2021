from tkinter import *
import backend.main as bm

class MyWindow:
    def __init__(self, win):
        self.lbl1 = Label(win, text='Business Name')
        self.t1 = Entry()
        self.t2 = Entry()
        self.btn1 = Button(win, text='Give me some recommendations', command=self.recommend)
        self.lbl1.place(x=100, y=50)
        self.t1.place(x=200, y=50)
        self.btn1.place(x=200, y=75)
        self.t2.place(x=200, y=100)

    def recommend(self):
        business_name = self.t1.get()
        result = bm.recommend(business_name)
        self.t2.insert(index=END, string=result)




window = Tk()
my_win = MyWindow(window)
window.title('<INSERT TITLE HERE>')
window.geometry("400x300+10+10")
window.mainloop()