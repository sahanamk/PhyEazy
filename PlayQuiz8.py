import pickle
from tkinter import *

tk=Tk()
tk.title('Login')
tk.geometry('500x500') #Dimensions of the space
tk.configure(bg='#ffecad')#background color

QuestList = []
Ques = []
Q=StringVar()
op1 = StringVar()
op2 = StringVar()
op3 = StringVar()
op4 = StringVar()
ropv = StringVar()
rop=0
score=0
cor=''
count = [10]
j=[0]

def Ranseval():
     global cor
     if cor!=0:
        cor=Label(tk,text='\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t',bg='#ffecad',width=30,font=("plasma  Brk",20,'bold'),fg='#00ad7f').place(x=-50, y=600, anchor = W)
     Next.destroy()
     print('Correct Option!')
     j[0]+=1
     count[0] -=1
     ProcessQuest()
     
def PlayQuiz():
     with ( open("Quiz8.txt", "rb")) as log_file:
            while True:
                 try:
                    QuestList.append( pickle.load(log_file))
                    #print(QuestList)
                 except EOFError:
                    break
     ProcessQuest()
     #for j in range( len(QuestList)):
def ProcessQuest():  
     global rop
     if count[0] !=0 :
          x = QuestList[j[0]]
          print(x)
          for key in x:
               print(x[key][0])
               if count[0] !=0 :
                    Q.set(x[key][0])
                    op1.set(x[key][1])
                    op2.set(x[key][2])
                    op3.set(x[key][3])
                    op4.set(x[key][4])
                    
               
                    #rop.set(x[key][5])
                    rop=x[key][5]
     else:
          print(score)
          A.destroy()
          B.destroy()
          C.destroy()
          D.destroy()
          cor=Label(tk,text='\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t',bg='#ffecad',width=30,font=("plasma  Brk",20,'bold'),fg='#00ad7f').place(x=-50, y=600, anchor = W)
          qe=Label(tk,text='\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t',bg='#ffecad',width=30,font=("plasma  Brk",20,'bold'),fg='#00ad7f').place(x=300, y=150, anchor = W)
          S=Label(tk,text='Your score is:',bg='#ffecad',width=30,font=("plasma  Brk",30,'bold'),fg='#00ad7f').place(x=400, y=300, anchor = W)
          Score=Label(tk,text=score,bg='#ffecad',width=30,font=("plasma  Brk",30,'bold'),fg='#00ad7f').place(x=450, y=400, anchor = W)
          def Back7():
               tk.destroy()
          back=Button(tk, text='Back to Class 7',font=("plasma  Brk",20,'bold'),fg='#00ad7f', width = 30,command = Back7)
          back.pack()
          back.place(x = 500,y = 600)
               
               
def NextA():
    global score
    global Next
    global cor
    if rop=='A':
        score+=1
        cor=Label(tk,text='Correct Option!',bg='#ffecad',width=30,font=("plasma  Brk",20,'bold'),fg='#00ad7f').place(x=-150, y=600, anchor = W)
    else:
        if rop=='B':
             cor=Label(tk,text='Sorry, the right option is B',bg='#ffecad',width=30,font=("plasma  Brk",20,'bold'),fg='#00ad7f').place(x=-50, y=600, anchor = W)
        if rop=='C':
             cor=Label(tk,text='Sorry, the right option is C',bg='#ffecad',width=30,font=("plasma  Brk",20,'bold'),fg='#00ad7f').place(x=-50, y=600, anchor = W)
        if rop=='D':
             cor=Label(tk,text='Sorry, the right option is D',bg='#ffecad',width=30,font=("plasma  Brk",20,'bold'),fg='#00ad7f').place(x=-50, y=600, anchor = W)
    Next=Button(tk, height=1, width=12, bg='coral2', text='Next', font=('Castellar',27), command=Ranseval)
    Next.place(x = 600,y = 600)
    
