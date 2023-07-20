import tkinter as t
from tkinter import ttk
import reviewtype as rt
from tkinter import messagebox
def load():
    def backendcode():
        stop=['i', 'me', 'my', 'myself', 'we', 'our', 'ours', 'ourselves', 'you', 'your', 'yours', 'yourself', 'yourselves', 'he', 'him', 'his', 'himself', 'she', 'her', 'hers', 'herself', 'it', 'its', 'itself', 'they', 'them', 'their', 'theirs', 'themselves', 'what', 'which', 'who', 'whom', 'this', 'that', 'these', 'those', 'am', 'is', 'are', 'was', 'were', 'be', 'been', 'being', 'have', 'has', 'had', 'having', 'do', 'does', 'did', 'doing', 'a', 'an', 'the', 'and', 'but', 'if', 'or', 'because', 'as', 'until', 'while', 'of', 'at', 'by', 'for', 'with', 'about', 'against', 'between', 'into', 'through', 'during', 'before', 'after', 'above', 'below', 'to', 'from', 'up', 'down', 'in', 'out', 'on', 'off', 'over', 'under', 'again', 'further', 'then', 'once', 'here', 'there', 'when', 'where', 'why', 'how', 'all', 'any', 'both', 'each', 'few', 'more', 'most', 'other', 'some', 'such', 'nor', 'only', 'own', 'same', 'so', 'than', 'too', 'very', 's', 't', 'can', 'will', 'just', 'don', 'should', 'now',]
        text=t1.get("1.0", "end-1c")
        textdata=text.split(' ')
        valid=0
        for i in textdata:
            if i in stop:
                valid+=1
        if valid<3 or len(text)<10:
            messagebox.showwarning("invalid","right at least 10 meaningful words")
            return 0
        res=rt.predictdata([text])
        print('button clicked')
        if res[0]=='hotel':
                messagebox.showinfo("hotel","seems like it is a hotel review")
        elif res[0]=='movie':
                messagebox.showinfo("movie","seems like it is a movie review")
        elif res[0]=='mail':
                messagebox.showinfo("mail","seems like it is a mail review")    
    win=t.Tk()
    win.geometry('600x500')
    win.title('Project Name')
    win.resizable(False,False)
    ###########frames Design done###################
    top=t.Frame(win,width=600,height=100,bd=2,relief='raise',pady=4,padx=40)
    top.pack(side='top')
    middle=t.Frame(win,width=600,height=400,bd=2,relief='raise',pady=20,padx=20)
    middle.pack(side='top')
    ###########top frame design##########################
    l1=t.Label(top,text='Check Review Type',font=('arial',20,'bold'),pady=10)
    l1.pack(side='top')
    con1='''       This Section basically helps the user to guess the type of
        review it bassically take the data and accordingly predict
        that which type of review it belongs
        Try it Once'''
    l2=t.Label(top,text=con1,font=('arial',14),justify='left',pady=12)
    l2.pack(side='top')
    ########################middle part design###############
    l3=t.Label(middle,text='Fill Details',font=('arial',16,'bold'),justify='left')
    t1=t.Text(middle,height=8,width=45,font=('arial',11))
    b1=t.Button(middle,text='Submit',font=('arial',14),command=backendcode)
    l3.place(x=10,y=20)
    t1.place(x=10,y=70)
    b1.place(x=10,y=220)

