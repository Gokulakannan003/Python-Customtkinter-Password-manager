from customtkinter import *
from tkinter import messagebox
from tkinter.filedialog import *
import random

root = CTk()
root.title("Password manager")
root.geometry("500x500")
root.configure(fg_color="#eae0c6")
S = StringVar()


def home():
    Home.configure(fg_color="magenta2")
    Exit.configure(fg_color="orangered")
    Generate.configure(fg_color="orangered")
    frame4.place_forget()
    frame3.place(x=0, y=70)


def generate():
    Home.configure(fg_color="orangered")
    Exit.configure(fg_color="orangered")
    Generate.configure(fg_color="magenta2")
    frame3.place_forget()
    frame4.place(x=0, y=70)


def save_as():
    filepath = asksaveasfilename(filetypes=[("Text File", "*.txt")],
                                 defaultextension=".txt")

    if filepath:
        with open(filepath, "w") as file:
            content1 = "Username: "
            temp = "\n"
            content0 = "Password: "
            content = username_entry.get()
            content2 = password_entry.get()
            final = content1+content
            final1 = content0+content2
            file.write(final)
            file.write(temp)
            file.write(final1)
    username_entry.delete(0, END)
    password_entry.delete(0, END)
    messagebox.showinfo("Done", "Saved successfully")


def generate_password(length, use_lower, use_upper):

    password = []

    if use_lower:
        password.append(random.choice('abcdefghijklmnopqrstuvwxyz'))

    if use_upper:
        password.append(random.choice('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))

    password.append(random.choice('0123456789'))

    password.append(random.choice('!@#$%^&*()-_=+[]{}|;:,.<>?'))

    available_characters = ''

    if use_lower:
        available_characters += 'abcdefghijklmnopqrstuvwxyz'

    if use_upper:
        available_characters += 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

    available_characters += '0123456789!@#$%^&*()-_=+[]{}|;:,.<>?'

    password += random.choices(available_characters, k=length - len(password))

    random.shuffle(password)

    return ''.join(password)


def generate2():

    length = 6 if S.get() == "0" else 8

    use_lower = l.get() == 1

    use_upper = u.get() == 1

    password = generate_password(length, use_lower, use_upper)

    text.delete(1.0, END)

    text.insert(END, password)


frame1 = CTkFrame(root,
                  fg_color="#eae0c6",
                  width=501,
                  corner_radius=0,
                  height=60)
frame1.place(x=0, y=0)

frame2 = CTkFrame(root,
                  fg_color="azure",
                  width=501,
                  corner_radius=0,
                  height=500)
frame2.place(x=0, y=65)

title = CTkLabel(frame1,
                 text="Password Manager",
                 font=("calibri", 30,"bold"))
title.place(x=130, y=20)


Home = CTkButton(frame2,
                 text="Home",
                 font=("calibri", 30, "bold"),
                 corner_radius=0,
                 width=166,
                 hover_color="ivory4",
                 border_width=2,
                 fg_color="orangered",
                 command=home)
Home.place(x=0, y=0)

Generate = CTkButton(frame2,
                     text="Generate",
                     font=("calibri", 30, "bold"),
                     corner_radius=0,
                     width=167,
                     hover_color="ivory4",
                     border_width=2,
                     fg_color="orangered",
                     command=generate)
Generate.place(x=165, y=0)

Exit = CTkButton(frame2,
                 text="Exit",
                 font=("calibri", 30, "bold"),
                 corner_radius=0,
                 width=170,
                 hover_color="ivory4",
                 border_width=2,
                 command=root.destroy,
                 fg_color="orangered")
Exit.place(x=165+165, y=0)

frame3 = CTkFrame(frame2,
                  width=501,
                  height=365,
                  corner_radius=0)
frame3.place(x=0, y=70)

username = CTkLabel(frame3,
                    text="Username:",
                    font=("calibri", 30, "bold"))
username.place(x=25, y=25)

username_entry = CTkEntry(frame3,
                          font=("calibri", 17, "bold"),
                          width=230, corner_radius=8)
username_entry.place(x=180, y=30)

password = CTkLabel(frame3,
                    text="Password:",
                    font=("calibri", 30, "bold"))
password.place(x=25, y=80)

password_entry = CTkEntry(frame3,
                          font=("calibri", 17, "bold"),
                          width=230,
                          corner_radius=8)
password_entry.place(x=180, y=85)

submit = CTkButton(frame3,
                   text="Save",
                   hover_color="ivory4",
                   fg_color="orangered",
                   font=("calibri", 17, "bold"),
                   width=200,
                   height=49,
                   command=save_as)
submit.place(x=160, y=150)

frame4 = CTkFrame(frame2,
                  width=501,
                  height=365,
                  corner_radius=0)

password_length = CTkLabel(frame4,
                           text="Password Length: ",
                           font=("calibri", 25, "bold"))
password_length.place(x=25, y=25)

l_6 = CTkRadioButton(frame4,
                     text="6",
                     font=("calibri", 25, "bold"),
                     hover_color="ivory4",
                     fg_color="orangered",
                     variable=S,
                     value=0)
l_6.place(x=230, y=25)

l_8 = CTkRadioButton(frame4,
                     text="8",
                     font=("calibri", 25, "bold"),
                     hover_color="ivory4",
                     fg_color="orangered",
                     variable=S,
                     value=1)
l_8.place(x=320, y=25)

lower = CTkLabel(frame4,
                 text="Lowercase: ",
                 font=("calibri", 25, "bold"))
lower.place(x=25, y=70)

l = CTkCheckBox(frame4,
                text="",
                corner_radius=0,
                fg_color="orangered",
                hover_color="ivory4",
                onvalue=1,
                offvalue=0)
l.place(x=170, y=75)

upper = CTkLabel(frame4,
                 text="Uppercase: ",
                 font=("calibri", 25, "bold"))
upper.place(x=25, y=70+45)

u = CTkCheckBox(frame4,
                text="",
                corner_radius=0,
                fg_color="orangered",
                hover_color="ivory4",
                onvalue=1,
                offvalue=0)
u.place(x=170, y=75+45)

generate1 = CTkButton(frame4,
                      text="Generate",
                      hover_color="ivory4",
                      fg_color="orangered",
                      font=("calibri", 17, "bold"),
                      width=200,
                      height=49,
                      command=generate2)
generate1.place(x=150, y=75+90+25)

text = CTkTextbox(frame4,
                  fg_color="ivory2",
                  font=("calibri", 17, "bold"),
                  width=200,
                  height=20)
text.place(x=150, y=75+90+25+70)

home()

root.mainloop()
