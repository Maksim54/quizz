from tkinter import *
import tkinter as tk
import sys
import tkinter
from tkinter import messagebox
#это мои попытки сделать немного иной вариант
##class Question:
##    def __init__(self, question, answers, correctLetter):
##        self.question = question
##        self.answers = answers
##        self.correctLetter = correctLetter
##
##    def check(self, letter, view):
##        global right
##        if(letter == self.correctLetter):
##            label = Label(view, text="Right!")
##            right += 1
##        else:
##            label = Label(view, text="Wrong!")
##        label.pack()
##        view.after(1000, lambda *args: self.unpackView(view))
##
##
##    def getView(self, window):
##        view = Frame(window)
##        Label(view, text=self.question).pack()
##        Button(view, text=self.answers[0], command=lambda *args: self.check("A", view)).pack()
##        Button(view, text=self.answers[1], command=lambda *args: self.check("B", view)).pack()
##        Button(view, text=self.answers[2], command=lambda *args: self.check("C", view)).pack()
##        Button(view, text=self.answers[3], command=lambda *args: self.check("D", view)).pack()
##        return view
##class Closeable:
##    def close(self):
##        print('closed')
##with contextlib.closing(Closeable()):
##    pass# печатает closed
##class App():

#Пытался сделать окно совместное с первоначальным,но не вышло(
####    def __init__(self,master):
####        #Frames
####        left_frame = Frame(master)
####        right_frame = Frame(master)
####        left_frame.pack(side="left", fill="both", expand=True)
####        right_frame.pack(side="right", fill="both", expand=True)
####
####        var1 = IntVar()
####        var1a = IntVar()
####
####        #Displaying checkboxes and assigning to variables
####        self.Checkbox = Checkbutton(right_frame, text="Ingredients present in full (any allergens in bold with allergen warning if necessary)", variable=var1)
####        self.Checkbox.grid(column = 1, row = 1, sticky = W)
####        self.Checkbox2 = Checkbutton(right_frame, variable = var1a)
####        self.Checkbox2.grid(column = 0, row = 1, sticky = W)
####
####       ###FRAME 2###
####        #widgets
####        self.msg1 = Label(left_frame, text = "Choose here")
####        self.msg1.grid(column = 0, row = 0)

q = 0
s = -1
count = 0
correct = 0
incorrect = 0

question = ["Now 2021 year?","Are you sure?","Really sure","Ok you are right"]

answer = ["yes","yes","ok","ok"]
answer_cap = ["Yes","Yes","Ok","Ok"]#программа показывает после каждого ответа правильно ли ответил пользователь или нет

def buttonCallback():
    messagebox.showinfo("Message", "You have clicked the Button!")

root = Tk()
root.title('Quiz')
root.geometry('600x340')
name = tk.Label(root,fg='darkslategrey',text = "Quiz about something...")#показывает название опросника
name.pack()
btn1 = tkinter.Button(height=2,width=8,text = "Resolution", bg = "darkmagenta",fg='thistle',command=lambda:root.geometry('800x600'))#'fg or foreground is for coloring the contents (buttons)
btn2 = tkinter.Button(height=2,width=8,text = "Background", bg = "darkmagenta",fg='thistle',command=lambda:root.config(bg='grey'))
btn3 = tk.Button(height=2,width=8,fg='thistle',bg='darkmagenta',text="Click", command=buttonCallback)
label = tk.Label(root,fg='darkslategrey',text = question[0])
label.pack()

entry = tk.Entry(root)
entry.pack()

def Exit():
    root.quit()
def out():#настройка кнопки для считывания ответа введенного в строке
    global q,correct,incorrect,s,count
    count = count + 1
    ans = entry.get()
    print (ans)
    print (question[q])#принтуем вопрос
    print (answer[q])#принтуем ответ
    if count < 4:
          if answer[q] or answer_cap[q] == ans :
              q = q + 1
              entry.delete(0, END)#после введения ответа строка очищается и нам задается следующий вопрос
              correct = correct + 1
              label.config(text = question[q])#засчитывает верные ответы
          else:
              q = q + 1
              entry.delete(0, END)
              incorrect = incorrect + 1
              label.config(text = question[q])#засчитывает неверные ответы
    else:
        entry.delete(0, END)
        label.config(text = "Correct: "+str(correct) + " Incorrect:   "+str(incorrect))#засчитывание каждого ответа и после чего программа выдает нам кол-во правильных ответов


def stop():#настройка кнопки для повторного ответа на вопросы
    global q,correct,incorrect
    q = 0
    correct = 0
    incorrect = 0
    entry.delete(0, END)#удаление всего введенного нами ранее
    label.config(text = question[0])#обнуление всех полученных ответов после нажатия кнопки рестарта


button = tk.Button(root,height=2,width=8,bg='darkmagenta',fg='thistle',text = "Submit",command = out)#кнопка отправки своего ответа для дальнейшей проверки
button.pack()

button_two = tk.Button(root,height=2,width=8,bg='darkmagenta',fg='thistle',text = "Restart",command = stop)#кнопка для повторных ответов или для исправления своих ответов
button_two.pack()

button_three = tk.Button(root,height=2,width=8,bg='darkmagenta',fg='thistle',text = "Exit",command = Exit)#кнопка для выхода из программы
button_three.pack()
root.configure(bg='aliceblue')#концигурации главного окна
btn1.pack()
btn2.pack()
btn3.pack()
root.mainloop()

