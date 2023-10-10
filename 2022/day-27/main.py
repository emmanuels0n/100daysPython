# import tkinter
from tkinter import *  # This imports al classes immediately and saves some typing


# Button
def button_clicked():  # Event listener
    print("I got clicked")
    new_text = entry.get()  # Gets the entry
    my_label.config(text=new_text)


# window = tkinter.Tk()
window = Tk()  # no need for the tkinter. part
window.title("My first GUI program")
window.minsize(width=500, height=300)
window.config(padx=20, pady=20)  # add padding

# Label
my_label = Label(text="I'm a label", font=("Arial", 24, "italic"))
my_label["text"] = "New Text"  # I can change it as it was a dictionary
my_label.config(text="New Text")  # or like this
# my_label.pack(side="top")  # "The packer": To disp our label on the window # There are default arguments that come
# already integrated into the function, to chance them I have to call them
# my_label.place(x=100, y=100)  # Another mode of specify the layout
my_label.grid(column=0, row=0) # a grid from upper left corner
my_label.config(pady=50, padx=50)

#Button
button = Button(text="Click me",
                command=button_clicked)  # for command, I used the name of the function without actually calling it
# button.pack()
button.grid(column=1, row=1)

button2 = Button(text="Clik on me2")
button2.grid(column=2, row=0)



# Entry
entry = Entry(width=10)
entry.get()  # To obtain the text in the entry
# entry.pack()
entry.grid(column=3, row=2)

window.mainloop()
