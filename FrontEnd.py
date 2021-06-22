from tkinter import *
import backend
import pandas
window = Tk()

window.wm_title("Books")

def get_selected_row(event):
                    #if list1.size() ==0:       # found a better solution to the bug
                    #   return
    try:
        global selected_tuple
        index=list1.curselection()[0]
        selected_tuple=list1.get(index)
        e1.delete(0, END)
        e1.insert(END, selected_tuple[1])
        e2.delete(0, END)
        e2.insert(END, selected_tuple[2])
        e3.delete(0, END)
        e3.insert(END, selected_tuple[3])
        e4.delete(0, END)
        e4.insert(END, selected_tuple[4])
    except IndexError:
        pass


def view_back():
    list1.delete(0, END)
    for row in backend.view():
        list1.insert(END, row)

def search_back():
    list1.delete(0, END)
    for row in backend.search(title_value.get(), author_value.get(), year_value.get(), isbn_value.get()):
        list1.insert(END, row)

def add_back():
    backend.add_entry(title_value.get(), author_value.get(), year_value.get(), isbn_value.get())
    list1.delete(0, END)
    list1.insert(END, (title_value.get(), author_value.get(), year_value.get(), isbn_value.get()))

def update_back():
    backend.update(selected_tuple[0],title_value.get(), author_value.get(), year_value.get(), isbn_value.get())
    #backend.update(selected_tuple[0], selected_tuple[1], selected_tuple[2], selected_tuple[3], selected_tuple[4])

def delete_back():
    # backend.delete(index)
    backend.delete(selected_tuple[0])


l1 = Label(window, text="Title", height=1, width=10)
l1.grid(row=0, column=0)

l2 = Label(window, text="Author", height=1, width=10)
l2.grid(row=0, column=2)

l3 = Label(window, text="Year", height=1, width=10)
l3.grid(row=1, column=0)

l4 = Label(window, text="ISBN", height=1, width=10)
l4.grid(row=1, column=2)

title_value=StringVar()
e1=Entry(window, textvariable=title_value)
e1.grid(row=0, column=1)

author_value=StringVar()
e2=Entry(window, textvariable=author_value)
e2.grid(row=0, column=3)

year_value=StringVar()
e3=Entry(window, textvariable=year_value)
e3.grid(row=1, column=1)

isbn_value=StringVar()
e4=Entry(window, textvariable=isbn_value)
e4.grid(row=1, column=3)

list1=Listbox(window, height=6, width=33)
list1.grid(row=2, column=0, rowspan=6, columnspan=2)

scroll= Scrollbar(window)
scroll.grid(row=2, column=2, rowspan=6)

list1.configure(yscrollcommand=scroll.set)
scroll.configure(command=list1.yview)

list1.bind('<<ListboxSelect>>', get_selected_row)

b1 = Button(window, text="View all", command=view_back, width=15)
b1.grid(row=2, column=3)

b2 = Button(window, text="Search entry", command=search_back, width=15)
b2.grid(row=3, column=3)

b3 = Button(window, text="Add entry", command=add_back, width=15)
b3.grid(row=4, column=3)

b4 = Button(window, text="Update Selected row", command=update_back, width=15)
b4.grid(row=5, column=3)

b5 = Button(window, text="Delete Selected row", command=delete_back, width=15)
b5.grid(row=6, column=3)

b6 = Button(window, text="Close", command=window.destroy, width=15)
b6.grid(row=7, column=3)


window.mainloop()
