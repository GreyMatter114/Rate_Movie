import pickle
import tkinter as tk
from tkinter import messagebox  
with open('model','rb') as f:
	regr=pickle.load(f)
window =tk.Tk()
window.title('Movie Rating')
window.geometry("360x360")
li=[]
e1 = tk.Entry(window)
e2 = tk.Entry(window)
e3 = tk.Entry(window)
e4 = tk.Entry(window)
e5 = tk.Entry(window)
tk.Label(window, text="Script").pack()
e1.pack()
tk.Label(window, text="Technique").pack()
e2.pack()
tk.Label(window, text="VFX").pack()
e3.pack()
tk.Label(window, text="Direction").pack()
e4.pack()
tk.Label(window, text="Acting").pack()
e5.pack()

def btn_click():
	li.append(int(e1.get()))
	li.append(int(e2.get()))
	li.append(int(e3.get()))
	li.append(int(e4.get()))
	li.append(int(e5.get()))
	predictedrate = regr.predict([li])
	messagebox.showinfo("Overall Rating",f'Overall Rating:{str(round(predictedrate[0][0]))}')
	li.clear()

btn1 = tk.Button(
        window,
        text="Predict",
        font=("Lucida Console", 20),
        width=15,
        bg="#ade5f1",
        command=btn_click)
btn1.pack()
window.resizable(False, False)
window.mainloop()