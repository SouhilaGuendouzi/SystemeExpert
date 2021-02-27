from tkinter import * 
from tkinter import filedialog

root = Tk()
root.title('read file')
root.geometry("500x450")

def open_txt():
    file1 = filedialog.askopenfilename(initialdir="/home/vvead/Projects/SystemeExpert/", 
    title="Open text file", filetypes=(("Text Files", "*.txt"),))
    file1 = open(file1, 'r')
    f = file1.read()
    my_text.insert(END, f)
    file1.close()

def save_txt():
    file1 = filedialog.askopenfilename(initialdir="/home/vvead/Projects/SystemeExpert/", 
    title="Open text file", filetypes=(("Text Files", "*.txt"),))
    file1 = open(file1, 'w')
    file1.write(my_text.get(1.0, END))

my_text = Text(root, width=40, height=10, font=("Helvetica", 16))
my_text.pack(pady=20)

open_button = Button(root, text="Open text file", command=open_txt)
open_button.pack(pady=20)

save_button = Button(root, text="Save file", command=save_txt)
save_button.pack(pady=20)

root.mainloop()