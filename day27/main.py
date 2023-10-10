from tkinter import *

window = Tk()
window.title("My first GUI program")
window.minsize(width=500, height=300)
window.config(padx=100, pady=200)

#Label

my_label = Label(text="I am a Label", font=("Arial", 24, "bold"))
# my_label.pack()
# my_label.place(x=100, y=0)
my_label.grid(column=0, row=0)

#Button

def button_clicked():
    print("I got cliccked")
    new_text = input.get()
    my_label.config(text=new_text)

button = Button(text='Click Me', command=button_clicked)
# button.pack()
button.grid(column=1, row=1)

new_button = Button(text='Click Me 2', command=button_clicked)
new_button.grid(column=2, row=0)

#Entry

input = Entry(width=10)

input.grid(column=3, row=2)







window.mainloop()