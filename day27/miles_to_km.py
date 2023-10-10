from tkinter import *


window = Tk()
window.title("Mile to km converter")
#window.minsize(width=500, height=300)
window.config(padx=50, pady=50)

#Entry

input = Entry(width=10)
input.grid(column=1, row=0)

miles_label = Label(text="miles", font=("Arial", 15))
miles_label.grid(column=2, row=0)

#Labels

is_equal = Label(text="is equal to", font=("Arial", 15))
is_equal.grid(column=0, row=1)

kms = Label(text="0", font=("Arial", 15, "bold"))
kms.grid(column=1, row=1)
kms.config(padx=15, pady=15)

kms_label = Label(text="km", font=("Arial", 15))
kms_label.grid(column=2, row=1)

#Button

def button_clicked():    
    miles = float(input.get())
    km = miles * 1.60934
    kms.config(text=f"{km}")


button = Button(text='Calculate', command=button_clicked)
# button.pack()
button.grid(column=1, row=2)


window.mainloop()