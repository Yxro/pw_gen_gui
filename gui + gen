import random
import string
from random import randint, choice
from tkinter import *



#window configuration:

window = Tk()
window.title("Password generator")
window.iconbitmap('icons8-show-password-100.ico')
window.geometry('700x200')
window.resizable(False, False)

#text
frame = Canvas(window,
               width=700,
               height=200,
               bg='light grey',
               )

frame.create_text(100,
                  40,
                  text="password lenght:",
                  fill="black",
                  font=('Helvetica 14 bold')
                  )
frame.pack()

#first entry for lenght

entry_lenght = Entry(window,
                     font=('Calibri', 14),
                     fg= 'black',
                     relief= SUNKEN,
                     bd= 4)


entry_lenght.place(x=190, y=25)
entry_lenght = entry_lenght.getint(0)


#genrator loop:
def generator():
    pw = string.ascii_lowercase + string.ascii_uppercase + string.punctuation
    pw_ls = []
    i = 0
    entry_lenght += 1
    while i < entry_lenght:
        i+=1
        if i < entry_lenght:
            u = random.choice(pw)
            pw_ls.append(u)
            result_pw.delete(0, END)
            result_pw.insert(0, pw_ls)

#the pw result:


result_pw = Entry(window,
                  font=('Calibri',14),
                  relief=FLAT,
                  bd=0,
                  fg= 'black',
                  )

result_pw.place(x=250, y= 120)

pw_len = entry_lenght.getint(+0)




#button for the generator

generator_button = Button(window,
                          text= 'Generate password',
                          relief= SUNKEN,
                          bd= 7,
                          bg='white',
                          fg='black',
                          activebackground='grey',
                          font=('Calibri',12),
                          activeforeground='white',
                          command= generator
                          )


generator_button.place(x=450, y=20)


window.mainloop()
