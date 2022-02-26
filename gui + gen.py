import random
import string
import time
import winsound
from tkinter import *

#window configuration:

window = Tk()
window.title("Password generator")
window.iconbitmap('icons8-show-password-100.ico')
window.geometry('700x200')
window.resizable(False, False)




#intro text:
intr_txt = Label(window,
                 text= "PW generator v0.1" ,
                 font=('Calibri', 15),
                 fg= 'black',
                 )
intr_txt.place(x= 270, y = 20)


#first entry for lenght

entry_lenght = Entry(window,
                     font=('Calibri', 14),
                     fg= 'black',
                     relief= SUNKEN,
                     bd= 4,
                     )


entry_lenght.place(x=250, y=65)

#back end

    #generator with a max and min value:
pw = string.ascii_letters + str(string.digits) + string.punctuation
pw_len = random.choice(range(6, 14))

    #generate command
def generator():

    password = []
    for i in range(pw_len):
        password.append(random.choice(pw))
        entry_lenght.delete(0, END)

    for x in password:
        x_1 = entry_lenght.insert(0, x)

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
                          command= generator()
                          )


generator_button.place(x=285, y= 120 )



#save to notepad command:
def save():
    save_time0 = time.ctime()
    save_time = time.strftime('%A %b %Y')
    copied_pw = entry_lenght.get()
    past_pw = open('the saved pw', 'a')
    spec_ln = [16, END]
    past_pw.write("\n"+ copied_pw + '   created on the ' + save_time)


snd_0 = lambda: winsound.PlaySound('Speach Sleep.wav', winsound.SND_FILENAME)


#save button:
save_button = Button(window,
                     text='Save ',
                     relief= SUNKEN,
                     bd= 5,
                     bg='white',
                     fg='Black',
                     activebackground='grey',
                     font=('Calibri', 11),
                     activeforeground='white',
                     command= lambda:[snd_0(), save()]
                     )

save_button.place(x=470, y=62)

window.mainloop()
