from tkinter import *
import pickle, os

''' Installed it in Windows
pip install Pillow'''

tk = Tk()

canvas = Canvas(tk, bg="lightpink", height=750, width=1300)
canvas.pack()

RecList=[]
Record={}


def QNo():
    count=1
    if os.path.isfile("Quiz11.txt"): 
        file=open("Quiz11.txt",'rb')
        try:
            while True:
                Record=pickle.load(file)
                print(Record) 
                count+=1
            count+=1
            file.close()
        except EOFError:
          file.close()
    else:
        count = 1
    return count

def AddQuestions():
    RecList=[]
    QuestNo = QNo()
    
    Quest=Quest1.get("1.0","end-1c")
    RecList.append(Quest)
    AnsA=Ans1.get("1.0","end-1c")
    RecList.append(AnsA)
    AnsB=Ans2.get("1.0","end-1c")
    RecList.append(AnsB)
    AnsC=Ans3.get("1.0","end-1c")
    RecList.append(AnsC)
    AnsD=Ans4.get("1.0","end-1c")
    RecList.append(AnsD)
    Correct=Rop.get("1.0","end-1c")
    RecList.append(Correct)
    print(RecList)
    Record[QuestNo] = RecList
    print(Record)
    Science_file = open("Quiz11.txt", 'ab')
    pickle.dump(Record, Science_file)

    Quest1.delete('1.0',END)
    Ans1.delete('1.0',END)
    Ans2.delete('1.0',END)
    Ans3.delete('1.0',END)
    Ans4.delete('1.0',END)
    Rop.delete('1.0',END)
    
    Science_file.close()


#Label Question
QuestLabel=Label(tk,text='Question:',bg='lightskyblue',width=20,font=("Ms Gothic",20,'bold'),fg='white')
QuestLabel.place(relx=.08,rely=.1)
#Question Text Box
Quest1=Text(tk,width=100,height=2)
Quest1.place(relx=.32,rely=.1)

#Label Option 1
ALabel=Label(tk,text='Option A:',bg='lightskyblue',width=20,font=("Ms Gothic",20,'bold'),fg='white')
ALabel.place(relx=.08,rely=.2)
#Text box for Option 1
Ans1=Text(tk,width=30,height=2)
Ans1.place(relx=.32,rely=.2)

BLabel=Label(tk,text='Option B:',bg='lightskyblue',width=20,font=("Ms Gothic",20,'bold'),fg='white')
BLabel.place(relx=.08,rely=.3)
Ans2=Text(tk,width=30,height=2)
Ans2.place(relx=.32,rely=.3)

CLabel=Label(tk,text='Option C:',bg='lightskyblue',width=20,font=("Ms Gothic",20,'bold'),fg='white')
CLabel.place(relx=.08,rely=.4)
Ans3=Text(tk,width=30,height=2)
Ans3.place(relx=.32,rely=.4)

DLabel=Label(tk,text='Option D:',bg='lightskyblue',width=20,font=("Ms Gothic",20,'bold'),fg='white')
DLabel.place(relx=.08,rely=.5)
Ans4=Text(tk,width=30,height=2)
Ans4.place(relx=.32,rely=.5)

CorrectLabel=Label(tk,text='Correct Option:',bg='teal',width=20,font=("Ms Gothic",20,'bold'),fg='white')
CorrectLabel.place(relx=.08,rely=.6)
Rop=Text(tk,width=30,height=2)
Rop.place(relx=.32,rely=.6)

#Button(tk, height=1, width=10, text="Clear",command=lambda: AddQuestions()).place(x=200,y=600)

# Align the button
Button(tk, height=1, width=10, text="Add",command=lambda: AddQuestions()).place(x=200,y=600)