def NextB():
    global Next
    global score
    global cor
    if rop=='B':
        score+=1
        cor=Label(tk,text='Correct Option!',bg='#ffecad',width=30,font=("plasma  Brk",20,'bold'),fg='#00ad7f').place(x=-50, y=600, anchor = W)
    else:
        if rop=='A':
             cor=Label(tk,text='Sorry, the right option is A',bg='#ffecad',width=30,font=("plasma  Brk",20,'bold'),fg='#00ad7f').place(x=-50, y=600, anchor = W)
        if rop=='C':
             cor=Label(tk,text='Sorry, the right option is C',bg='#ffecad',width=30,font=("plasma  Brk",20,'bold'),fg='#00ad7f').place(x=-50, y=600, anchor = W)
        if rop=='D':
             cor=Label(tk,text='Sorry, the right option is D',bg='#ffecad',width=30,font=("plasma  Brk",20,'bold'),fg='#00ad7f').place(x=-50, y=600, anchor = W)
    Next=Button(tk, height=1, width=12, bg='coral2', text='Next', font=('Castellar',27), command=Ranseval)
    Next.place(x = 600,y = 600)

def NextC():
    global Next
    global score
    global cor
    if rop=='C':
        score+=1
        cor=Label(tk,text='Correct Option!',bg='#ffecad',width=30,font=("plasma  Brk",20,'bold'),fg='#00ad7f').place(x=-50, y=600, anchor = W)
    else:
        if rop=='A':
             cor=Label(tk,text='Sorry, the right option is A',bg='#ffecad',width=30,font=("plasma  Brk",20,'bold'),fg='#00ad7f').place(x=-50, y=600, anchor = W)
        if rop=='B':
             cor=Label(tk,text='Sorry, the right option is B',bg='#ffecad',width=30,font=("plasma  Brk",20,'bold'),fg='#00ad7f').place(x=-50, y=600, anchor = W)
        if rop=='D':
             cor=Label(tk,text='Sorry, the right option is D',bg='#ffecad',width=30,font=("plasma  Brk",20,'bold'),fg='#00ad7f').place(x=-50, y=600, anchor = W)
    Next=Button(tk, height=1, width=12, bg='coral2', text='Next', font=('Castellar',27), command=Ranseval)
    Next.place(x = 600,y = 600)
    
def NextD():
    global score
    global Next
    global cor
    if rop=='D':
        score+=1
        cor=Label(tk,text='Correct Option!',bg='#ffecad',width=30,font=("plasma  Brk",20,'bold'),fg='#00ad7f').place(x=-50, y=600, anchor = W)
    else:
        if rop=='A':
             cor=Label(tk,text='Sorry, the right option is A',bg='#ffecad',width=30,font=("plasma  Brk",20,'bold'),fg='#00ad7f').place(x=-50, y=600, anchor = W)
        if rop=='B':
             cor=Label(tk,text='Sorry, the right option is B',bg='#ffecad',width=30,font=("plasma  Brk",20,'bold'),fg='#00ad7f').place(x=-50, y=600, anchor = W)
        if rop=='C':
             cor=Label(tk,text='Sorry, the right option is C',bg='#ffecad',width=30,font=("plasma  Brk",20,'bold'),fg='#00ad7f').place(x=-50, y=600, anchor = W)
    Next=Button(tk, height=1, width=12, bg='coral2', text='Next', font=('Castellar',27), command=Ranseval)
    Next.place(x = 600,y = 600)
               
Que=Label(tk,textvariable=Q,bg='#ffecad',width=80,font=("plasma  Brk",20,'bold'),fg='#00ad7f').place(x=-150, y=150, anchor = W)
A= Button(tk, textvariable = op1,font=('plasma  Brk',14), width = 50,command = NextA)
A.pack()
A.place(x = 500,y = 200)
B= Button(tk, textvariable = op2,font=('plasma  Brk',14), width = 50,command = NextB)
B.place(x = 500,y = 250)
C= Button(tk, textvariable = op3, font=('plasma  Brk',14),width = 50,command = NextC)
C.place(x = 500,y = 300)
D= Button(tk, textvariable = op4, font=('plasma  Brk',14),width = 50,command = NextD)
D.place(x = 500,y = 350)
PlayQuiz()
tk.mainloop()

