from tkinter import Tk,Button,Label,DoubleVar,Entry

window = Tk()
window.title("Simple tool Feet to Meter Converter App")
window.configure(background="light blue")
window.geometry("320x220")
window.resizable(width=False, height=False)


def convert():
    value = float(ft1e.get())
    meter = value * 0.3048
    ft1V.set("%.4f" % meter)

  


def clear():
    ft1V.set("")
    mt1V.set("")


ft1V = DoubleVar()
ft1e = Entry(window,textvariable=ft1V,width=14)
ft1e.grid(column=1,row=0)
ft1e.delete(0,'end')


ft1 = Label(window, text="Feet", bg="purple",fg="white",width=14)
ft1.grid(column=0, row=0,padx=15,pady=15)



mt1V = DoubleVar()
mt1e = Entry(window,textvariable=ft1V,width=14)
mt1e.grid(column=1,row=1,pady=30)
mt1e.delete(0,'end')

mtl = Label(window, text="Meter", bg="black",fg="white",width=14)
mtl.grid(column=0, row=1)

convBtn = Button(window,text="Convert" , bg="blue" , fg="white", width=14, command=convert)
convBtn.grid(column=0, row=3 , padx=15)

clearBtn = Button(window, text="Clear", bg="red", fg="white", width=14, command=clear)
clearBtn.grid(column=1, row=3 , padx=15)


window.mainloop()
